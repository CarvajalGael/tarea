import flet as ft
from src.controllers.userController import AuthController
from src.controllers.TareaController import TareaController
from src.views.LoginView import LoginView
from src.views.dashboard import DashboardView

def main(page: ft.Page):
    auth_controller = AuthController()
    task_ctrl = TareaController()

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(LoginView(page, auth_controller))
        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))
        page.update()

    page.on_route_change = route_change
    page.go("/")


if __name__ == "__main__":
    ft.app(target=main)