#This is the fourth file for this project which creates FASTAPI endpoints are set up to interact with the (student_data).
from fastapi import FastAPI, HTTPException, Depends, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
from sqlalchemy.orm import Session
from database import get_db
from models import GraduateDetails
import os

app = FastAPI()
UPLOAD_DIR = "uploads/"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/students/")
def create_student(
    student_id: int, student_name: str, standard: int, place: str,
    file: UploadFile = None, db: Session = Depends(get_db)
):
    if db.query(GraduateDetails).filter_by(student_id=student_id).first():
        raise HTTPException(status_code=400, detail="Student already exists")

    student = GraduateDetails(student_id=student_id, student_name=student_name, standard=standard, place=place)

    if file:
        student.photo = file.file.read()  # Save the file as byte data in the database

    db.add(student)
    db.commit()
    db.refresh(student)
    return JSONResponse(content={
        "student_id": student.student_id,
        "student_name": student.student_name,
        "standard": student.standard,
        "place": student.place,
    })


@app.put("/students/{student_id}")
def update_student(
    student_id: int, student_name: str, standard: int, place: str,
    file: UploadFile = None, db: Session = Depends(get_db)
):
    student = db.query(GraduateDetails).filter_by(student_id=student_id).first()
    
    student.student_name = student_name
    student.standard = standard
    student.place = place

    if file:
        student.photo = file.file.read()

    db.commit()
    return JSONResponse(content={
        "student_id": student.student_id,
        "student_name": student.student_name,
        "standard": student.standard,
        "place": student.place,
    })


#  FastAPI doesn’t support returning a file and JSON(photo) response in a single call therefore the boolean
#  function is intitiated so that if it is false then the details will come if it is true then we will get photo
 
@app.get("/students/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db), photo: bool = False):
    student = db.query(GraduateDetails).filter(GraduateDetails.student_id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    if photo:
        if student.photo:
            # Convert byte data to a temporary file and return it
            file_path = os.path.join(UPLOAD_DIR, f"{student_id}_photo.jpg")
            with open(file_path, "wb") as f:
                f.write(student.photo)
            return FileResponse(file_path, media_type="image/jpeg")

        raise HTTPException(status_code=404, detail="Photo not found")

    return JSONResponse(content={
        "student_id": student.student_id,
        "student_name": student.student_name,
        "standard": student.standard,
        "place": student.place,
    })

@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(GraduateDetails).filter_by(student_id=student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"detail": "Student deleted successfully"}



'''POST '/students/' Endpoint: This endpoint allows the client to create a new student record in the database. 
It accepts parameters like `student_id`, `student_name`, `standard`, and `place`, and inserts them into the `GraduateDetails` table.

GET '/students/{student_id}' Endpoint: This endpoint allows the client to retrieve a student's 'student_name',
       'standard', and 'place' by providing the 'student_id'. If the student is not found, it raises a 404 error.

PUT /students/{student_id}: To update an existing students details.

DELETE /students/{student_id}: To delete a student record.'''

#To access we have to run the code and write the command in the terminal as "uvicorn.file_name:app --reload"