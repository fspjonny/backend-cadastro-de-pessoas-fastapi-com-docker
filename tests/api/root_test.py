from fastapi.testclient import TestClient


def test_get_initial_page_of_app(call_client: TestClient):
    response = call_client.get("/")
    body = response.json()

    assert response.status_code == 200
    assert body["mensagem1"] == "Usando FastApi em um container Docker"


def test_get_the_list_of_all_users(list_client: TestClient):
    response = list_client.get("/usuarios")

    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "nome": "Fábio da Silva Pedro",
            "email": "fabio.pedro@email.com"
        },
        {
            "id": 2,
            "nome": "Renata Almeida",
            "email": "r.almeida@email.com"
        },
        {
            "id": 3,
            "nome": "José Vitor",
            "email": "josevitor@email.com"
        },
        {
            "id": 4,
            "nome": "Rebeca Fonseca",
            "email": "rebeca_fonseca@email.com"
        },
        {
            "id": 5,
            "nome": "Nathália Soares",
            "email": "nathalia.s@email.com"
        },
        {
            "id": 6,
            "nome": "Rodrigo Pessoa",
            "email": "rodrigo.pessoa@email.com"
        }
    ]


def test_get_the_user_by_id(list_user_by_id: TestClient):
    response = list_user_by_id.get("/usuarios/{id}?value_id=1")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "nome": "Fábio da Silva Pedro",
        "email": "fabio.pedro@email.com"
    }


def test_create_new_user(creating_new_user: TestClient):
    data = {"id": 10, "nome": "Fulano", "email": "fulano@email.com"}
    response = creating_new_user.post("/usuarios", json=data)

    assert response.status_code == 200
    assert response.json() == {
        "id": 10,
        "nome": "Fulano",
        "email": "fulano@email.com"
    }


def test_edit_data_user(edit_user: TestClient):
    response = edit_user.put(
        "/usuarios/1",
        params={
            "id": 1,
            "nome": "Fábio",
            "email": "fabio@email.com"
        })
    body = response.json()

    assert response.status_code == 200
    assert body == "Usuário ID: 1, atualizado!"


def test_delete_user(delete_user: TestClient):
    response = delete_user.delete("/usuarios/{id}?value_id=1")
    body = response.json()

    assert response.status_code == 200
    assert body == "Usuário ID: 1, removido!"


# Testes para resultados negativos tratados

def test_fail_user_not_exist(user_not_id: TestClient):
    response = user_not_id.get("/usuarios/{id}?value_id=0")
    body = response.json()

    assert response.status_code == 400
    assert body["Mensagem"] == "Usuário não encontrado com este ID: 0"


def test_error_404_fail_obtain_user_list_url_error(url_error_list_client: TestClient):
    response = url_error_list_client.get("/usuario")
    body = response.json()

    assert response.status_code == 404
    assert body["detail"] == "Not Found"


def test_error_404_fail_create_new_user_url_error(fail_new_user: TestClient):
    data = {"id": 10, "nome": "Fulano", "email": "fulano@email.com"}
    response = fail_new_user.post("/usuario", json=data)

    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


def test_fail_edit_user_not_found(edit_user_fail: TestClient):
    response = edit_user_fail.put(
        "/usuarios/0",
        params={
            "id": 0,
            "nome": "Fábio",
            "email": "fabio@email.com"
        })
    body = response.json()

    assert response.status_code == 400
    assert body["Mensagem"] == "Usuário não encontrado com este ID: 0"


def test_fail_delete_user_not_found(delete_user_fail: TestClient):
    response = delete_user_fail.delete("/usuarios/{id}?value_id=0")
    body = response.json()

    assert response.status_code == 400
    assert body["Mensagem"] == "Usuário não encontrado com este ID: 0"
