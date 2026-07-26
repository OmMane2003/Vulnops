from sqlalchemy.orm import Session
from app.core.security import verify_password
from app.models.user import User
from app.core.security import hash_password


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, full_name: str, email: str, password: str):
    user = User(
        full_name=full_name,
        email=email,
        password_hash=hash_password(password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def authenticate_user(db, email: str, password: str):
    user = get_user_by_email(db, email)

    print("USER:", user)

    if not user:
        print("User not found")
        return None

    print("Stored hash:", user.password_hash)
    print("Password valid:", verify_password(password, user.password_hash))

    if not verify_password(password, user.password_hash):
        return None

    return user