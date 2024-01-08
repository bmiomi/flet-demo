import flet as ft
from flet_route import Routing
from route import app_route


def main(page: ft.Page):

    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_height=500
    page.window_width=500
    
    Routing(page,app_route)
    page.go(page.route)


ft.app(main)