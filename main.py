import flet as ft
import random
import time

def main(page: ft.Page):
    # Настройки страницы в стиле твоей аватарки
    page.title = "Kunigram Oracle"
    page.bgcolor = "#000000"  # Глубокий черный
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 390
    page.window_height = 844

    # Цвета с твоей аватарки
    PURPLE = "#8B5CF6"  # Яркий фиолетовый
    DARK_PURPLE = "#2E1065"

    # Список ответов
    answers = [
        "ДА", "НЕТ", "РИСКНИ", "ПОЗЖЕ", 
        "100%", "ЗАБУДЬ", "ТВОЙ ШАНС", "НЕ СТОИТ"
    ]

    # Текстовое поле для ответа
    answer_text = ft.Text(
        value="ЖМИ",
        size=50,
        color=ft.colors.WHITE,
        weight=ft.FontWeight.BOLD,
        italic=True,
        animate_opacity=300,
    )

    # Красивая светящаяся кнопка
    def on_click(e):
        # Эффект "загрузки"
        answer_text.opacity = 0
        page.update()
        time.sleep(0.3)
        
        # Выбираем случайный ответ
        answer_text.value = random.choice(answers)
        answer_text.color = PURPLE
        answer_text.opacity = 1
        
        # Меняем свечение кнопки при нажатии
        main_button.content.shadow = ft.BoxShadow(
            blur_radius=50,
            color=PURPLE,
            spread_radius=1,
        )
        page.update()

    main_button = ft.Container(
        content=ft.Text("?", size=40, weight="bold"),
        on_click=on_click,
        width=150,
        height=150,
        bgcolor=DARK_PURPLE,
        border_radius=75, # Делаем круглым
        alignment=ft.alignment.center,
        # Тень как неоновое свечение
        shadow=ft.BoxShadow(
            blur_radius=30,
            color=PURPLE,
            offset=ft.Offset(0, 0),
            spread_radius=2,
        ),
        animate=ft.animation.Animation(600, ft.AnimationCurve.DECELERATE),
    )

    # Собираем интерфейс
    page.add(
        ft.Column(
            [
                ft.Container(height=50), # Отступ сверху
                ft.Stack([
                    # Декоративный круг на фоне
                    ft.Container(
                        width=300,
                        height=300,
                        bgcolor=ft.colors.with_opacity(0.1, PURPLE),
                        border_radius=150,
                    ),
                    ft.Column([
                        answer_text,
                    ], alignment=ft.alignment.center, width=300, height=300)
                ]),
                ft.Container(height=40),
                main_button,
                ft.Text(
                    "DO NOT TRUST THE ORACLE", 
                    size=12, 
                    color=ft.colors.GREY_700,
                    letter_spacing=2
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
