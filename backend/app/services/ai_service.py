import os
from groq import Groq

class AIService:
    def __init__(self):
        # Initialize Groq client
        api_key = os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=api_key) if api_key else None
        self.model = "llama-3.3-70b-versatile"

    async def summarize(self, text: str) -> str:
        """
        Generate a summary using Groq API.
        """
        if not self.client:
            return "Error: GROQ_API_KEY not found in environment variables."

        if not text:
            return "No content to summarize."

        prompt = f"Summarize the following document in 3 concise bullet points:\n\n{text}"
        
        try:
            # Groq call (synchronous, but fast enough)
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=self.model,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            print(f"AI Service Error: {e}")
            return f"AI Service Error: {str(e)}"

ai_service = AIService()
