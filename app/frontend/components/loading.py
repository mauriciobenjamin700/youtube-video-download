import flet as ft

class Loading(ft.ProgressRing):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.visible = False
        

    def show(self):
        self.visible = True
        self.update()
    
    def hide(self):
        self.visible = False
        self.update()

# https://flet.dev/docs/controls/progressring/