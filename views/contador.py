from flet import (Column, TextField, TextAlign, Row,
                  IconButton, icons, MainAxisAlignment,
                  ElevatedButton, ControlEvent, View, Page)


from flet_route import Params, Basket


class ContadorScreen:

    def __init__(self,):

        self.route = '/'
        self.txt_number = TextField(value="0", text_align=TextAlign.RIGHT, width=100)

    def minus_click(self, e: ControlEvent):
        self.txt_number.value = str(int(self.txt_number.value) - 1)
        self.page.update()

    def plus_click(self, e:ControlEvent):
        self.txt_number.value = str(int(self.txt_number.value) + 1)
        self.page.update()

    def view(self, page: Page, params: Params, basket: Basket):
        self.page=page
        return View(
            route=self.route,
            controls=[
                Column(

                    controls=[
                        Row(
                            [
                                IconButton(
                                    icons.REMOVE, on_click=self.minus_click),
                                self.txt_number,
                                IconButton(
                                    icons.ADD, on_click=self.plus_click),
                             
                            ],
                            alignment=MainAxisAlignment.CENTER,
                       
                        ),

                        Row(controls=[
                            ElevatedButton('Siguiente Paguina',
                                           on_click=lambda _: page.go('/home'))
                        ]
                        )
                    ]
    
                    ,alignment=MainAxisAlignment.CENTER,
                

                )
            ])
