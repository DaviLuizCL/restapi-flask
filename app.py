from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_mongoengine import MongoEngine
from mongoengine import NotUniqueError
from validate_docbr import CPF

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'users',
    'host': 'mongodb',
    'port': 27017,
    'username': 'admin',
    'password': 'admin'
}
_user_parser = reqparse.RequestParser()
_user_parser.add_argument('first_name',
                          type=str,
                          required=True,
                          help="This field cannot be blank")
_user_parser.add_argument('last_name',
                          type=str,
                          required=True,
                          help="This field cannot be blank")
_user_parser.add_argument('cpf',
                          type=str,
                          required=True,
                          help="This field cannot be blank")
_user_parser.add_argument('email',
                          type=str,
                          required=True,
                          help="This field cannot be blank")
_user_parser.add_argument('birth_date',
                          type=str,
                          required=True,
                          help="This field cannot be blank")

api = Api(app)
db = MongoEngine(app)
cpf = CPF()


class UserModel(db.Document):
    cpf = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True)
    first_name = db.StringField(max_length=50, required=True)
    last_name = db.StringField(max_length=50, required=True)
    birth_date = db.DateTimeField(required=True)


class Users(Resource):
    def get(self):
        return {'message': 'user1'}


class User(Resource):
    def post(self):
        data = _user_parser.parse_args()
        if not cpf.validate(data["cpf"]):
            return {"message": "CPF is invalid!"}, 400
        
        try:

            response = UserModel(**data).save()
            return {"message": f"user {response.id} successfully created!"}
        
        except NotUniqueError:
            return {"message": "CPF already exists in database"}, 400
    def get(self):
        return {'message': 'teste'}


api.add_resource(Users, '/users')
api.add_resource(User, '/user')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
