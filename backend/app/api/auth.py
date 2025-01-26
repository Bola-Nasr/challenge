"""
Authentication endpoints.
"""
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import get_db
import bcrypt
import jwt
from datetime import datetime, timedelta

router = APIRouter()

SECRET_KEY = "W&D Bola Challenge"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Token(BaseModel):
    """
    Token response model.
    """
    access_token: str
    token_type: str


def create_access_token(
    data: dict,
    expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
):
    """
    Create a JWT token with an expiration time.
    :param data:
    :param expires_delta:
    :return:
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# TODO:User authentication (Hardcoded for demo, should be dynamic in real app)
fake_users_db = {
    "admin": {
        "username": "admin",
        "password": bcrypt.hashpw("admin".encode("utf-8"), bcrypt.gensalt()).decode(
            "utf-8"
        ),
    }
}


@router.post("/api/login", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    """
    Login endpoint to generate a JWT token after successful authentication.
    :param form_data:
    :param db:
    :return:
    """
    user = fake_users_db.get(form_data.username)

    if not user or not bcrypt.checkpw(
        form_data.password.encode("utf-8"), user["password"].encode("utf-8")
    ):
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}
