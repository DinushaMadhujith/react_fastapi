from sqlalchemy import Column, Integer, String, Float
from database import Base

class Signup(Base):
    __tablename__ = 'signup'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, nullable=False)
    type = Column(String, nullable=False)  # customer, labor, admin, deliver, farmer
    password = Column(String, nullable=False)  # Store hashed passwords in production

class Contact(Base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    telephone_num = Column(String, nullable=False)
    email = Column(String, nullable=False)
    product_type = Column(String, nullable=False)
    message = Column(String, nullable=False)
class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, nullable=False)
    item_category = Column(String, nullable=False)
    item_description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    #image_url = Column(String, nullable=True)  # URL for the item image

