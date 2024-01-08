from views.contador import ContadorScreen
from views.home import HomeScreen
from views.usuarios import UsuarioScreen
from flet_route import path


app_route=[
        path(
            url='/',
            clear=True,
            view=ContadorScreen().view
        ),
        path(
            url='/home',
            clear=True,
            view=HomeScreen().view
        ),
        path(
            url='/usuario',
            clear=True,
            view=UsuarioScreen().view
        )
    ]

