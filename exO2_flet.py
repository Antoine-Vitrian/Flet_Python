import flet as ft

def main(page: ft.Page):
    page.title = "Imagem de Fundo"
    page.padding = 0

    # Container com imagem de fundo ocupando toda a janela
    background = ft.Container(
        expand=True,
        src="vegasf1.png",  # Caminho local ou URL da imagem
        fit=ft.ImageFit.COVER,
    )

    page.add(background)
    page.update()

ft.app(target=main)
