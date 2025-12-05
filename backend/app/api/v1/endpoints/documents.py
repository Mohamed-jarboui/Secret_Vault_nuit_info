from typing import List, Any
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session

from app.api import deps
from app.models.user import User
from app.services.mayan_service import mayan_service
from app.services.ai_service import ai_service

router = APIRouter()

@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Upload a document to the Vault (Mayan EDMS) and trigger AI analysis.
    """
    # 1. Upload to Mayan
    content = await file.read()
    doc_metadata = await mayan_service.upload_document(content, file.filename)
    
    # 2. Trigger AI Analysis
    # Extract text from the uploaded file
    try:
        # Try to decode as UTF-8 text first
        extracted_text = content.decode("utf-8")
    except UnicodeDecodeError:
        # If not UTF-8, try to extract from PDF
        try:
            import io
            from PyPDF2 import PdfReader
            
            pdf_file = io.BytesIO(content)
            pdf_reader = PdfReader(pdf_file)
            
            # Extract text from all pages
            extracted_text = ""
            for page in pdf_reader.pages:
                extracted_text += page.extract_text() + "\n"
            
            # If no text extracted, try OCR
            if not extracted_text.strip():
                try:
                    from pdf2image import convert_from_bytes
                    import pytesseract
                    
                    # Convert PDF to images
                    images = convert_from_bytes(content)
                    
                    # OCR each page
                    extracted_text = ""
                    for i, image in enumerate(images):
                        text = pytesseract.image_to_string(image)
                        extracted_text += f"Page {i+1}:\n{text}\n\n"
                    
                    if not extracted_text.strip():
                        extracted_text = f"PDF file uploaded: {file.filename}. No text could be extracted from the PDF (possibly empty or image-only)."
                except Exception as ocr_error:
                    print(f"OCR Error: {ocr_error}")
                    extracted_text = f"PDF file uploaded: {file.filename}. Text extraction failed."
                    
        except Exception as e:
            # Fallback for other binary files
            print(f"File extraction error: {e}")
            extracted_text = f"Binary file uploaded: {file.filename}. Content analysis not supported for this file type."

    summary = await ai_service.summarize(extracted_text)
    
    # 3. Save to Local DB for Search
    from app.models.document import Document
    db_doc = Document(
        filename=file.filename,
        mayan_id=doc_metadata.get("id"),
        ai_summary=summary,
        owner_id=current_user.id
    )
    db.add(db_doc)
    db.commit()
    db.refresh(db_doc)

    return {
        "filename": file.filename,
        "mayan_id": doc_metadata.get("id"),
        "ai_summary": summary,
        "status": "stored_and_analyzed"
    }

@router.get("/search")
async def search_documents(
    q: str,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Search for documents.
    """
    from app.models.document import Document
    # Simple case-insensitive search on filename or summary
    results = db.query(Document).filter(
        (Document.filename.ilike(f"%{q}%")) | 
        (Document.ai_summary.ilike(f"%{q}%"))
    ).all()
    
    return [{"id": doc.id, "label": doc.filename, "summary": doc.ai_summary} for doc in results]
