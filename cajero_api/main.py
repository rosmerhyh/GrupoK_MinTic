from fastapi import FastAPI
from db.user_db import database_users
from fastapi import HTTPException
from db.user_db import UserInDB

app = FastAPI()

@app.get("/")    #GET / HTTP/1.1 (Cliente)
async def root():
    return {"message": "Hello fast API"}

@app.get("/users")    #GET / HTTP/1.1 (Cliente)
async def users():
    return {"message": database_users}

@app.get("/users/{username}")    #GET / HTTP/1.1 (Cliente)
async def get_user_username(username : str):
    if username in database_users:
        return {"message": database_users [username]}
    raise  HTTPException(status_code=404, detail="El usuario no existe") #{"message":"El usuario no existe"}

@app.post("/users/")
async def ceate_user(user : UserInDB):
    database_users[user.username] = user
    return user