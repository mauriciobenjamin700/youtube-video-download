import flet as ft


from app.backend.main import download_video
from app.frontend.components.alert import AlertDialog
from app.frontend.components.search import Search
from app.frontend.components.loading import Loading


def main(page: ft.Page):


    page.title = "Downloader Youtube Videos"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER


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
        title="Seu download foi concluído com sucesso!",
        content=None,
        on_dismiss=lambda _: search.clean_field(),
    )
    

    page.add(
        search,
        ft.Container(
            content=loading_indicator,
            alignment=ft.alignment.center,
            expand=True,  # Ocupa toda a tela para centralizar o indicador
            bgcolor="transparent",  # Fundo semitransparente (opcional)
        ),
        alert_dialog
    )

   
    
if __name__ == "__main__":
    ft.app(main)