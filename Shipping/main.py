from fastapi import FastAPI
from routers.users import router as user_router
from routers.goods import router as product_router

app = FastAPI()
app.include_router(user_router, prefix='/user')
app.include_router(product_router, prefix='/product')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)