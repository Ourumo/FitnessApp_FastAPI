from sqlalchemy.orm import Session
from . import models, schemas

# 화원가입
def regiseter(db: Session, user: schemas.UserRegister):
    db_user = models.User(
        email=user.email,
        name=user.name,
        password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# 이메일 중복 확인
def check_email(db: Session, email):
    return db.query(models.User).filter(models.User.email == email).first()

# 로그인
def login(db: Session, user: schemas.UserLogin):
    return db.query(models.User).filter(
        models.User.email == user.email,
        models.User.password == user.password
    ).first()

# 메모 create
def create_memo(db: Session, memo: schemas.MemoCreate):
    db_memo = models.Memo(
        user_id=memo.user_id,
        title=memo.title,
        content=memo.content
    )
    db.add(db_memo)
    db.commit()
    db.refresh(db_memo)
    return db_memo

# 메모 read
def read_memo(db: Session, userid: int):
    return db.query(models.Memo).filter(models.Memo.user_id == userid).all()

# 메모 update
def update_memo(db: Session, memo: schemas.MemoUpdate):
    db_memo = db.query(models.Memo).filter(models.Memo.id == memo.id, models.Memo.user_id == memo.user_id).first()
    db_memo.title = memo.title
    db_memo.content = memo.content
    db.commit()
    db.refresh(db_memo)
    return db_memo

# 메모 delete
def delete_memo(db: Session, id: int, userid: int):
    db_memo = db.query(models.Memo).filter(models.Memo.id == id, models.Memo.user_id == userid).first()
    db.delete(db_memo)
    db.commit()
    return {"message": "success"}