from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return JSONResponse(
        status_code=200,
        content={
            "mensagem1": "Usando FastApi em um container Docker",
            "mensagem2": "Navegue pelas rotas da API através do '/docs' na frente da URL"
        },
    )


class Usuario(BaseModel):
    id: int
    nome: str
    email: str


base_de_dados = [
    Usuario(id=1, nome='Fábio da Silva Pedro', email='fabio.pedro@email.com'),
    Usuario(id=2, nome='Renata Almeida', email='r.almeida@email.com'),
    Usuario(id=3, nome='José Vitor', email='josevitor@email.com'),
    Usuario(id=4, nome='Rebeca Fonseca', email='rebeca_fonseca@email.com'),
    Usuario(id=5, nome='Nathália Soares', email='nathalia.s@email.com'),
    Usuario(id=6, nome='Rodrigo Pessoa', email='rodrigo.pessoa@email.com'),
]


@app.get("/usuarios")
async def get_users():
    return JSONResponse(
        status_code=200,
        content=jsonable_encoder(base_de_dados)
    )


@app.get("/usuarios/{id}")
async def get_user_by_id(value_id: int):
    for usuario in base_de_dados:
        if usuario.id == value_id:
            return JSONResponse(
                status_code=200,
                content=jsonable_encoder(usuario)
            )
    return JSONResponse(
        status_code=400,
        content={"Mensagem": f"Usuário não encontrado com este ID: {value_id}"}
    )


@app.post("/usuarios")
async def new_user(nome: Usuario):
    base_de_dados.append(nome)
    return JSONResponse(status_code=200, content=jsonable_encoder(nome))


@app.delete("/usuarios/{id}")
async def delete_user_by_id(value_id):
    item_remove = ''
    for x in range(len(base_de_dados)):
        for y in str(base_de_dados[x].id):
            if str(y) == str(value_id):
                item_remove = x

    if item_remove == '':
        return JSONResponse(
            status_code=400,
            content={
                "Mensagem": f"Usuário não encontrado com este ID: {value_id}"
            }
        )
    else:
        base_de_dados.pop(item_remove)
        return JSONResponse(
            status_code=200, content=f"Usuário ID: {value_id}, removido!"
        )


@app.put("/usuarios/{id}")
async def update_user_by_id(id: int, nome: str, email: str):
    id_update = ''
    for x in range(len(base_de_dados)):
        for y in str(base_de_dados[x].id):
            if str(y) == str(id):
                id_update = x

    if id_update == '':
        return JSONResponse(
            status_code=400,
            content={
                "Mensagem": f"Usuário não encontrado com este ID: {id}"
            }
        )
    else:
        result = Usuario(id=id, nome=nome, email=email)
        base_de_dados.pop(id_update)
        base_de_dados.insert(id_update, result)
        return JSONResponse(
            status_code=200, content=f"Usuário ID: {id}, atualizado!"
        )
