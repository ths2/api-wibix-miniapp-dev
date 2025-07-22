# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuração CORS: Inicialmente, permita tudo para facilitar o teste.
# APÓS a implantação do frontend, você DEVE substituir '*' pelo URL do seu frontend S3.
# Ex: origins = ["http://your-frontend-bucket-name.s3-website-sa-east-1.amazonaws.com"]
origins = ["*"] # Mude isso para o URL do seu frontend após a implantação!

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI on AWS ECS!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

