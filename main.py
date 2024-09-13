from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# 의존성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "This page is FitnessApp Server Page!"}

@app.post("/register")
def register(user: schemas.UserRegister, db: Session = Depends(get_db)):
    db_user = crud.check_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="이메일 중복")
    return crud.regiseter(db=db, user=user)

@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.login(db, user=user)
    if db_user is None:
        raise HTTPException(status_code=400, detail="아이디나 비밀번호 틀림")
    return db_user