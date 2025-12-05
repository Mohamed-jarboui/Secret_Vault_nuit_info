from app.db.base import SessionLocal, Base, engine
from app.models.user import User
from app.core.security import get_password_hash

def seed_db():
    # Ensure tables exist
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:
        email = "admin@example.com"
        password = "admin123"
        
        user = db.query(User).filter(User.email == email).first()
        if not user:
            print(f"Creating admin user: {email}")
            user = User(
                email=email,
                hashed_password=get_password_hash(password),
                full_name="Admin User",
                is_superuser=True,
                is_active=True
            )
            db.add(user)
            db.commit()
            print("Admin user created successfully.")
        else:
            print("Admin user already exists. Updating password...")
            user.hashed_password = get_password_hash(password)
            db.add(user)
            db.commit()
            print("Admin password updated.")
            
    except Exception as e:
        print(f"Error seeding DB: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_db()
