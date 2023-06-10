import flet as ft
import requests

from flet_core import RoundedRectangleBorder

txt_button_texts = ["가격", "성능", "배터리", "카메라"]
csv_button_texts = ['갤럭시_모델별_점유율', '스마트폰_모델별_스펙', '스마트폰_성별_연령별_점유율_2022',
                    '스마트폰_성별_연령별_향후구매의향_2022', '스마트폰_점유율_국내', '스마트폰_점유율_글로벌',
                    '스마트폰_판매량_국내_2022', '스마트폰_판매량_글로벌_2022']


def chat_page(page: ft.Page) -> ft.View:
    def btn_on_click(e):
        temp_txt = chat_field.value
        chat_field.value = 'Loading...'
        page.update()
        if temp_txt != '': txt_chat_log.value += f"User: {temp_txt}\n{get_response(temp_txt)}\n"
        chat_field.value = ""
        page.update()

    def loadtxt(e):
        is_empty = len(txt_chat_log.value) == 0
        if is_empty:
            view.scroll_to(key="key")
        button_text = e.get("text")
        txt_chat_log.value += f"Chat Bot: {load_file(button_text)}\n\n"
        page.update()
        if not is_empty:
            view.scroll_to(key="key")

    chat_field = ft.TextField(label="Enter your text", multiline=True, width=page.width - 150,
                              min_lines=1, max_lines=3,
                              color=ft.colors.BLACK87,
                              border_radius=10,
                              border_color=ft.colors.AMBER)

    txt_chat_log = ft.TextField(label="Chat Bot Log", width=page.width - 150, color=ft.colors.BLACK87,
                                border_radius=10,
                                border_color=ft.colors.AMBER,
                                max_lines=9999, multiline=True, read_only=True)

    txt_buttons = [ft.ElevatedButton(text=btn_text, color=ft.colors.WHITE,
                                     bgcolor=ft.colors.AMBER,
                                     style=ft.ButtonStyle(
                                         shape={
                                             ft.MaterialState.DEFAULT: RoundedRectangleBorder(
                                                 radius=10,
                                             ),
                                         },
                                     ),
                                     on_click=lambda event,
                                                     text=btn_text: loadtxt({"text": text}))
                   for btn_text in txt_button_texts]
    csv_buttons = [ft.ElevatedButton(text=btn_text, color=ft.colors.WHITE,
                                     bgcolor=ft.colors.AMBER,
                                     style=ft.ButtonStyle(
                                         shape={
                                             ft.MaterialState.DEFAULT: RoundedRectangleBorder(
                                                 radius=10,
                                             ),
                                         },
                                     ),
                                     on_click=lambda event,
                                                     text=btn_text: loadtxt({"text": text}))
                   for btn_text in csv_button_texts]
    btn_send = ft.ElevatedButton(text="Submit", color=ft.colors.WHITE,
                                 bgcolor=ft.colors.AMBER,
                                 style=ft.ButtonStyle(
                                     shape={
                                         ft.MaterialState.DEFAULT: RoundedRectangleBorder(
                                             radius=10,
                                         ),
                                     },
                                 ),
                                 on_click=btn_on_click)
    view = ft.View(
        route='/chat_page',
        appbar=ft.AppBar(
            automatically_imply_leading=False,
            title=ft.Text(
                value='데이톡스! - Chat Bot',
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
                wrap=True,
                controls=txt_buttons + csv_buttons,
            ),
            ft.Row(controls=[chat_field, btn_send]),
            txt_chat_log,
            ft.Container(
                key="key",
            )
        ],
    )
    return view


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
        ]
    }

    # API 요청 보내기
    response = requests.post(url, json=data, headers=headers)

    # 응답 결과 확인
    if response.status_code == 200:
        result = response.json()
        reply = result['choices'][0]['message']['content']
        return f'Chat Bot: {reply}'
    else:
        return 'Chat Bot: 잠시 후 다시 시도해 주세요.'
        # f'Chat GPT: Error! {response.status_code} {response.reason}'


def load_file(file_name):
    with open(f"./chatbot/{file_name}.txt", 'r', encoding='utf-8') as file:
        return file.read()
