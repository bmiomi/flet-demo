from flet import (Column,TextField,
                  ElevatedButton,View, 
                  Page)

from flet_route import Params,Basket

class HomeScreen:
    
    def __init__(self):
        self.route = '/home'


    def view(self,page: Page,params:Params,basket:Basket):
        self.page=page
        textfield=TextField(hint_text='Ingrese un texto al home')

        return View(
            route=self.route,
            controls=[ Column(
            controls=[  
                textfield,
                ElevatedButton('Cambiar',on_click=lambda _:page.go('/usuario'))
            ]
        )])