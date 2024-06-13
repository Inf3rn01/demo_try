import flet as ft
from src.database.database_operations import check_login

class LoginForm(ft.UserControl):
    def __init__(self, db_manager, navigate_to_registration, navigate_to_main_window):
        super().__init__()
        self.db_manager = db_manager
        self.navigate_to_registration = navigate_to_registration
        self.navigate_to_main_window = navigate_to_main_window

    def build(self):
        self.loginField = ft.TextField(label="Логин", on_change=self.validate)
        self.passwordField = ft.TextField(label="Пароль", password=True, on_change=self.validate)
        self.login_button = ft.ElevatedButton(text="Войти", on_click=self.login_clicked, disabled=True)
        self.register_button = ft.ElevatedButton(text="Зарегистрироваться", on_click=lambda _: self.navigate_to_registration())

        return ft.Column(
            controls=[
                self.loginField,
                self.passwordField,
                self.login_button,
                self.register_button
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def validate(self, e):
        self.login_button.disabled = not (self.loginField.value and self.passwordField.value)
        self.update()

    def login_clicked(self, e):
        user = check_login(self.db_manager, self.loginField.value, self.passwordField.value)
        if user:
            print(f"User ID: {user['id']}")
            self.navigate_to_main_window()  # Переход на главное окно
        else:
            print("Login failed")
