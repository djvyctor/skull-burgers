from pydantic import BaseModel
from typing import Optional

# Schema para criar e receber dados
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    image_url: Optional[str] = None
    category: str  

# Schema para leitura
class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True