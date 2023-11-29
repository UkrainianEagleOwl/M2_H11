
# Contact Management REST API

## Overview
This project is a REST API for managing contact information, built using FastAPI and SQLAlchemy with a PostgreSQL database. It supports creating, retrieving, updating, and deleting contacts, as well as searching and birthday reminders.

## Features
- **CRUD Operations**:
  - Create, read, update, and delete contact information.
- **Contact Information**:
  - Store name, surname, email, phone number, birthday, and additional data.
- **Search Functionality**:
  - Search contacts by name, surname, or email address.
- **Birthday Reminders**:
  - Retrieve contacts with birthdays in the next 7 days.
- **API Documentation**:
  - Auto-generated documentation for the API.
- **Data Validation**:
  - Pydantic models for request and response data validation.

## Technical Details
- **FastAPI Framework**: 
  - For building a high-performance, easy-to-use RESTful API.
- **SQLAlchemy ORM**:
  - For database interactions and schema management.
- **PostgreSQL Database**:
  - Chosen for its robustness and scalability.
- **Pydantic**:
  - For validating and managing request and response data models.

## Usage
- **Running the API**:
  - Launch the API server and access endpoints for managing contacts.
- **Endpoints**:
  - `POST /contacts`: Create a new contact.
  - `GET /contacts`: Retrieve all contacts.
  - `GET /contacts/{id}`: Retrieve a contact by ID.
  - `PUT /contacts/{id}`: Update a contact.
  - `DELETE /contacts/{id}`: Delete a contact.
  - `GET /search`: Search contacts.
  - `GET /birthdays`: Get contacts with upcoming birthdays.

## Installation and Dependencies
- Clone the repository.
- Ensure Python, FastAPI, SQLAlchemy, PostgreSQL, and Pydantic are installed.
- Set up a PostgreSQL database and configure the connection in the application.
 
