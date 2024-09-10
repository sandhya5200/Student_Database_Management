#This is the first file for this project before this we have to create a database in postgresql.
#This file handles the connection to the postgreSQL database.
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, declarative_base

db_user = 'postgres'          # database_user
db_password = "thrymr%40123"  # password thyrmr@123 (@=%40)
db_host = 'localhost'         # by default
db_port = '5432'              # by default  
db_name = 'graduates'         #database_name

DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(DATABASE_URL)  
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db(): #This function provides a database session for the application and ensures that the session is properly closed.
    db = sessionLocal() 
    try:
        yield db
    finally:
        db.close()

#1. Engine: The `engine` connects your application to the PostgreSQL database.
#2. Session: The `sessionLocal` provides sessions that interact with the database through the `engine`.
                 #Each session can be used to query and modify the database.
#3. Base: The `Base` class is the foundation for your ORM models, which represent database tables. 
              #It helps SQLAlchemy understand how your classes map to the database schema.
