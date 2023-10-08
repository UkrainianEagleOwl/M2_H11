from pydantic import BaseModel, EmailStr, HttpUrl
from datetime import date,datetime

class ContactModel(BaseModel):
    name: str
    surname: str
    email: EmailStr
    phone_number: str
    birthday: date
    additional_data: str

class ContactCreate(ContactModel):
    pass

class ContactUpdate(ContactModel):
    pass

class ContactResponse(ContactModel):
    id: int
    name: str
    surname: str
    email: EmailStr
    phone_number: str
    birthday: date
    additional_data: str
    created_at: datetime

    class Config:
        orm_mode = True
