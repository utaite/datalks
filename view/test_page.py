import csv
import flet as ft

from flet_core import RoundedRectangleBorder

colors = {
    "Samsung": ft.colors.BLUE,
    "Apple": ft.colors.BLACK87,
    "LG": ft.colors.ORANGE,
    "others": ft.colors.GREEN,
}


def test_page(page: ft.Page) -> ft.View:
    li1 = list(csv.reader(open(f"./스마트폰_성별_연령별_점유율_2022.csv", "r", encoding="utf-8-sig")))

    return ft.View(
        route='/test_page',
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
            ft.Tabs(
                scrollable=False,
                label_color=ft.colors.AMBER,
                unselected_label_color=ft.colors.BLACK87,
                indicator_color=ft.colors.AMBER,
                tabs=[
                    ft.Tab(
                        text=x,
                        content=test_tab_content(list(filter(lambda y: y[0] == x, li1)))
                    ) for x in unique(map(lambda x: x[0], li1[1:]))
                ],
            ),
        ],
    )


def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]


def test_tab_content(li1) -> ft.Column():
    print(li1)
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
                ]
            ) for i in range(len(li1))
        ]
    )
