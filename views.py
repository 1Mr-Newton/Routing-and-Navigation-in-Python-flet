from flet import *
from pages.home import Home
from pages.login import Login

def views_handler(page):
  return {
    '/':View(
        route='/',
        controls=[
          Home(page)
        ]
      ),
    '/login':View(
        route='/login',
        controls=[
          Login(page)
        ]
      ),
  }