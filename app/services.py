import httpx # type: ignore
from .models import UserProfile, Product
import os

USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://user-service/api/users")
PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL", "http://product-service/api/products")

async def fetch_user(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{USER_SERVICE_URL}/{user_id}")
        return UserProfile(**response.json())

async def fetch_products():
    async with httpx.AsyncClient() as client:
        response = await client.get(PRODUCT_SERVICE_URL)
        return [Product(**item) for item in response.json()]
