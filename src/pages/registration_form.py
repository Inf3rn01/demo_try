import flet as ft
from src.database.database_operations import register

class RegistrationForm(ft.UserControl):
    def __init__(self, db_manager, navigate_to_login, navigate_to_main_window):
        super().__init__()
        self.db_manager = db_manager
        self.navigate_to_main_window = navigate_to_main_window
        self.navigate_to_login = navigate_to_login

    def build(self):
        self.usernameField = ft.TextField(label="Имя пользователя", on_change=self.validate)
        self.loginField = ft.TextField(label="Логин", on_change=self.validate)
        self.passwordField = ft.TextField(label="Пароль", password=True, on_change=self.validate)
        self.register_button = ft.ElevatedButton(text="Зарегистрироваться", on_click=self.register_clicked, disabled=True)
        return ft.Column(
            controls=[
                self.usernameField,
                self.loginField,
                self.passwordField,
                self.register_button,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def validate(self, e):
        self.register_button.disabled = not (self.usernameField and self.loginField.value and self.passwordField.value)
        self.update()
        
    def register_clicked(self, e):
        user = register(self.db_manager, self.usernameField.value, self.loginField.value ,self.passwordField.value)
        if user:
            self.navigate_to_main_window  # Переход на страницу логина после успешной регистрации
        else:
            print("Registration failed")