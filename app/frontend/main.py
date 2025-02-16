import flet as ft


from app.backend.main import download_video
from app.frontend.components.alert import AlertDialog
from app.frontend.components.search import Search
from app.frontend.components.loading import Loading


def main(page: ft.Page):


    page.title = "Downloader Youtube Videos"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    
    page.window.width = 800
    page.window.height = 600
    page.window.max_width = 800
    page.window.max_height = 600
    page.window.full_screen = False
    page.window.resizable = False
    page.window.movable = True

    page.bgcolor = ft.Colors.WHITE
    
    is_dark_mode = False
    
    def change_theme(event):
        nonlocal is_dark_mode
        is_dark_mode = not is_dark_mode
        page.bgcolor = ft.Colors.GREY_900 if is_dark_mode else ft.Colors.WHITE
        search.input.bgcolor = ft.Colors.GREY_700 if is_dark_mode else ft.Colors.GREY_300
        search.input.color = ft.Colors.WHITE if is_dark_mode else ft.Colors.BLACK
        search.output.bgcolor = ft.Colors.GREY_700 if is_dark_mode else ft.Colors.GREY_300
        search.output.color = ft.Colors.WHITE if is_dark_mode else ft.Colors.BLACK
        search.button.bgcolor = ft.Colors.GREY_700 if is_dark_mode else ft.Colors.GREY_300
        search.button.color = ft.Colors.WHITE if is_dark_mode else ft.Colors.BLACK
        change_theme_button.icon = ft.Icons.DARK_MODE if is_dark_mode else ft.Icons.LIGHT_MODE
        page.update()
    
    change_theme_button = ft.IconButton(
        ft.Icons.LIGHT_MODE,
        on_click=change_theme
    )


    def handle_download(url: str, output: str, file_name: str) -> None:
        loading_indicator.show()
        page.update()
        try:
            download_video(url, output, file_name)
        finally:
            loading_indicator.hide()
            page.open(alert_dialog)
            search.clean_field()

    loading_indicator = Loading(
        width=100,
        height=100,
    )

    search = Search(handle_download)

    alert_dialog = AlertDialog(
        title="Download successful!",
        content=None,
        on_dismiss=lambda _: search.clean_field(),
    )
    

    page.add(
        ft.Container(
            change_theme_button,
            alignment=ft.alignment.top_right,
        ),
        search,
        ft.Container(
            content=loading_indicator,
            alignment=ft.alignment.center,
            expand=True,  # Ocupa toda a tela para centralizar o indicador
            bgcolor="transparent",  # Fundo semitransparente (opcional)
        ),
        alert_dialog,
    )
    
    change_theme(None)

   
    
if __name__ == "__main__":
    ft.app(main)