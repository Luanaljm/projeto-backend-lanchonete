from fastapi import FastAPI
import uvicorn
from app.database.db import engine, Base
from app.models import pedido, usuario 
from app.routes import pedido_routes, usuario_routes 

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Lanchonete Multicanal")

app.include_router(pedido_routes.router)
app.include_router(usuario_routes.router) 

@app.get("/")
def home():
    return {"status": "Online"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
