# встановлення самого фреймворку + сервер(тільки для розробки)
# py -m pip install fastapi uvicorn

# розширена версія з інструментами для валідації з json тощо
# py -m pip install "fastapi[all]"

from fastapi import FastAPI, status

app = FastAPI()

@app.get('/')
def index():
    """
    This endpoint sends congratulations for install FastAPI
    """
    return {"message": "FastAPI installation&run complete!"}

@app.post('/user', status_code=status.HTTP_201_CREATED)
def make_account():
    return{"status":201, "mesage":"Created", "user":{"username": "user1", 'created_at':'2026-04-24 19:05:1231'}}

@app.get('/user/{id}')
def info(id:str):
    return {"user_id": id}