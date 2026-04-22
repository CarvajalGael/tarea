import flet as ft

def main(page: ft.Page):
    page.title = "INICIO DE SESIÓN"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Datos correctos
    USUARIO_CORRECTO = "admin"
    CORREO_CORRECTO = "admin@dominio.com"
    CONTRA_CORRECTA = "1234"

    # Campos
    nombre = ft.TextField(
        label="Nombre de Usuario",
        width=300,
        prefix_icon=ft.Icons.PERSON
    )

    correo = ft.TextField(
        label="Correo electrónico",
        width=300,
        prefix_icon=ft.Icons.EMAIL
    )

    password = ft.TextField(
        label="Contraseña",
        width=300,
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK
    )

    # Función para mostrar panel
    def mostrar_panel():
        page.clean()

        page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
                ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Explorar"),
                ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Perfil"),
            ]
        )

        page.add(
            ft.Column(
                [
                    ft.Text("Panel Principal", size=35, weight=ft.FontWeight.BOLD),
                    ft.Text("Bienvenido al sistema", size=20),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

    # Login
    def iniciar_sesion(e):
        if (
            nombre.value == USUARIO_CORRECTO and
            correo.value == CORREO_CORRECTO and
            password.value == CONTRA_CORRECTA
        ):
            mostrar_panel()
        else:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Usuario, correo o contraseña incorrectos ❌")
            )
            page.snack_bar.open = True
            page.update()

    boton_login = ft.ElevatedButton(
        "Iniciar Sesión",
        width=300,
        on_click=iniciar_sesion
    )

    boton_texto = ft.TextButton(
        "¿Olvidaste tu contraseña?"
    )

    # UI con mejor diseño
    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text("INICIAR SESIÓN", size=30, weight=ft.FontWeight.BOLD),
                        nombre,
                        correo,
                        password,
                        boton_login,
                        boton_texto
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                padding=20,
                width=350
            )
        )
    )

ft.app(target=main)
