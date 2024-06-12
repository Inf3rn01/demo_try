import flet as ft
from database.database_operations import check_login

class LoginForm(ft.UserControl):
    def __init__(self, db_manager, go_to_registration):
        super().__init__()
        self.db_manager = db_manager
        self.go_to_registration = go_to_registration

    def build(self):
        self.appbar = ft.AppBar(
            title=ft.Text("Вход"),
        )
        self.loginField = ft.TextField(label="Логин")
        self.passwordField = ft.TextField(label="Пароль", password=True)
        self.login_button = ft.ElevatedButton(text="Войти", on_click=self.login_clicked, disabled=True)
        self.register_button = ft.ElevatedButton(text="Зарегистрироваться", on_click=self.register_clicked)
        return ft.Column(controls=[
            self.login,
            self.password,
            self.login_button,
            self.register_button
        ])

    def validate(self, e):
        if all([self.loginField.value, self.passwordField.value]):
            self.login_button.disabled = False
        else:
            self.login_button.disabled = True

    def login_clicked(self, e):
        user = check_login(self.db_manager, self.login.value, self.password.value)
        if user:
            print(f"User ID: {user['id']}, Name: {user['name']}, Post ID: {user['post_id']}")
            # Здесь можно добавить переход на следующую страницу или обновление интерфейса
        else:
            print("Login failed")

    def register_clicked(self, e):
        self.go_to_registration(e)
