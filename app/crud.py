from sqlalchemy.orm import Session
from . import models, schemas

# 화원가입
def regiseter(db: Session, user: schemas.UserRegister):
    db_user = models.User(
        email=user.email,
        name=user.name,
        password=user.password,
        profile_img="assets/profile_default.jpg" # 이미지 관련 코드 작성 필요
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
    db_memo = db.query(models.Memo).filter(
        models.Memo.id == memo.id,
        models.Memo.user_id == memo.user_id
    ).first()
    db_memo.title = memo.title
    db_memo.content = memo.content
    db.commit()
    db.refresh(db_memo)
    return db_memo

# 메모 delete
def delete_memo(db: Session, id: int, userid: int):
    db_memo = db.query(models.Memo).filter(
        models.Memo.id == id,
        models.Memo.user_id == userid
    ).first()
    db.delete(db_memo)
    db.commit()
    return {"message": "success"}

# 달력 메모 create
def create_datememo(db: Session, datememo: schemas.DateMemoCreate):
    db_datememo = models.DateMemo(
        user_id=datememo.user_id,
        title=datememo.title,
        content=datememo.content,
        datetime=datememo.datetime
    )
    db.add(db_datememo)
    db.commit()
    db.refresh(db_datememo)
    return db_datememo

# 달력 메모 read
def read_datememo(db: Session, userid: int):
    return db.query(models.DateMemo).filter(models.DateMemo.user_id == userid).all()

# 달력 메모 update
def update_datememo(db: Session, datememo: schemas.DateMemoUpdate):
    db_datememo = db.query(models.DateMemo).filter(
        models.DateMemo.id == datememo.id,
        models.DateMemo.user_id == datememo.user_id
    ).first()
    db_datememo.title = datememo.title
    db_datememo.content = datememo.content
    db.commit()
    db.refresh(db_datememo)
    return db_datememo

# 달력 메모 delete
def delete_datememo(db: Session, id: int, userid: int):
    db_datememo = db.query(models.DateMemo).filter(
        models.DateMemo.id == id,
        models.DateMemo.user_id == userid
    ).first()
    db.delete(db_datememo)
    db.commit()
    return {"message": "success"}

# 운동 리스트 create
def create_training_list(db: Session, traininglist: schemas.TrainingListCreate):
    db_traininglist = models.TrainingList(
        user_id=traininglist.user_id,
        name=traininglist.name
    )
    db.add(db_traininglist)
    db.commit()
    db.refresh(db_traininglist)
    return db_traininglist

# 운동 리스트 read
def read_training_list(db: Session, userid: int):
    return db.query(models.TrainingList).filter(models.TrainingList.user_id == userid).all()

# 운동 리스트 update
def update_training_list(db: Session, traininglist: schemas.TrainingListUpdate):
    db_traininglist = db.query(models.TrainingList).filter(
        models.TrainingList.id == traininglist.id,
        models.TrainingList.user_id == traininglist.user_id
    ).first()
    db_traininglist.name = traininglist.name
    db.commit()
    db.refresh(db_traininglist)
    return db_traininglist

# 운동 리스트 delete
def delete_training_list(db: Session, id: int, userid: int):
    db_traininglist = db.query(models.TrainingList).filter(
        models.TrainingList.id == id,
        models.TrainingList.user_id == userid
    ).first()
    db.delete(db_traininglist)
    db.commit()
    return {"message": "success"}

# 운동 create
def create_training(db: Session, training: schemas.TrainingCreate):
    db_training = models.Training(
        category=training.category,
        name=training.name,
        target=training.target,
        tip=training.tip,
        preparation=training.preparation,
        movement=training.movement,
        breathing=training.breathing,
        precautions=training.precautions,
        img=training.img,
        gif=training.gif
    )
    db.add(db_training)
    db.commit()
    db.refresh(db_training)
    return db_training

# 운동 read
def read_training(db: Session):
    return db.query(models.Training).all()