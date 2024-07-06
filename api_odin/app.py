from http import HTTPStatus

from fastapi import FastAPI
from api_odin.schemas import Message, UserSchema, UserPublic

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}

#EndPoint recebe o modelo UserSchema para validação dos dados
#Responde após validar os dados na classe UserSchema com modelo UserPublic sem a senha do usuário
@app.post('/users/', response_model=UserPublic)
def create_user(user: UserSchema):
    return user