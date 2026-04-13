import flet as ft

def LoginView(page, auth:contrpoller):
    email_inputt = ft.TextField(label="Correo electronico", width=350, border_radius=10)
    pass_input = ft.TextField (label="Contraseña", password=True can_reveal_password=True, width=350, border_radius=10)
    
    def login_click(e):
        user, msg = au