import pytest

from app import app, calcular


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()

def test_adicao():
    assert calcular("1", 2, 3) == 5


def test_subtracao():
    assert calcular("2", 5, 3) == 2


def test_multiplicacao():
    assert calcular("3", 4, 3) == 12


def test_divisao():
    assert calcular("4", 10, 4) == 2.5


def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        calcular("4", 1, 0)

def test_pagina_inicial(client):
    resposta = client.get("/")
    assert resposta.status_code == 200


def test_soma_pela_pagina(client):
    resposta = client.post("/", data={"num1": "10", "num2": "2,5", "opcao": "1"})
    assert b"12.5" in resposta.data


def test_divisao_por_zero_pela_pagina(client):
    resposta = client.post("/", data={"num1": "1", "num2": "0", "opcao": "4"})
    assert b"dividir por zero" in resposta.data


def test_entrada_invalida_pela_pagina(client):
    resposta = client.post("/", data={"num1": "abc", "num2": "2", "opcao": "1"})
    assert b"Entrada inv" in resposta.data