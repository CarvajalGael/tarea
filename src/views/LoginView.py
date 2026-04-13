import flet as ft

def LoginView(page, auth:contrpoller):
    email_input = ft.TextField(label="Correo electronico", width=350, border_radius=10)
    pass_input = ft.TextField (label="Contraseña", password=True can_reveal_password=True, width=350, border_radius=10)
    
    def login_click(e):
        user, msg = auth_controller,login(email_input.value, pass_input.value)
        if user:
            page.session.set("user", user) #Guardamos sesion
        else:
            page.snack_bar = ft.SnackBar(ft.Text(msg))
            page.snack_bar.open = True
            page.update()
            
    return ft.view("/", [
        ft.AppBar(title=ft.Text("SIGE - Login"), )
    ])