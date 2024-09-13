from pydantic import BaseModel

### User
class UserRegister(BaseModel):
    email: str
    name: str
    password: str

class UserCheckEmail(BaseModel):
    email: str

class UserLogin(BaseModel):
    email: str
    password: str
    
### Memo
class MemoCreate(BaseModel):
    user_id: int
    title: str
    content: str

class MemoUpdate(BaseModel):
    id: int
    user_id: int
    title: str
    content: str

### DateMemo
class DateMemoCreate(BaseModel):
    user_id: int
    title: str
    content: str
    datetime: str

class DateMemoUpdate(BaseModel):
    id: int
    user_id: int
    title: str
    content: str

### TrainingList
class TrainingListCreate(BaseModel):
    user_id: int
    name: str

class TrainingListUpdate(BaseModel):
    id: int
    user_id: int
    name: str

### Training
class TrainingCreate(BaseModel):
    category: str
    name: str
    target: str
    tip: str
    preparation: str
    movement: str
    breathing: str
    precautions: str
    img: bytes
    gif: bytes

### TrainingListDetail
class TrainingListDetailCreate(BaseModel):
    user_id: int
    training_list_id: int
    training_id: int
    content: str

class TrainingListDetailUpdate(BaseModel):
    id: int
    user_id: int
    content: str