from fastapi import FastAPI
from Modelo import gerar_resumo

app = FastAPI()

@app.post("/resumir/")
def resumir_texto(texto: str):
    resumo = gerar_resumo(texto)
    return {"resumo": resumo}

# Para rodar a API, execute:
# uvicorn api:app --reload
