from fastapi import APIRouter
from ..controllers.Usuarios import listarUsuarios, cadastrarUsuario, atualizarUsuario, excluirUsuario

rotas = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"],
    responses={404: {"description": "Not Found"}},
)

@rotas.get('/', tags=['Usuarios'])
async def listar_usuarios(): 
    return await listarUsuarios()

@rotas.post('/{id_usuario}')
async def cadastrar_usuario(id_usuario):
    return await cadastrarUsuario(id_usuario)

@rotas.delete('/{id_usuario}')
async def excluir_usuario(id_usuario):
    return await excluirUsuario(id_usuario)

@rotas.put('/{id_usuario}')
async def atualizar_usuario(id_usuario):
    return await atualizarUsuario(id_usuario)

