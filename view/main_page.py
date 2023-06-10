import csv

import flet as ft

from flet_core import RoundedRectangleBorder


def get_color(is_black: bool):
    return ft.colors.BLACK87 if is_black else ft.colors.WHITE


def main_page(page: ft.Page) -> ft.View:
    view = ft.View(
        route='/',
        appbar=ft.AppBar(
            automatically_imply_leading=False,
            title=ft.Text(
                value='데이톡스!',
                size=24,
                color=get_color(is_black=True),
            ),
            center_title=True,
            bgcolor=ft.colors.WHITE,
        ),
        padding=ft.padding.all(0),
        bgcolor=ft.colors.WHITE,
        scroll=ft.ScrollMode.ALWAYS,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )

    for i, v in enumerate(views):
        view.controls.append(ft.Container(
            bgcolor=get_color(is_black=i % 2 == 0),
            content=v(page, view, is_black=i % 2 == 0),
        ))

    return view


def share_view(page: ft.Page, view: ft.View, is_black: bool) -> ft.Column():
    def go_share(_):
        page.route = "/share"
        page.update()

    return ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Container(height=50),
            ft.Text(
                value=f"먼저, 국내/외 스마트폰 시장 점유율을 알려드릴게요!",
                size=24,
                color=get_color(not is_black),
            ),
            ft.ElevatedButton(
                content=ft.Text(
                    value='시장 점유율은 어떻게 될까요?',
                    size=18,
                    color=get_color(is_black),
                    weight=ft.FontWeight.W_500,
                ),
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
            ft.Container(height=50),
        ]
    )


def personal_view(page: ft.Page, view: ft.View, is_black: bool) -> ft.Column():
    genders = ["남성", "여성"]
    ages = list(map(lambda x: f"{x}0대{' 이상' if x == 7 else ''}", range(2, 8)))

    def on_click_personal(_):
        if gender.value in genders and age.value in ages:
            index = views.index(chat_view)
            for _ in range(len(view.controls) - index):
                view.controls.pop()

            i = 4 + (genders.index(gender.value) + 1) * len(ages) + ages.index(age.value)
            chart = ft.Container(
                bgcolor=get_color(not is_black),
                content=personal_chart(page, li1, i, not is_black),
            )

            for i, v in enumerate(views[:index] + [chart] + views[index:]):
                if i >= len(views) - index:
                    if type(v) is ft.Container:
                        view.controls.append(v)
                    else:
                        view.controls.append(ft.Container(
                            bgcolor=get_color(is_black=i % 2 == 0),
                            content=v(page, view, is_black=i % 2 == 0),
                        ))
            view.update()

    gender = ft.Dropdown(
        label="성별",
        border_color=ft.colors.AMBER,
        label_style=ft.TextStyle(
            size=15,
            color=ft.colors.AMBER,
        ),
        text_style=ft.TextStyle(
            size=18,
            color=ft.colors.AMBER,
        ),
        options=[
            ft.dropdown.Option(x) for x in genders
        ]
    )
    age = ft.Dropdown(
        label="연령",
        border_color=ft.colors.AMBER,
        label_style=ft.TextStyle(
            size=15,
            color=ft.colors.AMBER,
        ),
        text_style=ft.TextStyle(
            size=18,
            color=ft.colors.AMBER,
        ),
        options=[
            ft.dropdown.Option(x) for x in ages
        ]
    )
    li1 = list(csv.reader(open(f"./dataset/스마트폰_성별_연령별_점유율_2022.csv", "r", encoding="utf-8-sig")))
    return ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Container(height=50),
            ft.Text(
                value=f"다음으로, 또래들이 어떤 스마트폰을 사용하는지 알려드릴게요!",
                size=24,
                color=get_color(not is_black),
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    gender,
                    age,
                    ft.ElevatedButton(
                        content=ft.Text(
                            value='확인',
                            size=18,
                            color=get_color(is_black),
                            weight=ft.FontWeight.W_500,
                        ),
                        color=get_color(is_black),
                        bgcolor=ft.colors.AMBER,
                        style=ft.ButtonStyle(
                            shape={
                                ft.MaterialState.DEFAULT: RoundedRectangleBorder(
                                    radius=10,
                                ),
                            }
                        ),
                        on_click=on_click_personal,
                    ),
                ]
            ),
            ft.Container(height=50),
        ],
    )


def personal_chart(page: ft.Page, li1: list, i: int, is_black: bool) -> ft.Column():
    def go_personal_all(_):
        page.route = "/personal_all"
        page.update()

    colors = {
        "Samsung": ft.colors.BLUE,
        "Apple": get_color(not is_black),
        "LG": ft.colors.ORANGE,
        "others": ft.colors.GREEN,
    }

    return ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Container(height=50),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                             ft.Text(
                                 value=f"{li1[i][1]} 스마트폰 점유율",
                                 size=24,
                                 color=get_color(not is_black),
                             ),
                         ] + [
                             ft.Row(
                                 controls=[
                                     ft.Container(
                                         width=20,
                                     ),
                                     ft.Text(
                                         value=k,
                                         size=12,
                                         color=get_color(not is_black),
                                         weight=ft.FontWeight.W_500,
                                     ),
                                     ft.Container(
                                         width=10,
                                         height=10,
                                         bgcolor=v,
                                     ),
                                 ]
                             ) for (k, v) in colors.items()
                         ],
            ),
            ft.Container(
                height=20,
            ),
            ft.PieChart(
                sections=[
                    ft.PieChartSection(
                        li1[i][j],
                        title=f"{li1[i][j]}%",
                        title_style=ft.TextStyle(
                            color=get_color(is_black),
                            size=15,
                        ),
                        color=list(colors.values())[j - 2],
                        radius=40,
                        border_side=ft.BorderSide(0, ft.colors.with_opacity(0, get_color(is_black)))
                    ) for j in range(2, len(li1[0]))
                ],
                height=120,
                width=120,
                sections_space=0,
                center_space_radius=40,
            ),
            ft.Container(height=20),
            ft.ElevatedButton(
                content=ft.Text(
                    value='다른 연령대는 어떤 스마트폰을 사용할까요?',
                    size=18,
                    color=get_color(is_black),
                    weight=ft.FontWeight.W_500,
                ),
                bgcolor=ft.colors.AMBER,
                style=ft.ButtonStyle(
                    shape={
                        ft.MaterialState.DEFAULT: RoundedRectangleBorder(
                            radius=10,
                        ),
                    }
                ),
                on_click=go_personal_all,
            ),
            ft.Container(height=50),
        ],
    )


def chat_view(page: ft.Page, view: ft.View, is_black: bool) -> ft.Column():
    def go_chat(_):
        page.route = "/chat"
        page.update()

    return ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Container(height=50),
            ft.Text(
                value=f"이제, 당신에게 맞는 스마트폰을 추천해드릴게요!",
                size=24,
                color=get_color(not is_black),
            ),
            ft.ElevatedButton(
                content=ft.Text(
                    value='어떤 모델을 사용해야 할까요?',
                    size=18,
                    color=get_color(is_black),
                    weight=ft.FontWeight.W_500,
                ),
                bgcolor=ft.colors.AMBER,
                style=ft.ButtonStyle(
                    shape={
                        ft.MaterialState.DEFAULT: RoundedRectangleBorder(
                            radius=10,
                        ),
                    }
                ),
                on_click=go_chat,
            ),
            ft.Container(height=50),
        ]
    )


def price_view(page: ft.Page, view: ft.View, is_black: bool) -> ft.Column():
    def go_price(_):
        page.route = "/price"
        page.update()

    return ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Container(height=50),
            ft.Text(
                value=f"마지막으로, 언제 사는 게 가장 좋을까요?",
                size=24,
                color=get_color(not is_black),
            ),
            ft.ElevatedButton(
                content=ft.Text(
                    value='지금 가격은 어떨까요?',
                    size=18,
                    color=get_color(is_black),
                    weight=ft.FontWeight.W_500,
                ),
                bgcolor=ft.colors.AMBER,
                style=ft.ButtonStyle(
                    shape={
                        ft.MaterialState.DEFAULT: RoundedRectangleBorder(
                            radius=10,
                        ),
                    }
                ),
                on_click=go_price,
            ),
            ft.Container(height=50),
        ]
    )


views = [share_view, personal_view, chat_view, price_view]
