from fastapi import FastAPI, HTTPException, status

lista = [
    {"cpf": "12345678911", "nome": "imaginario"},
    {"cpf": "98765432199", "nome": "teste"}
]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Você está no começo"}

@app.get("/aniversario/{cpf}")
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
