import flet as ft
import random

def main(page: ft.Page):
    # Настройки страницы
    page.bgcolor = "#000000"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Цвета с аватарки
    NEON_PURPLE = "#A855F7"
    
    # Текст ответа
    res_text = ft.Text(
        value="TAP",
        size=60,
        color=NEON_PURPLE,
        weight="bold",
        opacity=1,
        animate_opacity=200,
    )

    # Список фраз
    quotes = ["ДА", "НЕТ", "РИСКНИ", "ПОЗЖЕ", "100%", "ЗАБУДЬ", "ТВОЙ ШАНС", "НЕ СТОИТ", "СКВИРТ"]

    def shake_oracle(e):
        # Меняем текст и анимируем прозрачность (быстрое мигание)
        res_text.opacity = 0
        page.update()
        
        res_text.value = random.choice(quotes)
        res_text.opacity = 1
        page.update()

    # Основная кнопка (просто круг со свечением)
    btn = ft.Container(
        content=ft.Icon(ft.icons.BOLT, color="#000000", size=40),
        width=120,
        height=120,
        bgcolor=NEON_PURPLE,
        border_radius=60,
        alignment=ft.alignment.center,
        on_click=shake_oracle,
        shadow=ft.BoxShadow(
            blur_radius=40,
            color=NEON_PURPLE,
            spread_radius=-5,
        ),
    )

    # Собираем экран
    page.add(
        ft.Column(
            [
                ft.Container(
                    content=res_text,
                    height=200,
                    alignment=ft.alignment.center,
                ),
                ft.Container(height=50),
                btn,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
