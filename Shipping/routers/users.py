from fastapi import APIRouter

router = APIRouter()

# get user id
@router.get("/{user_id}", summary="getUserId", description="Get User ID.")
async def getUser(user_id: int):
    return {"message": f"Hello user {user_id}"}

# create user name
@router.post("/{username}", summary="createUser", description="Create a user.")
async def createUser(username):
    return {"message": f"Hello user {username}"} 