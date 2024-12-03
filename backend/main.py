
# main.py
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import engine, SessionLocate
import models
from typing import Annotated


app = FastAPI()
models.Base.metadata.create_all(bind=engine)
# Dependency to get DB session
def get_db():
    db = SessionLocate()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

# Signup model for API
class SignupBase(BaseModel):
    name: str
    email: str
    phone_number: str
    type: str  # customer, labor, admin, deliver, farmer
    password: str

@app.post("/signup/")
async def create_signup(signup: SignupBase, db: db_dependency):
    # Check if email already exists
    existing_user = db.query(models.Signup).filter(models.Signup.email == signup.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
     # Add new user
    db_signup = models.Signup(
        name=signup.name,
        email=signup.email,
        phone_number=signup.phone_number,
        type=signup.type,
        password=signup.password  # Ideally, use a hashed password
    )
    db.add(db_signup)
    db.commit()
    db.refresh(db_signup)
    return {"message": "Signup successful", "user_id": db_signup.id}

# Contact model for API
class ContactBase(BaseModel):
    name: str
    telephone_num: str
    email: str
    product_type: str
    message: str
@app.post("/contact/")
async def create_contact(contact: ContactBase, db: db_dependency):
    # Add new contact entry
    db_contact = models.Contact(
        name=contact.name,
        telephone_num=contact.telephone_num,
        email=contact.email,
        product_type=contact.product_type,
        message=contact.message
    )
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return {"message": "Contact entry created successfully", "contact_id": db_contact.id}

# Item model for API
class ItemBase(BaseModel):
    item_name: str
    item_category: str
    item_description: str
    price: float
    quantity: int
    #image_url: str | None = None  # Optional image URL
@app.post("/item/")
async def create_item(item: ItemBase, db: db_dependency):
    # Add new item entry
    db_item = models.Item(
        item_name=item.item_name,
        item_category=item.item_category,
        item_description=item.item_description,
        price=item.price,
        quantity=item.quantity,
        #image_url=item.image_url
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"message": "Item created successfully", "item_id": db_item.id}