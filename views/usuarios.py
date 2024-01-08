from flet import (Column,TextField,
                  ElevatedButton,Text,
                  View, Page)

from flet_route import Params,Basket

class UsuarioScreen:
    
    def __init__(self):
        self.route = '/usuario'



    def view(self,page: Page,params:Params,basket:Basket):
        
        self.page=page

        textfield=TextField(hint_text='Ingrese un Usuario')

        return View(
            route=self.route,
            controls=[Column(
            controls=[  
                Text('Estoy en UsuarioScreen'),
                textfield,
                ElevatedButton('Cambiar de paguina.', on_click=lambda _:page.go('/'))
            ]
        )]) 