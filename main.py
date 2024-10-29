from fastapi import Depends, FastAPI, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal, engine, s3, s3_url
from typing import Optional

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# 의존성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 루트 페이지
@app.get("/")
def home():
    return {"message": "This page is FitnessApp Server Page!"}

### 유저
# 회원가입
@app.post("/user/register")
def register(user: schemas.UserRegister, db: Session = Depends(get_db)):
    db_user = crud.check_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="이메일 중복")
    return crud.regiseter(db, user=user, url=s3_url)

# 로그인
@app.post("/user/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.login(db, user=user)
    if db_user is None:
        raise HTTPException(status_code=400, detail="아이디나 비밀번호 틀림")
    return db_user

# 프로필 변경
@app.put("/user/profile")
def update_profile(id: int = Form(...), password: str = Form(None), profileimg: Optional[UploadFile] = File(None), db: Session = Depends(get_db)):
    db_user = crud.update_profile(db, id=id, password=password, profileimg=profileimg)
    if db_user is None:
        raise HTTPException(status_code=400, detail="없는 유저인데유")
    return db_user

### 메모
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

### 달력 메모
# 달력 메모 생성
@app.post("/datememo")
def create_datememo(datememo: schemas.DateMemoCreate, db: Session = Depends(get_db)):
    return crud.create_datememo(db, datememo=datememo)

# 달력 메모 로드
@app.get("/datememo")
def read_datememo(userid: int, db: Session = Depends(get_db)):
    return crud.read_datememo(db, userid=userid)

# 달력 메모 업데이트
@app.put("/datememo")
def update_datememo(datememo: schemas.DateMemoUpdate, db: Session = Depends(get_db)):
    return crud.update_datememo(db, datememo=datememo)

# 달력 메모 삭제
@app.delete("/datememo")
def delete_datememo(id: int, userid: int, db: Session = Depends(get_db)):
    return crud.delete_datememo(db, id=id, userid=userid)

### 운동 리스트
# 운동 리스트 생성
@app.post("/traininglist")
def create_training_list(traininglist: schemas.TrainingListCreate, db: Session = Depends(get_db)):
    return crud.create_training_list(db, traininglist=traininglist)

# 운동 리스트 로드
@app.get("/traininglist")
def read_training_list(userid: int, db: Session = Depends(get_db)):
    return crud.read_training_list(db, userid=userid)

# 운동 리스트 업데이트
@app.put("/traininglist")
def update_training_list(traininglist: schemas.TrainingListUpdate, db: Session = Depends(get_db)):
    return crud.update_training_list(db, traininglist=traininglist)

# 운동 리스트 삭제
@app.delete("/traininglist")
def delete_training_list(id: int, userid: int, db: Session = Depends(get_db)):
    return crud.delete_training_list(db, id=id, userid=userid)

### 운동
# 운동 추가
@app.post("/training")
def create_training(training: schemas.TrainingCreate, db: Session = Depends(get_db)):
    return crud.create_training(db, training=training)

# 운동 로드
@app.get("/training")
def read_training(db: Session = Depends(get_db)):
    return crud.read_training(db)

# 운동 로드 20개 제한
@app.get("/training/limit")
def read_training_limit(db: Session = Depends(get_db)):
    return crud.read_training_limit(db)

# 운동 개수 로드
@app.get("/training/count")
def read_training_count(db: Session = Depends(get_db)):
    return crud.read_training_count(db)

# 운동 업데이트
@app.put("/training")
def update_training(training: schemas.TrainingUpdate, db: Session = Depends(get_db)):
    return crud.update_training(db, training=training)

### 세부 운동 리스트
# 세부 운동 리스트 생성
@app.post("/traininglistdetail")
def create_training_list_detail(traininglistdetail: schemas.TrainingListDetailCreate, db: Session = Depends(get_db)):
    return crud.create_training_list_detail(db, traininglistdetail=traininglistdetail)

# 세부 운동 리스트 로드
@app.get("/traininglistdetail")
def read_training_list_detail(userid: int, traininglistid: int, db: Session = Depends(get_db)):
    return crud.read_training_list_detail(db, userid=userid, traininglistid=traininglistid)

# 세부 운동 리스트 업데이트
@app.put("/traininglistdetail")
def update_training_list_detail(traininglistdetail: schemas.TrainingListDetailUpdate, db: Session = Depends(get_db)):
    return crud.update_training_list_detail(db, traininglistdetail=traininglistdetail)

# 세부 운동 리스트 삭제
@app.delete("/traininglistdetail")
def delete_training_list_detail(id: int, userid: int, db: Session = Depends(get_db)):
    return crud.delete_training_list_detail(db, id=id, userid=userid)