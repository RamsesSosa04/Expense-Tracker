from fastapi import APIRouter, Depends, HTTPException
from src.shared.schemas.auth import UserCreate, UserLogin, Token

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=Token)
def register(user: UserCreate):
    # Crear usuario y devolver token
    pass

@router.post("/login", response_model=Token)
def login(user: UserLogin):
    # Validar y devolver token
    pass

@router.get("/me")
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
