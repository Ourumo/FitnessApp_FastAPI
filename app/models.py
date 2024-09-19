from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    password = Column(String)
    profile_img = Column(String)
    updated_at = Column(String)
    
class Memo(Base):
    __tablename__ = "memos"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String)
    content = Column(String)
    
class DateMemo(Base):
    __tablename__ = "date_memos"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String)
    content = Column(String)
    datetime = Column(String)
    
class TrainingList(Base):
    __tablename__ = "training_list"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    
class Training(Base):
    __tablename__ = "training"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String)
    name = Column(String)
    target = Column(String)
    tip = Column(String)
    preparation = Column(String)
    movement = Column(String)
    breathing = Column(String)
    precautions = Column(String)
    img = Column(String)
    gif = Column(String)

class TrainingListDetail(Base):
    __tablename__ = "training_list_detail"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('training_list.user_id'))
    training_list_id = Column(Integer, ForeignKey('training_list.id'))
    training_id = Column(Integer, ForeignKey('training.id'))
    content = Column(String)