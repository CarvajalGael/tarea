import flet as ft

def RegistroView(page, auth_controller):

    nombre_input = ft.TextField(
        label="Nombre",
        hint_text="Ingresa tu nombre",
        width=350,
        border=ft.InputBorder.NONE,
        icon=ft.Icons.PERSON,
    )

    apellido_input = ft.TextField(
        label="Apellido",
        hint_text="Ingresa tu apellido",
        width=350,
        border=ft.InputBorder.NONE,
        icon=ft.Icons.BADGE,
    )

    email_input = ft.TextField(
        label="Correo",
        hint_text="Ingresa tu correo",
        width=350,
        border=ft.InputBorder.NONE,
        icon=ft.Icons.EMAIL,
    )

    password_input = ft.TextField(
        label="Contraseña",
        hint_text="Ingresa tu contraseña",
        width=350,
        password=True,
        can_reveal_password=True,
        border=ft.InputBorder.NONE,
        icon=ft.Icons.LOCK,
    )

    telefono_input = ft.TextField(
        label="Teléfono",
        hint_text="Ingresa tu teléfono",
        width=350,
        border=ft.InputBorder.NONE,
        icon=ft.Icons.PHONE,
    )

    foto_input = ft.TextField(
        label="Foto de perfil",
        hint_text="Ruta o URL de la imagen",
        width=350,
        border=ft.InputBorder.NONE,
        icon=ft.Icons.IMAGE,
    )

    def cerrar_dialogo(e):
        dialogo.open = False
        page.update()

    def validar_campos():
        return (
            nombre_input.value
            and apellido_input.value
            and email_input.value
            and password_input.value
        )

    def registrar_usuario(e):
        if not validar_campos():
            page.snack_bar = ft.SnackBar(
                ft.Text("Completa los campos obligatorios")
            )
            page.snack_bar.open = True
            page.update()
            return

        success, mensaje = auth_controller.register(
    nombre_input.value,
    apellido_input.value,
    email_input.value,
    password_input.value
)

        if success:
            page.snack_bar = ft.SnackBar(
                ft.Text(mensaje)
            )
            page.snack_bar.open = True
            page.update()
            page.go("/")
        else:
            dialogo.content = ft.Text(mensaje)
            dialogo.open = True
            page.dialog = dialogo
            page.update()

    dialogo = ft.AlertDialog(
        title=ft.Text("Error de registro"),
        content=ft.Text(""),
        actions=[
            ft.TextButton("Cerrar", on_click=cerrar_dialogo)
        ]
    )

    boton_registrar = ft.ElevatedButton(
        "Registrar usuario",
        width=350,
        bgcolor=ft.Colors.BLACK,
        color=ft.Colors.WHITE,
        on_click=registrar_usuario
    )

    return ft.View(
        route="/registro",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Column(
                controls=[
                    ft.Text(
                        "Crear cuenta",
                        size=30,
                        weight=ft.FontWeight.BOLD
                    ),
                    nombre_input,
                    apellido_input,
                    email_input,
                    password_input,
                    telefono_input,
                    foto_input,
                    boton_registrar,
                    ft.TextButton(
                        "Volver al login",
                        on_click=lambda e: page.go("/")
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15
            )
        ]
    )
