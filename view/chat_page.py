import flet as ft
import requests

from flet_core import RoundedRectangleBorder


def chat_page(page: ft.Page) -> ft.View:
    def btn_on_click(e):
        if chat_field.value != "": txt_chat_log.value += f"User: {chat_field.value}\n{get_response(chat_field.value)}\n"
        chat_field.value = ""
        page.update()

    chat_field = ft.TextField(
        label="Enter your text",
        multiline=True,
        width=page.width-150,
        min_lines=1,
        max_lines=3, )
    btn_send = ft.ElevatedButton(text="Submit", on_click=btn_on_click)
    txt_chat_log = ft.TextField(label="Chat GPT Log", width=page.width-150, max_lines=25, multiline=True, read_only=True)

    first_row = ft.Row(controls=[chat_field, btn_send]),
    ft.Column(controls=[first_row, txt_chat_log]),

    return ft.View(
        route='/chat_page',
        appbar=ft.AppBar(
            automatically_imply_leading=False,
            title=ft.Text(
                value='데이톡스! - Chat GPT3.5',
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
            ft.Row(controls=[chat_field, btn_send]),
            ft.Row(controls=[txt_chat_log]),
        ],
    )


def get_response(message):
    # API 요청을 보낼 URL
    url = 'https://api.openai.com/v1/chat/completions'

    # OpenAI API 키
    api_key = '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'

    # 요청 헤더에 API 키 추가
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    # API 요청 데이터
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {'role': 'system', 'content': f'{message}'},
            # {'role': 'user', 'content': 'Who won the world series in 2020?'}
        ]
    }

    # API 요청 보내기
    response = requests.post(url, json=data, headers=headers)

    # 응답 결과 확인
    if response.status_code == 200:
        result = response.json()
        reply = result['choices'][0]['message']['content']
        return f'Chat GPT: {reply}'
    else:
        return f'Chat GPT: Error! {response.status_code} {response.reason}'