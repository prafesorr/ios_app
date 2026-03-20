import flet as ft

def main(page: ft.Page):
    page.title = "Мое приложение"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    text = ft.Text("Счётчик: 0", size=30)

    def button_click(e):
        count = int(text.value.split(": ")[1])
        text.value = f"Счётчик: {count + 1}"
        page.update()

    page.add(
        text,
        ft.ElevatedButton("Нажми меня!", on_click=button_click)
    )

ft.run(main)
