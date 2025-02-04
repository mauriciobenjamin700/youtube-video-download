import os.path as Path
import sys

sys.path.append(Path.abspath(Path.join(Path.dirname(__file__), "..", "..")))

import flet as ft
from components.loading import Loading

def main(page: ft.Page):
    page.title = "Teste do LoadingIndicator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    loading_indicator = Loading()
    loading_indicator.show()
    def toggle_loading(e):
        loading_indicator.visible = not loading_indicator.visible
        page.update()

    toggle_button = ft.ElevatedButton(text="Alternar Loading", on_click=toggle_loading)

    page.add(toggle_button, loading_indicator)

if __name__ == "__main__":
    ft.app(main)
