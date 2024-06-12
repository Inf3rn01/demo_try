import flet as ft
from database.database_operations import register


class RegistrationForm(ft.UserControl):
    def __init__(self, db_manager, go_to_login):
        super().__init__()
        self.db_manager = db_manager
        self.go_to_login = go_to_login
        
    def build(self):
        self.appbar = ft.AppBar(
            title=ft.Text("Регистрация"),
            leading=ft.IconButton(
                icon=ft.icons.ARROW_BACK,
                on_click=self.go_to_login
            )
        )
        self.nameField = ft.TextField(label="Имя")
        self.loginField = ft.TextField(label="Логин")
        self.passwordField = ft.TextField(label="Пароль", password=True)
        self.register_button = ft.ElevatedButton(text="Зарегистрироваться", on_click=self.register_clicked, disabled=True)
        return ft.Column(controls=[
            self.name,
            self.login,
            self.password,
            self.register_button
        ])

    def validate(self, e):
        if all([self.nameField, self.loginField.value, self.passwordField.value]):
            self.login_button.disabled = False
        else:
            self.login_button.disabled = True

    def register_clicked(self, e):
        success = register(self.db_manager, self.name.value, self.login.value, self.password.value)
        if success:
            print("Registration successful")
            # Здесь можно добавить переход на страницу логина или обновление интерфейса
        else:
            print("Registration failed")