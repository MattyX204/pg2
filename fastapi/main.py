from fastapi import FastAPI, HTTPexception
from models import Flight


app = FastAPI()


@app.get("/",tags=["Root"])
def read_root():
    return {"message":"Welcomento the FLight API"}

@app.get("/flights",response_model=list[Flight],tags=["Flights"])
def_read_flights():
