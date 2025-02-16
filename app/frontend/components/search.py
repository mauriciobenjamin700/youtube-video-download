from datetime import datetime
import flet as ft

class Search(ft.Container):
    def __init__(
            self,
            download_function,
            placeholder: str = "Search for videos",
            icon: ft.Icon = ft.Icons.SEARCH,
            output_placeholder: str = "File Name",
            **kwargs,
        ):
        super().__init__(**kwargs)
        self.input = ft.TextField(
            hint_text=placeholder,
            width=600,
        )
        self.output = ft.TextField(
            hint_text=output_placeholder,
            width=600,
        )
        self.button = ft.ElevatedButton(
            icon=icon,
            text="Search",
            bgcolor=ft.Colors.TRANSPARENT, 
            color=ft.Colors.GREY_800,
            on_click=self.download,
            width=100,
            height=50
        )
        self.content = ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(
                            self.input,
                        ), 
                        ft.Container(
                            self.button,
                        ) 
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Container(
                    self.output,
                    margin=ft.Margin(225, 0, 0, 0)
                )
                
            ]
            
            
        )
        #self.padding = 100
        self.margin = (50)
        self.download_function = download_function

    def download(self, e):
        value = self.input.value
        file_name = self.output.value if self.output.value else f"video-{datetime.now()}"
        self.download_function(value, "videos", file_name)

    def clean_field(self):
        self.input.value = None
        self.output.value = None
        self.update()
        
# https://flet.dev/docs/controls/container
