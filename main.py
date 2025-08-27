from fastapi import FastAPI
from routers import users, transfers

app = FastAPI()
app.include_router(users.router)
app.include_router(transfers.router)

app.state.db = dict()