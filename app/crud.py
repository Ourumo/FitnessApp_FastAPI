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