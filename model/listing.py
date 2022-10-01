# Define Listing class inheriting from Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INTEGER, String, BIGINT

Base = declarative_base()

# Create a DeclarativeMeta instance
Base = declarative_base()


class Listing(Base):
    __tablename__ = 'listings'
    listing_id = Column(INTEGER, primary_key=True)
    address = Column(String(1000))
    price = Column(BIGINT)

