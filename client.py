import flet as ft
from database.database_manager import DBManager
from pages import LoginForm, RegistrationForm
from settings import DB_PATH

def main(page: ft.Page):
    db_manager = DBManager(DB_PATH)

    # Функция для перехода на страницу логина
    def go_to_login(e):
        page.go('/login')

    # Функция для перехода на страницу регистрации
    def go_to_registration(e):
        page.go('/registration')

    # Определяем маршруты
    def route_change(route):
        page.controls.clear()
        if page.route == '/registration':
            page.controls.append(RegistrationForm(db_manager, go_to_login=go_to_login))
        else:
            page.controls.append(LoginForm(db_manager, go_to_registration=go_to_registration))
        page.update()

    # Устанавливаем начальный маршрут
    page.on_route_change = route_change
    page.go('/login')

if __name__ == '__main__':
    ft.app(target=main)