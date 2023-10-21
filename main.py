from fastapi import FastAPI

from routes.index import user

app = FastAPI()

# @app.get("/")
# def hello():
#     return {"message" : "hello world"}


app.include_router(user)