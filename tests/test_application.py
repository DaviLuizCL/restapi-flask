import pytest
from application import create_app
from config import MockConfig  # Adicione a importação da configuração


class TestApplication:

    @pytest.fixture
    def client(self):
        app = create_app(MockConfig)  # Use a classe diretamente
        return app.test_client()

    @pytest.fixture
    def valid_user(self):
        return {
            "first_name": "Davi",
            "last_name": "Lima",
            "cpf": "751.457.960-56",
            "email": "davizinoftapioca@gmail.com",
            "birth_date": "2002-07-31"
        }

    @pytest.fixture
    def invalid_user(self):
        return {
            "first_name": "Davi",
            "last_name": "Lima",
            "cpf": "751.457.960-57",
            "email": "davizinoftapioca@gmail.com",
            "birth_date": "2002-07-31"
        }

    def test_get_users(self, client):
        response = client.get('/users')
        assert response.status_code == 200

    def test_post_user(self, client, valid_user, invalid_user):
        response = client.post('/user', json=valid_user)
        assert response.status_code == 200
        assert b"successfully" in response.data

        response = client.post('/user', json=invalid_user)
        assert response.status_code == 400
        assert b"invalid" in response.data

    def test_get_user(self, client, valid_user):
        response = client.get(f'/user/{valid_user["cpf"]}')
        assert response.status_code == 200
        user_data = response.get_json()[0]
        assert user_data["first_name"] == "Davi"
        assert user_data["last_name"] == "Lima"
        assert user_data["cpf"] == "751.457.960-56"
        assert user_data["email"] == "davizinoftapioca@gmail.com"
        birth_date = user_data["birth_date"]["$date"]
        assert birth_date == "2002-07-31T00:00:00Z"
