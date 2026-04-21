import flet as ft

def LoginView(page: ft.Page):

    USUARIO_CORRECTO = "admin"
    CORREO_CORRECTO = "admin@dominio.com"
    CONTRA_CORRECTA = "1234"

    nombre = ft.TextField(label="Nombre de Usuario", width=300)
    correo = ft.TextField(label="Correo electrónico", width=300)
    password = ft.TextField(label="Contraseña", password=True, width=300)

    def iniciar_sesion(e):
        if (
            nombre.value == USUARIO_CORRECTO
            and correo.value == CORREO_CORRECTO
            and password.value == CONTRA_CORRECTA
        ):
            page.go("/dashboard") 
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Datos incorrectos"))
            page.snack_bar.open = True
            page.update()

    return ft.View(
        route="/",
        controls=[
            ft.Text("INICIAR SESION", size=35),nombre, correo,password, ft.ElevatedButton("Iniciar Sesión", on_click=iniciar_sesion),],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )