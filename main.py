# from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi import FastAPI

app = FastAPI(title="Microservice App")


@app.get("/users/")
async def get_hello():
    return "Hello world!"


@app.post("/users/")
async def init_users():
    return "initiation users"


@app.delete("users/{id}")
async def delete_users():
    return "deleting users"
