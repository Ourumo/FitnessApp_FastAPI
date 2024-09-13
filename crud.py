from sqlalchemy.orm import Session
from . import models, schemas

# 화원가입
def regiseter(db: Session, user: schemas.UserRegister):
    checkUser = db.query(models.User).filter(models.User.email == user.email).first()
    if checkUser is None:
        return None
    else:
        db_user = models.User(
            email=user.email,
            name=user.name,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

# 로그인
def login(db: Session, user: schemas.UserLogin):
    db_user = db.query(models.User).filter(
        models.User.email == user.email,
        models.User.password == user.password
    ).first()
    if db_user is None:
        return None
    else:
        return db_user