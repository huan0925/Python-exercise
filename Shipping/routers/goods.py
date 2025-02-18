from fastapi import APIRouter

router = APIRouter()

# get product id
@router.get("/{product_id}")
async def getProductId(product_id):
    return {"message": f"Product id: {product_id}"}

# insert product
@router.post("/{product_name}")
async def insertProduct(product_name):
    return {"message": f"New Product: {product_name}"}