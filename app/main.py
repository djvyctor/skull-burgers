from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from app.schemas import Product, ProductBase # Nossos schemas

app = FastAPI(
    title="Skull Burgers API",
    description="API do cardapio do Skull Burgers",
    version="1.0.0"
)

# Config do cors
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Banco de bosta, reseta ao reiniciar o lixo que chamo de servidor
fake_db = [
    {
        "id": 1,
        "name": "Sans Burguer",
        "description": "Um hambúrguer preguiçoso com muito queijo e ketchup.",
        "price": 25.0,
        "category": "Lanches",
        "image_url": "http://img.com/sans.png"
    },
    {
        "id": 2,
        "name": "Papyrus Spaghetti",
        "description": "O grande prato do chefe! (Não é hambúrguer, mas é massa).",
        "price": 20.0,
        "category": "Pratos",
        "image_url": "http://img.com/papyrus.png"
    },
]

# Lista da merda do cardapio
# response_model=List[Product] diz para o FastAPI formatar a saída como uma lista do nosso schema
@app.get("/products", response_model=List[Product])
def get_products():
    return fake_db

#Busca produto especifico
@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    # Vai procurar pra mim na lista, simulando a bosta do query
    product = next((item for item in fake_db if item["id"] == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Item não emcontrato GARAI...") # Joga o pc fora man...
    return product
    
# Cria um novo produto
@app.post("/products", response_model=Product, status_code=201)
def create_product(product: ProductBase):
    # Logica q gera ID automatico
    new_id = len(fake_db) + 1
    # Transforma o schema em dicionario e adiciona o ID (DOENÇA)
    new_product_dict = product.model_dump()
    new_product_dict["id"] = new_id

    fake_db.append(new_product_dict)
    return new_product_dict # Se não funcionar, faz o L