# import flet as ft

# def main(page: ft.Page):
#     page.window.always_on_top = True

#     # URL de imagem válida (exemplo genérico)
#     page.decoration = ft.BoxDecoration(
#         image=ft.DecorationImage(
#             src="https://upload.wikimedia.org/wikipedia/commons/e/e1/Las_Vegas_Strip.JPG",  # imagem real
#             fit=ft.ImageFit.COVER
#         )
#     )

#     page.update()

# ft.app(target=main)
import flet as ft

def main(page: ft.Page):
    page.title = "Imagem de Fundo"
    page.padding = 0
    page.window.resizable = False
    page.window.width =1200
    page.window.height = 800


    # Stack para sobrepor a imagem com conteúdo
    page.add(
        ft.Stack([
            ft.Image(
                src="vegasf1.png",  # imagem local
                fit=ft.ImageFit.COVER,
                expand = True
            ),
            ft.Container(
                ft.Text(
                    value="EA Formula USA",
                    color = "white",
                    size= 100
                )
            )
        ])
    )
    page.add(
        ft.Button(
            ft.Image(
                src="vegasTrc.png",
                width=100
            )
        )
    )

ft.app(target=main)


