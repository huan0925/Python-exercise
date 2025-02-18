from fastapi import APIRouter

router = APIRouter()

# get user id
@router.get("/{user_id}")
async def getUser(user_id: int):
    return {"message": f"Hello user {user_id}"}

# create user name
@router.post("/{username}")
async def createUser(username):
    return {"message": f"Hello user {username}"}