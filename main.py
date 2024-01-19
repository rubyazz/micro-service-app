# from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Microservice App")


@app.get("/users/")
async def get_hello():
    return "Hello world!"


@app.post("/users/")
async def init_users():
    return "initiation users"


class Users(BaseModel):
    pass


class Role(BaseModel):
    pass
