# This is the fifth file for this project, Used to insert initial data into the database. 
# this data will be fixed and new student data which is posted will be automatically does into database and we can get that too.

from database import Base, engine, get_db
from models import GraduateDetails
from crud import insert_students
from typing import List
from sqlalchemy.orm import Session

# Create the table in the database
Base.metadata.create_all(bind=engine)

class Student:
    def __init__(self, student_id: int, student_name: str, standard: int, place: str, photo: str = None):
        self.student_id = student_id
        self.student_name = student_name
        self.standard = standard
        self.place = place
        self.photo = photo

    def __repr__(self):
        return str((self.student_id, self.student_name, self.standard, self.place))

students = [
    Student(student_id=101, student_name="Sandhya", standard=10, place="Hyderabad"),
    Student(student_id=102, student_name="Swathi", standard=9, place="Karimnagar"),
    Student(student_id=103, student_name="Sreeja", standard=8, place="Siricilla"),
    Student(student_id=104, student_name="Swetha", standard=7, place="Kothagudem"),
    Student(student_id=105, student_name="Jayanthi", standard=6, place="Andra"),
    Student(student_id=106, student_name="Vaishnavi", standard=10, place="SangaReddy")
]

def main():
    with next(get_db()) as db:
        insert_students(students, db)

if __name__ == "__main__":
    main()
