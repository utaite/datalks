import flet as ft
import pandas as pd
import plotly.graph_objects as go

from flet_core import RoundedRectangleBorder
from flet.plotly_chart import PlotlyChart

labels = {
    "갤럭시 S22": [600000, 1100000],
    "갤럭시 S22 Plus": [700000, 1400000],
    "갤럭시 S22 Ultra": [800000, 1800000],
    "갤럭시 S23": [700000, 1400000],
    "갤럭시 S23 Plus": [900000, 1500000],
    "갤럭시 S23 Ultra": [1000000, 1800000],
    "아이폰 14": [1000000, 1500000],
    "아이폰 14 Plus": [1000000, 1600000],
    "아이폰 14 Pro": [1300000, 1800000],
    "아이폰 14 Pro Max": [1500000, 2000000],
}


def price_page(page: ft.Page) -> ft.View:
    def on_click(e):
        view.controls.pop()
        view.controls.append(PlotlyChart(figure=price_figure(e.control.key, labels[e.control.key])))
        view.update()

    view = ft.View(
        route='/price_page',
        appbar=ft.AppBar(
            automatically_imply_leading=False,
            title=ft.Text(
                value='데이톡스! - 가격 추이 변동',
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
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.ElevatedButton(
                        key=x,
                        content=ft.Text(
                            value=x,
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
                        on_click=on_click
                    ) for x in list(labels.keys())
                ],
            ),
            ft.Container(),
        ],
    )
    return view


def price_figure(label, yaxis):
    fig = go.Figure()
    df = pd.read_csv(f'./dataset/{label}.csv')

    df['가격'] = df['가격'].str.replace(',', '').astype(int)
    df['날짜'] = pd.to_datetime(df['날짜'], format='%Y년 %m월 %d일')

    fig.add_trace(go.Scatter(x=df['날짜'], y=df['가격'], mode='lines', name='가격'))
    fig.add_trace(go.Scatter(x=[df['날짜'].iloc[df['가격'].idxmin()]], y=[df['가격'].min()], mode='markers', name='최저가',
                             marker=dict(symbol='circle', size=8, color='red')))
    fig.add_trace(go.Scatter(x=[df['날짜'].iloc[df['가격'].idxmax()]], y=[df['가격'].max()], mode='markers', name='최고가',
                             marker=dict(symbol='circle', size=8, color='green')))

    fig.update_layout(
        title=label,
        xaxis=dict(title='월별'),
        yaxis=dict(title='가격'),
        yaxis_tickformat=',',
        yaxis_range=yaxis,
        showlegend=True
    )

    fig.update_layout(
        annotations=[
            go.layout.Annotation(
                x=df['날짜'].iloc[df['가격'].idxmin()],
                y=df['가격'].min(),
                text=f"최저가: {df['가격'].min():,}",
                showarrow=True,
                arrowhead=7,
                ax=0,
                ay=40
            ),
            go.layout.Annotation(
                x=df['날짜'].iloc[df['가격'].idxmax()],
                y=df['가격'].max(),
                text=f"최고가: {df['가격'].max():,}",
                showarrow=True,
                arrowhead=7,
                ax=0,
                ay=-40
            )
        ]
    )
    return fig
