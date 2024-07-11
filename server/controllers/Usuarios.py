async def listarUsuarios():
    return [{"usuario": "Alejandro"}, {"usuario": "Washington"}]

async def cadastrarUsuario(id_usuario):
    return f"Usuario cadastrado com sucesso! Id: {id_usuario}"

async def excluirUsuario(id_usuario):
    return f"Usuario excluido com sucesso! Id: {id_usuario}"

async def atualizarUsuario(id_usuario):
    return f"Usuario atualizado com sucesso! Id: {id_usuario}"