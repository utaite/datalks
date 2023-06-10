import flet as ft

from view.chat_page import chat_page
from view.main_page import main_page
from view.personal_all_page import personal_all_page
from view.price_page import price_page
from view.share_page import share_page


def main(page: ft.Page):
    def on_route_change(route):
        page.views.clear()
        if route.route == '/':
            page.views.append(main_page(page))
        elif route.route == '/chat':
            page.views.append(chat_page(page))
        elif route.route == '/personal_all':
            page.views.append(personal_all_page(page))
        elif route.route == '/price':
            page.views.append(price_page(page))
        elif route.route == '/share':
            page.views.append(share_page(page))
        page.update()

    page.title = "데이톡스!"
    page.on_route_change = on_route_change
    page.go(page.route)


ft.app(target=main, view=ft.WEB_BROWSER)
