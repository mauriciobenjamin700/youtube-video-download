from datetime import datetime
import flet as ft

class Search(ft.Container):
    def __init__(
            self,
            download_function,
            placeholder: str = "Search for videos",
            icon: ft.Icon = ft.icons.SEARCH,
            **kwargs,
        ):
        super().__init__(**kwargs)
        self.input = ft.TextField(
            hint_text=placeholder,
            width=600,
        )
        self.button = ft.ElevatedButton(
            icon=icon,
            text="Search",
            bgcolor=ft.Colors.TRANSPARENT, 
            on_click=self.download,
        )
        self.content = ft.Row([self.input, self.button])
        self.content.alignment = ft.MainAxisAlignment.CENTER
        #self.padding = 100
        self.margin = (50)
        self.download_function = download_function

    def download(self, e):
        value = self.input.value
        self.download_function(value, "videos", f"teste-search-{datetime.now()}")