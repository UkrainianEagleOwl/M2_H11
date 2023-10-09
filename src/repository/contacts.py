from sqlalchemy.orm import Session
from typing import List, Optional
from src.database.models import Contact
from src.schemas import ContactCreate, ContactUpdate
from datetime import datetime

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

async def search_contacts(
    db: Session, name: str = None, surname: str = None, email: str = None 
) -> List[Contact]:
    query = db.query(Contact)
    if name:
        query = query.filter(Contact.name.ilike(f"%{name}%"))
    if surname:
        query = query.filter(Contact.surname.ilike(f"%{surname}%"))
    if email:
        query = query.filter(Contact.email.ilike(f"%{email}%"))
    contacts = await query.all()
    return contacts

async def get_contacts_with_birthdays(
    start_date: datetime, end_date: datetime, db: Session
) -> List[Contact]:
    contacts = (
        db.query(Contact)
        .filter(Contact.birthday.between(start_date.date(), end_date.date()))
        .all()
    )
    return contacts
