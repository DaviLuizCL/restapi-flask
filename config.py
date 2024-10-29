import os


class DevConfig():

    MONGODB_SETTINGS = {
        'db': os.getenv('MONGODB_DB'),
        'host': os.getenv('MONGODB_HOST'),
        'port': os.getenv('MONGODB_PORT'),
        'username': os.getenv('MONGODB_USER'),
        'password': os.getenv('MONGODB_PASSWD')
    }


class MockConfig:
    MONGODB_SETTINGS = {
        'db': 'users',
        'host': 'mongomock://localhost',

    }
