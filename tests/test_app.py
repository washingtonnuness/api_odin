from http import HTTPStatus

from fastapi.testclient import TestClient

from server.app import app


# Função de test o que está sendo testado e o que precisa ser retornado caso ok
def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organização do teste)

    response = client.get('/usuarios')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Ola Mundo!'}
