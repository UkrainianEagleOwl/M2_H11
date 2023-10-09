from typing import List

from fastapi import APIRouter, HTTPException, Depends, status,Query
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from src.database.db import get_db
from src.schemas import ContactModel, ContactResponse, ContactCreate, ContactUpdate
from src.repository import contacts as repository_contacts

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.get("/", response_model=List[ContactResponse])
async def get_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    contacts = await repository_contacts.get_contacts(skip, limit, db)
    return contacts


@router.get("/{contact_id}", response_model=ContactResponse)
async def get_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact(contact_id, db)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact


@router.post("/", response_model=ContactResponse)
async def create_contact(body: ContactCreate, db: Session = Depends(get_db)):
    return await repository_contacts.create_contact(body, db)


@router.put("/{contact_id}", response_model=ContactResponse)
async def update_contact(
    contact_id: int, body: ContactUpdate, db: Session = Depends(get_db)
):
    contact = await repository_contacts.update_contact(contact_id, body, db)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact


@router.delete("/{contact_id}", response_model=ContactResponse)
async def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = await repository_contacts.delete_contact(contact_id, db)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact

@router.get("/search/", response_model=List[ContactResponse])
async def search_contacts(
    name: str = Query(None, description="Search by name"),
    surname: str = Query(None, description="Search by surname"),
    email: str = Query(None, description="Search by email"),
    db: Session = Depends(get_db),
):
    contacts = await repository_contacts.search_contacts(name, surname, email, db)
    return contacts

@router.get("/birthdays/", response_model=List[ContactResponse])
async def get_contacts_with_birthdays(db: Session = Depends(get_db)):
    today = datetime.now()
    next_week = today + timedelta(days=7)
    contacts = await repository_contacts.get_contacts_with_birthdays(today, next_week, db)
    return contacts