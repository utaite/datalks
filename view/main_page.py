import flet as ft
from flet_core import RoundedRectangleBorder


def main_page() -> ft.View:
    return ft.View(
        route='/',
        appbar=ft.AppBar(
            automatically_imply_leading=False,
            title=ft.Text(
                value='데이톡스!',
                size=24,
                color=ft.colors.BLACK87,
            ),
            center_title=True,
            bgcolor=ft.colors.WHITE,
        ),
        padding=ft.padding.all(20),
        bgcolor=ft.colors.WHITE,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.TextField(
                        width=500,
                        text_size=18,
                        color=ft.colors.BLACK87,
                        border_radius=10,
                        border_color=ft.colors.AMBER,
                        hint_text='지금 무엇이 궁금한가요?',
                        hint_style=ft.TextStyle(
                            size=18,
                            color=ft.colors.GREY,
                        ),
                    ),
                    ft.ElevatedButton(
                        content=ft.Text(
                            value='질문',
                            size=18,
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.W_500,
                        ),
                        color=ft.colors.WHITE,
                        bgcolor=ft.colors.AMBER,
                        style=ft.ButtonStyle(
                            shape={
                                ft.MaterialState.DEFAULT: RoundedRectangleBorder(
                                    radius=10,
                                ),
                            }
                        ),
                    ),
                ],
            ),
            ft.Text(
                value="갤럭시 VS 아이폰",
                size=24,
                color=ft.colors.BLACK87,
            ),
            ft.Row(
                wrap=True,
                spacing=10,
                run_spacing=10,
                controls=[
                    ft.Container(
                        content=ft.Text(value='갤럭시'),
                        bgcolor=ft.colors.PURPLE,
                        alignment=ft.alignment.center,
                        width=150,
                        height=150,
                    ),
                    ft.Container(
                        content=ft.Text(value='아이폰'),
                        bgcolor=ft.colors.GREY,
                        alignment=ft.alignment.center,
                        width=150,
                        height=150,
                    )
                ],
            ),
            ft.Container(
                height=20,
            ),
            ft.Text(
                value="아이폰 모델별 비교",
                size=24,
                color=ft.colors.BLACK87,
            ),
            ft.Container(
                height=20,
            ),
            ft.Text(
                value="플랫폼별 특징, 장단점 비교",
                size=24,
                color=ft.colors.BLACK87,
            ),
            ft.Container(
                height=20,
            ),
            ft.Text(
                value="플랫폼별 가격 비교",
                size=24,
                color=ft.colors.BLACK87,
            ),
        ],
    )
