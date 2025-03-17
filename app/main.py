from fastapi import FastAPI, Depends, HTTPException, Header # type: ignore
import os
from .services import fetch_user, fetch_products

app = FastAPI()

API_KEY = os.getenv("API_KEY", "default-secret-key")

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")

@app.get("/bff/user/{user_id}")
async def get_user_dashboard(user_id: int, _: str = Depends(verify_api_key)):
    user = await fetch_user(user_id)
    products = await fetch_products()

    return {
        "user": user.dict(),
        "recommended_products": [product.dict() for product in products]
    }
