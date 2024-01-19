# from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi import FastAPI

app = FastAPI(title="Microservice App")


@app.get("/users/")
async def get_hello():
    return "Hello world!"
