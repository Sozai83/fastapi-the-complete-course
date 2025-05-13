from fastapi import FastAPI
import models
from database import engine

app = FastAPI()

# create everything from database.py file and models.py file to be able to create a new table
models.Base.metadata.create_all(bind=engine)