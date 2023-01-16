from flet import *
class Home(UserControl):
  def __init__(self,page):
    super().__init__()
    self.page = page

  def build(self):
    return Column(
      controls=[
        Container(
          height=800,width=300,
          bgcolor='red',
          content=Column(
            controls=[
              Text('Welcome to the homepage'),
              Container(
                on_click= lambda _: self.page.go('/login') ,
                content=Text('Goto Login',size=25,color='black')
              )
            ]
          )
          )
        ]
    )