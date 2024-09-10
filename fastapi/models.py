#This is second file for this project where a table (sandhya_table) is inserted in that particular database
#Defines the database schema for the `GraduateDetails` table.
#This SQLAlchemy ORM class maps to the `my_details` table in the PostgreSQL database. The table includes columns for `student_id`,
#   `student_name`, `standard`, and `place`.
from sqlalchemy import Column, Integer, String, LargeBinary
from database import Base

class GraduateDetails(Base):
    __tablename__ = 'sandhya_table'
    student_id = Column(Integer, primary_key=True)
    student_name = Column(String, nullable=False)
    standard = Column(Integer, nullable=False)
    place = Column(String, nullable=False)
    photo = Column(LargeBinary, nullable=True)
