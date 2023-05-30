import flet as ft

from flet_core import RoundedRectangleBorder


def main_page(page: ft.Page) -> ft.View:
    def go_share(e):
        page.route = "/share"
        page.update()

    def go_test(e):
        page.route = "/test"
        page.update()

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
        padding=ft.padding.symmetric(horizontal=20),
        bgcolor=ft.colors.WHITE,
        scroll=ft.ScrollMode.ALWAYS,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
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
            ft.ElevatedButton(
                content=ft.Text(
                    value='시장 점유율은 어떻게 될까요?',
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
                on_click=go_share
            ),
            ft.ElevatedButton(
                content=ft.Text(
                    value='또래는 어떤 스마트폰을 많이 사용할까요?',
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
                on_click=go_test
            ),
        ],
    )
