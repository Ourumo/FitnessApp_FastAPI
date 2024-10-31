from sqlalchemy.orm import Session
from . import models, schemas, database
from fastapi.encoders import jsonable_encoder
from datetime import datetime

# 화원가입
def regiseter(db: Session, user: schemas.UserRegister, url: str):
    db_user = models.User(
        email=user.email,
        name=user.name,
        password=user.password,
    )
    db_user.profile_img = f"{url}/profile_img/profile_default.jpg"
    db_user.updated_at = datetime.now()
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

# 유저 프로필 업데이트
def update_profile(db: Session, id: int, password: str | None, profileimg):
    db_user = db.query(models.User).filter(models.User.id == id).first()
    if db_user:          
        if profileimg is None:
            url = "profile_img/proile_default.jpg"
        else:
            temp_type = profileimg.filename.split('.')[-1]
            temp_content_type = profileimg.headers['content-type']
            url = f"profile_img/profile_{db_user.id}.{temp_type}"
            try:
                database.s3.upload_fileobj(
                    profileimg.file,
                    database.s3_bucket_name,
                    f"{url}",
                    ExtraArgs={
                        'ContentType': temp_content_type,
                        'ACL': 'public-read'
                    }
                )
            except:
                return None
    if password is not None:
        db_user.password = password
    db_user.profile_img = f"{database.s3_url}/{url}"
    db_user.updated_at = datetime.now()
    db.commit()
    db.refresh(db_user)
    return db_user

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
    if db_memo: 
        db.delete(db_memo)
        db.commit()
        msg = {"message": "success"}
    else:
        msg = {"message": "failure"}
    return msg

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
    if db_datememo:
        db.delete(db_datememo)
        db.commit()
        msg = {"message": "success"}
    else:
        msg = {"message": "failure"}
    return msg

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
    if db_traininglist:
        db_traininglistdetails = db.query(models.TrainingListDetail).filter(
            models.TrainingListDetail.training_list_id == id).all()
        if db_traininglistdetails:
            for training_list_detail in db_traininglistdetails:
                db.delete(training_list_detail)
        db.delete(db_traininglist)
        db.commit()
        msg = {"message": "success"}
    else:
        msg = {"message": "failure"}
    return msg

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

# 운동 read 30개 제한
def read_training_limit(db: Session):
    return db.query(models.Training).limit(30).all()

# 운동 개수 read
def read_training_count(db: Session):
    return db.query(models.Training).count()

# 운동 update
def update_training(db: Session, training: schemas.TrainingUpdate):
    db_training = db.query(models.Training).filter(models.Training.id == training.id).first()
    db_training.category=training.category
    db_training.name=training.name
    db_training.target=training.target
    db_training.tip=training.tip
    db_training.preparation=training.preparation
    db_training.movement=training.movement
    db_training.breathing=training.breathing
    db_training.precautions=training.precautions
    db_training.img=training.img
    db_training.gif=training.gif
    db.add(db_training)
    db.commit()
    db.refresh(db_training)
    return db_training

# 세부 운동 리스트 create
def create_training_list_detail(db: Session, traininglistdetail: schemas.TrainingListDetailCreate):
    db_traininglistdetail = models.TrainingListDetail(
        user_id=traininglistdetail.user_id,
        training_list_id=traininglistdetail.training_list_id,
        training_id=traininglistdetail.training_id,
        content=traininglistdetail.content
    )
    db.add(db_traininglistdetail)
    db.commit()
    db.refresh(db_traininglistdetail)
    return db_traininglistdetail

# 세부 운동 리스트 read
def read_training_list_detail(db: Session, userid: int, traininglistid: int):
    db_traininglistdetail = db.query(models.TrainingListDetail, models.Training).join(
        models.Training,
        models.TrainingListDetail.training_id == models.Training.id
        ).filter(
            models.TrainingListDetail.user_id == userid,
            models.TrainingListDetail.training_list_id == traininglistid
    ).all()
    result = []
    for training_list_detail, training in db_traininglistdetail:
        training_list_detail_data = jsonable_encoder(training_list_detail)
        training_data = jsonable_encoder(training)
        result.append({
            "training_list_detail": training_list_detail_data,
            "training": training_data
        })
    return result

# 세부 운동 리스트 update
def update_training_list_detail(db: Session, traininglistdetail: schemas.TrainingListDetailUpdate):
    db_traininglistdetail = db.query(models.TrainingListDetail).filter(
        models.TrainingListDetail.id == traininglistdetail.id,
        models.TrainingListDetail.user_id == traininglistdetail.user_id
    ).first()
    db_traininglistdetail.content = traininglistdetail.content
    db.add(db_traininglistdetail)
    db.commit()
    db.refresh(db_traininglistdetail)
    return db_traininglistdetail

# 세부 운동 리스트 delete
def delete_training_list_detail(db: Session, id: int, userid: int):
    db_traininglist_detail = db.query(models.TrainingListDetail).filter(
        models.TrainingListDetail.id == id,
        models.TrainingListDetail.user_id == userid
    ).first()
    if db_traininglist_detail:
        db.delete(db_traininglist_detail)
        db.commit()
        msg = {"message": "success"}
    else:
        msg = {"message": "failure"}
    return msg