#This is the third file for this project, which contains the logic for interacting with database, specially for
#inserting student records.

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models import GraduateDetails

def insert_students(students, db: Session): #This function takes a list of `Student` objects and inserts them into the 
            #`GraduateDetails` table in the database. It also handles transaction commits and rollbacks in case of errors.
    try:
        for student in students:
            student_data = GraduateDetails(
                student_id=student.student_id,
                student_name=student.student_name,
                standard=student.standard,
                place=student.place,
                photo=student.photo
            )
            db.add(student_data)
        db.commit()
        print("Data inserted successfully.")
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")
        db.rollback()
