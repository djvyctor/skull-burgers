from fastapi import FastAPI

app = FastAPI(
    title="Skull Burgers API",
    description="API para o sistema de pedidos da lanchonete mais osso-duro da cidade.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "message": "Bem-vindo ao Skull Burgers",
        "status": "A cozinha está aberta.",
        "quote": "Do you wanna have a bad time? Peça nosso Mega Burger!"
    }