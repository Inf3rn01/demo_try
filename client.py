import flet as ft
from src.database.database_manager import DBManager
from src.pages.login_form import LoginForm
from src.pages.registration_form import RegistrationForm
from settings import DB_PATH
from src.pages.main_window import MainWindow


def main(page: ft.Page):
    db_manager = DBManager(DB_PATH)

    def navigate_to_main_window():
        MainWindow(page)  # Переходим на главное окно

    def show_login_page():
        page.controls.clear()  # Очищаем текущие элементы страницы
        page.appbar = ft.AppBar(
            title=ft.Text("Логин"),
            center_title=True,
            bgcolor=ft.colors.SURFACE_VARIANT,
        )
        login_form = LoginForm(db_manager, show_registration_page, navigate_to_main_window)
        page.add(login_form)  # Добавляем форму логина на страницу
        page.update()  # Обновляем страницу для отображения изменений

    def show_registration_page():
        page.controls.clear()  # Очищаем текущие элементы страницы
        page.appbar = ft.AppBar(
            title=ft.Text("Регистрация"),
            center_title=True,
            bgcolor=ft.colors.SURFACE_VARIANT,
            leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: show_login_page())  # Кнопка для возврата
        )
        registration_form = RegistrationForm(db_manager, show_login_page, navigate_to_main_window)
        page.add(registration_form)  # Добавляем форму регистрации на страницу
        page.update()  # Обновляем страницу для отображения изменений

    show_login_page()  # Начальная загрузка страницы логина

ft.app(target=main)