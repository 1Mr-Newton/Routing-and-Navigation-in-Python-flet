from flet import *

class Login(UserControl):
  def __init__(self,page):
    super().__init__()
    self.page = page

  def build(self):
    return Column(
      controls=[
        Container(
          height=800,width=200,
          bgcolor='blue',
          content=Column(
            controls=[
              Text('Welcome back \n This is the login pages'),
              Container(
                on_click= lambda _: self.page.go('/'), 
                content=Text('Goto Home',size=25,color='black')
              )
            ]
          )
          )
        ]
    )