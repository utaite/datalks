import flet as ft

from view.main_page import main_page


def main(page: ft.Page):
    def on_route_change(route):
        if route.route == '/':
            page.views.append(main_page())
        page.update()

    page.title = "데이톡스!"
    page.on_route_change = on_route_change
    page.go(page.route)


ft.app(target=main, view=ft.WEB_BROWSER)
