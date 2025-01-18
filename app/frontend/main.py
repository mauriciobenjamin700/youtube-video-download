import flet as ft


from app.backend.main import download_video
from app.frontend.components.search import Search


def main(page: ft.Page):


    page.title = "Downloader Youtube Videos"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    search = Search(download_video)

    page.add(
        search,
    )

   
    
if __name__ == "__main__":
    ft.app(main)