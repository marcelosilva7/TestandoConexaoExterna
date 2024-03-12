from fastapi import FastAPI, Request, Response, status, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

import os

allowed_ip = os.getenv("IP_PERMITIDO")

class OnlyOneIPMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, allowed_ip: str):
        super().__init__(app)
        self.allowed_ip = allowed_ip

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        if client_ip == self.allowed_ip:
            return await call_next(request)
        return Response(content="Acesso negado.", status_code=status.HTTP_403_FORBIDDEN)



lista = [

    {"cpf": "12345678911", "nome": "rodolfo", "nomemae": "maria", "nascimento": "10/10/2001"},
    {"cpf": "98765432199", "nome": "joao", "nomemae": "joaquina", "nascimento": "09/09/2002"}

]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Você está no começo"}

@app.get("/cpf/{cpf}")
def listar_cpf(cpf: str):
    cpf_achado = None  # Inicializa cpf_achado antes do loop
    for item in lista:
        if item["cpf"] == cpf:
            cpf_achado = item
            break

    if cpf_achado is None:  # Verifica se cpf_achado ainda é None
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='CPF não encontrado')

    return cpf_achado
