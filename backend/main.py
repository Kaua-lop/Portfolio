from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuração para permitir que o frontend acesse a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite acesso de qualquer origem (para testes)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dados fictícios dos projetos (pode puxar do GitHub futuramente)
@app.get("/api/projects")
async def get_projects():
    return [
        {"name": "Snake_Game", "description": "é um jogo de cobrinha desenvolvido em Python utilizando a biblioteca Pygame. O objetivo do jogo é controlar a cobrinha para pegar as maçãs e crescer.", "url": "https://github.com/Kaua-lop/Skane_Game"},
        {"name": "Jogo-da-forca", "description": "Um simples jogo da forca implementado em Python, com temas variados como desenhos, filmes, frutas e jogos.", "url": "https://github.com/Kaua-lop/jogo-da-forca-python"},
    ]
