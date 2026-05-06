from models.UserModel import UsuarioModel
from models.schemasModel import UsuariosSchema
from pydantic import ValidationError


class AuthController:
    def __init__(self):
        self.model = UsuarioModel()

    def registrar_usuario(
        self,
        nombre,
        apellido,
        email,
        password,
        telefono=None,
        foto_perfil=None
    ):
        try:
            nuevo_usuario = UsuariosSchema(
                nombre=nombre,
                apellido=apellido,
                email=email,
                password=password,
                telefono=telefono,
                foto=foto_perfil
            )

            success = self.model.registrar(nuevo_usuario)

            if success:
                return True, "Usuario creado correctamente"

            return False, "No se pudo registrar el usuario"

        except ValidationError as e:
            return False, e.errors()[0]["msg"]
