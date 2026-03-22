import flet as ft
import random

def main(page: ft.Page):
    # Базовые настройки страницы
    page.bgcolor = "#000000"
    page.theme_mode = ft.ThemeMode.DARK
    
    # Исправленные выравнивания (теперь через строки, так надежнее)
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    # Твои фразы
    phrases = ["ДА", "НЕТ", "РИСКНИ", "ПОЗЖЕ", "100%", "ЗАБУДЬ", "ТВОЙ ШАНС", "НЕ СТОИТ", "СКВИРТ"]

    # Главный текст
    res_text = ft.Text(
        value="KUNIGRAM",
        size=45,
        color="#A855F7",
        weight="bold",
    )

    def button_click(e):
        res_text.value = random.choice(phrases)
        page.update()

    # Кнопка (исправлено выравнивание внутри)
    btn = ft.Container(
        content=ft.Text("?", color="black", size=30, weight="bold"),
        width=100,
        height=100,
        bgcolor="#A855F7",
        border_radius=50,
        # Вместо ft.alignment.center используем просто Alignment(0,0) - это центр
        alignment=ft.Alignment(0, 0),
        on_click=button_click,
    )

    # Собираем интерфейс
    page.add(
        ft.Column(
            [
                res_text,
                ft.Container(height=50),
                btn,
            ],
            horizontal_alignment="center", # Тоже строкой для надежности
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
