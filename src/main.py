from base_config import auth_backend, fastapi_users
from fastapi import FastAPI
from schemas import UserCreate, UserRead

from operations.router import router as router_operation

app = FastAPI(title="Trading App")

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(router_operation)

# 6:27
