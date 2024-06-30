from beanie import Document

from pydantic import BaseModel

from datetime import datetime

from typing import Optional

class ProductReview(Document):
    name: str
    title: str
    rating: float
    review: str
    date: datetime=datetime.now()

    class Settings:
        name = "product_collection"
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Saad Abdur Razzaq",
                "title": "MacBook Air M2",
                "rating": 5.0,
                "review": "Best Laptop in the world",
                "date": datetime.now()
            }
        }
    
class UpdateProductReview(BaseModel):
    name: str
    title: str
    rating: float
    review: str
    date: datetime=datetime.now()

    class Config:
        schema_extra = {
            "example": {
                "name": "Taha Abdur Razzaq",
                "title": "HP Victus 16",
                "rating": 5.0,
                "review": "Worst Laptop in the world",
                "date": datetime.now()
            }
        }