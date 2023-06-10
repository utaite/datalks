import csv
import flet as ft

from flet_core import RoundedRectangleBorder

colors = {
    "Samsung": ft.colors.BLUE,
    "Apple": ft.colors.BLACK87,
    "LG": ft.colors.ORANGE,
    "others": ft.colors.GREEN,
}
genders = ["남성", "여성"]
ages = list(map(lambda x: f"{x}0대{' 이상' if x == 7 else ''}", range(2, 8)))


def personal_page(page: ft.Page) -> ft.View:
    def go_personal_all(_):
        page.route = "/personal_all"
        page.update()

    def on_click(e):
        if gender.value in genders and age.value in ages:
            view.controls.pop()
            view.controls.append(personal_view(li1, 4 + (genders.index(gender.value) + 1) * len(ages) + ages.index(age.value)))
            view.update()

    li1 = list(csv.reader(open(f"./dataset/스마트폰_성별_연령별_점유율_2022.csv", "r", encoding="utf-8-sig")))

    gender = ft.Dropdown(
        label="성별",
        border_color=ft.colors.AMBER,
        options=[
            ft.dropdown.Option(x) for x in genders
        ]
    )
    age = ft.Dropdown(
        label="연령",
        border_color=ft.colors.AMBER,
        options=[
            ft.dropdown.Option(x) for x in ages
        ]
    )
    view = ft.View(
        route='/personal_page',
        appbar=ft.AppBar(
            automatically_imply_leading=False,
            title=ft.Text(
                value='데이톡스! - 성별/연령별 시장 점유율 분석',
                size=24,
                color=ft.colors.BLACK87,
            ),
            center_title=True,
            bgcolor=ft.colors.WHITE,
        ),
        padding=ft.padding.symmetric(horizontal=20),
        bgcolor=ft.colors.WHITE,
        scroll=ft.ScrollMode.ALWAYS,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    gender,
                    age,
                    ft.ElevatedButton(
                        content=ft.Text(
                            value='확인',
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
                        on_click=on_click,
                    ),
                    ft.ElevatedButton(
                        content=ft.Text(
                            value='전체보기',
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
                        on_click=go_personal_all,
                    ),
                ]
            ),
            ft.Container(),
        ],
    )
    return view


def personal_view(li1, i) -> ft.Column():
    return ft.Column(
        controls=[
            ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        height=40,
                    ),
                    ft.Row(
                        controls=[
                                     ft.Text(
                                         value=f"{li1[i][0]} - {li1[i][1]} 스마트폰 점유율",
                                         size=24,
                                         color=ft.colors.BLACK87,
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
                                                 color=ft.colors.BLACK87,
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
                                    color=ft.colors.WHITE,
                                    size=15,
                                ),
                                color=list(colors.values())[j - 2],
                                radius=40,
                                border_side=ft.BorderSide(0, ft.colors.with_opacity(0, ft.colors.WHITE))
                            ) for j in range(2, len(li1[0]))
                        ],
                        height=120,
                        width=120,
                        sections_space=0,
                        center_space_radius=40,
                    ),
                ],
            ),
        ]
    )
