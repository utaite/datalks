import flet as ft

from view.main_page import main_page
from view.share_page import share_page
from view.test_page import test_page
from view.chat_page import chat_page


def main(page: ft.Page):
    def on_route_change(route):
        if route.route == '/':
            page.views.append(main_page(page))
        elif route.route == '/share':
            page.views.append(share_page(page))
        elif route.route == '/test':
            page.views.append(test_page(page))
        elif route.route == '/chat':
            page.views.append(chat_page(page))
        page.update()

    page.title = "데이톡스!"
    page.on_route_change = on_route_change
    page.go(page.route)


ft.app(target=main, view=ft.WEB_BROWSER)
