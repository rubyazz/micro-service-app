# from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi import FastAPI

app = FastAPI(title="Microservice App")


@app.get("/users/")
def get_hello():
    return "Hello world!"


@app.post("/users/")
def init_users():
    return "initiation users"
