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

class MemoDelete(BaseModel):
    id: int
    user_id: int

### DateMemo
class DateMemoCreate(BaseModel):
    user_id: int
    title: str
    content: str
    datetime: str

class DateMemoRead(BaseModel):
    user_id: int

class DateMemoUpdate(BaseModel):
    id: int
    user_id: int
    title: str
    content: str

class DateMemoDelete(BaseModel):
    id: int
    user_id: int

### TrainingList
class TrainingListCreate(BaseModel):
    user_id: int
    name: str

class ALLTrainingListRead(BaseModel):
    user_id: int

class TrainingListRead(BaseModel):
    id: int
    user_id: int

class TrainingListUpdate(BaseModel):
    id: int
    user_id: int
    name: str

class TrainingListDelete(BaseModel):
    id: int
    user_id: int

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

class TrainingRead(BaseModel):
    id: int

### TrainingListDetail
class TrainingListDetailCreate(BaseModel):
    user_id: int
    training_list_id: int
    training_id: int
    content: str

class ALLTrainingListDetailRead(BaseModel):
    user_id: int

class TrainingListDetailRead(BaseModel):
    user_id: int
    training_list_id: int

class TrainingListDetailUpdate(BaseModel):
    id: int
    user_id: int
    content: str

class TrainingListDetailDelete(BaseModel):
    id: int
    user_id: int