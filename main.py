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

# 회원가입
@app.post("/register")
def register(user: schemas.UserRegister, db: Session = Depends(get_db)):
    db_user = crud.check_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="이메일 중복")
    return crud.regiseter(db, user=user)

# 로그인
@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.login(db, user=user)
    if db_user is None:
        raise HTTPException(status_code=400, detail="아이디나 비밀번호 틀림")
    return db_user

# 메모 생성
@app.post("/memo")
def create_memo(memo: schemas.MemoCreate, db: Session = Depends(get_db)):
    return crud.create_memo(db, memo=memo)

# 메모 로드
@app.get("/memo")
def read_memo(userid: int, db: Session = Depends(get_db)):
    return crud.read_memo(db, userid=userid)

# 메모 업데이트
@app.put("/memo")
def update_memo(memo: schemas.MemoUpdate, db: Session = Depends(get_db)):
    return crud.update_memo(db, memo=memo)

# 메모 삭제
@app.delete("/memo")
def delete_memo(id: int, userid: int, db: Session = Depends(get_db)):
    return crud.delete_memo(db, id=id, userid=userid)