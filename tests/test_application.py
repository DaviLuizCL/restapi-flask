import pytest
from application import create_app


class TestApplication():

    @pytest.fixture
    def client(self):
        app = create_app('config.MockConfig')
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
        assert response.json[0]["first_name"] == "Davi"
        assert response.json[0]["last_name"] == "Lima"
        assert response.json[0]["cpf"] == "751.457.960-56"
        assert response.json[0]["email"] == "davizinoftapioca@gmail.com"
        birth_date = response.json[0]["birth_date"]["$date"]
        assert birth_date == "2002-07-31T00:00:00Z"
