from fastapi import FastAPI

app = FastAPI()

# =============== GET ===============
@app.get("/")
async def root():
    return {"message": "Hello World"}

# user id 為動態設計
@app.get("/users/{user_id}")
async def user(user_id):
    return {"message": f"Hi user {user_id}"}

# Query Parameter
fake_items_db = [{"Player1": "Stephen Curry"}, {"Player2": "Lebron James"}, {"Player3": "Kevin Durant"}]
@app.get("/items")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
# http://127.0.0.1:8000/items?skip=1&limit=1 -> 若在該 API 後面加上?可攜帶參數，參數就是 read_item 所夾帶的。此例子就只會顯示 [{"Player2":"Lebron James"}]

# =============== POST ===============
# use Form-data
from fastapi import Form
@app.post("/login")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}

# use JSON
from pydantic import BaseModel
class User(BaseModel):
    username: str
    password: str

@app.post("/login_json")
async def login_json(user: User):
    return {"username": user.username}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)