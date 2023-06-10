import csv
import flet as ft

colors = {
    "Samsung": ft.colors.BLUE,
    "Apple": ft.colors.BLACK87,
    "LG": ft.colors.ORANGE,
    "others": ft.colors.GREEN,
}


def personal_all_page(page: ft.Page) -> ft.View:
    li1 = list(csv.reader(open(f"./dataset/스마트폰_성별_연령별_점유율_2022.csv", "r", encoding="utf-8-sig")))

    return ft.View(
        route='/personal_all_page',
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
            ft.Tabs(
                scrollable=False,
                label_color=ft.colors.AMBER,
                unselected_label_color=ft.colors.BLACK87,
                indicator_color=ft.colors.AMBER,
                tabs=[
                    ft.Tab(
                        text=x,
                        content=personal_all_tab_content(list(filter(lambda y: y[0] == x, li1)))
                    ) for x in unique(map(lambda x: x[0], li1[1:]))
                ],
                height=1650,
            ),
        ],
    )


def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]


def personal_all_tab_content(li1) -> ft.Column():
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
                ]
            ) for i in range(len(li1))
        ]
    )
