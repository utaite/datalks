import csv
import flet as ft

from flet_core import RoundedRectangleBorder

colors = {
    "국내": {
        "Samsung": ft.colors.BLUE,
        "Apple": ft.colors.BLACK87,
        "LG": ft.colors.ORANGE,
        "others": ft.colors.GREEN,
    },
    "글로벌": {
        "Samsung": ft.colors.BLUE,
        "Apple": ft.colors.BLACK87,
        "Xiami": ft.colors.PURPLE,
        "OPPO": ft.colors.AMBER,
        "vivo": ft.colors.CYAN,
        "others": ft.colors.GREEN,
    },
}


def share_page(page: ft.Page) -> ft.View:
    return ft.View(
        route='/share_page',
        appbar=ft.AppBar(
            automatically_imply_leading=False,
            title=ft.Text(
                value='데이톡스! - 시장 점유율 분석',
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
                        text="국내 점유율",
                        content=share_tab_content("국내"),
                    ),
                    ft.Tab(
                        text="글로벌 점유율",
                        content=share_tab_content("글로벌"),
                    ),
                ],
                height=1300,
            ),
        ],
    )


def share_tab_content(name) -> ft.Column():
    li1 = list(csv.reader(open(f"./스마트폰_점유율_{name}.csv", "r", encoding="utf-8-sig")))
    return ft.Column(
        controls=[
            ft.Column(
                controls=[
                    ft.Container(
                        height=40,
                    ),
                    ft.Row(
                        controls=[
                                     ft.Text(
                                         value=f"{li1[0][i * 4 + 1].split(' ')[0]}년 {name} 스마트폰 점유율",
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
                                     ) for (k, v) in colors[name].items()]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                                expand=True,
                                controls=[
                                    ft.Text(
                                        value=li1[0][i * 4 + 1 + j],
                                        size=24,
                                        color=ft.colors.BLACK87,
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                    ft.Container(
                                        height=20,
                                    ),
                                    ft.PieChart(
                                        sections=[
                                            ft.PieChartSection(
                                                li1[k][i * 4 + 1 + j],
                                                title=f"{li1[k][i * 4 + 1 + j]}%",
                                                title_style=ft.TextStyle(
                                                    color=ft.colors.WHITE,
                                                    size=15,
                                                ),
                                                color=colors[name][li1[k][0]],
                                                radius=40,
                                                border_side=ft.BorderSide(0, ft.colors.with_opacity(0, ft.colors.WHITE))
                                            ) for k in range(1, len(li1))
                                        ],
                                        height=120,
                                        width=120,
                                        sections_space=0,
                                        center_space_radius=40,
                                    ),
                                ]
                            ) for j in range(4)
                        ],
                    ),
                ]
            ) for i in range(len(li1[0]) // 4)
        ]
    )
