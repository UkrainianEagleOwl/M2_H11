from sqlalchemy.orm import Session
from typing import List, Optional
from src.database.models import Contact
from src.schemas import ContactCreate, ContactUpdate

async def get_contacts(skip: int, limit: int, db: Session) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()

async def get_contact(contact_id: int, db: Session) -> Optional[Contact]:
    return db.query(Contact).filter(Contact.id == contact_id).first()

async def create_contact(contact: ContactCreate, db: Session) -> Contact:
    db_contact = Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

async def update_contact(contact_id: int, contact: ContactUpdate, db: Session) -> Optional[Contact]:
    db_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if db_contact:
        for key, value in contact.dict().items():
            setattr(db_contact, key, value)
        db.commit()
        db.refresh(db_contact)
    return db_contact

async def delete_contact(contact_id: int, db: Session) -> Optional[Contact]:
    db_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if db_contact:
        db.delete(db_contact)
        db.commit()
    return db_contact
