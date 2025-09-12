from fastapi import APIRouter

shop = APIRouter()

@shop.get("/shop/food")
async def shop_food():
    return {"shop": "food"}

@shop.get("/shop/drink")
async def shop_drink():
    return {"shop": "drink"}