import flet as ft
from typing import Callable

class AlertDialog(ft.AlertDialog):
    def __init__(
            self, 
            title: str, 
            content: ft.Control | None, 
            on_dismiss:Callable | None = None, 
            **kwargs):
        super().__init__(
            title=ft.Text(title), 
            content=content, 
            on_dismiss=on_dismiss, 
            **kwargs
        )
        

    def show(self, e):
        self.open = True

    def hide(self, e):
        self.open = False