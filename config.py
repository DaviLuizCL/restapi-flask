import os


class DevConfig():

    MONGODB_SETTINGS = {
        'db': os.getenv('MONGODB_DB'),
        'host': os.getenv('MONGODB_HOST'),
        'port': os.getenv('MONGODB_PORT'),
        'username': os.getenv('MONGODB_USER'),
        'password': os.getenv('MONGODB_PASSWD')
    }


class ProdConfig:
    MONGODB_USER = os.getenv('MONGODB_USER')
    MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
    MONGODB_HOST = os.getenv('MONGODB_HOST')
    MONGODB_DB = os.getenv('MONGODB_DB')
    MONGO_APP_NAME = os.getenv('MONGO_APP_NAME')
    MONGO_URL = os.getenv('MONGO_URL')
    MONGODB_SETTINGS = {
        'host': "mongodb+srv://627daviluiz:%s@comunidadedevops-python.xb0cw.mongodb.net/?retryWrites=true&w=majority&tls=true&tlsAllowInvalidCertificates=true&appName=comunidadedevops-python" %(MONGODB_PASSWORD)

    }


class MockConfig:
    MONGODB_SETTINGS = {
        'db': 'users',
        'host': 'mongomock://localhost',

    }
