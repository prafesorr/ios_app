import flet as ft
import random
import asyncio

async def main(page: ft.Page):
    # Базовые настройки для iOS
    page.title = "KUNIGRAM"
    page.bgcolor = "#000000"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 50

    # Фразы
    phrases = [
        "ДА", "НЕТ", "РИСКНИ", "ПОЗЖЕ", 
        "100%", "ЗАБУДЬ", "ТВОЙ ШАНС", "НЕ СТОИТ", "СКВИРТ"
    ]

    # Текст ответа (Фиолетовый как на аве)
    result_text = ft.Text(
        value="УЗНАЙ",
        size=55,
        color="#A855F7",
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    # Функция обработки нажатия
    async def shake(e):
        # Эффект мигания для живости
        result_text.opacity = 0
        await page.update_async()
        await asyncio.sleep(0.1)
        
        result_text.value = random.choice(phrases)
        result_text.opacity = 1
        await page.update_async()

    # Кнопка-молния (черная на фиолетовом фоне)
    btn = ft.Container(
        content=ft.Icon(ft.icons.BOLT, color="black", size=40),
        width=100,
        height=100,
        bgcolor="#A855F7",
        border_radius=50,
        on_click=shake,
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(
            blur_radius=30,
            color="#A855F7",
            spread_radius=-5,
        ),
    )

    # Собираем экран
    await page.add_async(
        ft.Column(
            [
                ft.Container(
                    content=result_text,
                    height=250,
                    alignment=ft.alignment.center,
                ),
                ft.Container(height=40),
                btn,
                ft.Container(height=20),
                ft.Text("ORACLE BY KUNIGRAM", size=10, color="#333333"),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

# Запуск в асинхронном режиме (важно для iOS)
if __name__ == "__main__":
    ft.app(target=main)
