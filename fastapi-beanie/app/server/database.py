from beanie import init_beanie
import motor.motor_asyncio
from app.server.models.product_review import ProductReview
import asyncio

mongo_url='mongodb://host.docker.internal'

async def init_db():
    try:
        client = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
        client.get_io_loop = asyncio.get_running_loop
        await init_beanie(database=client.db_name, document_models=[ProductReview])

        return True
    except Exception as err:
        
        return False