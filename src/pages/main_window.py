import flet as ft

def MainWindow(page: ft.Page):
    page.title = "Главное окно"
    page.controls.clear()
    page.appbar = ft.AppBar(
        title=ft.Text("Главное окно"),
        center_title=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
    )
    page.add(ft.Text("Добро пожаловать в главное окно!"))
    page.update()  # Обновляем страницу для отображения изменений