from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL_DATABASE = "postgresql://postgres:mad123@localhost:5432/GreenHaven"

engine = create_engine(URL_DATABASE)

SessionLocate = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
