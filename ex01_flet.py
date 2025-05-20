import flet as ft

# Função principal
def main(page: ft.Page):
    page.fonts = {
        'Racer' : 'https://fonts.cdnfonts.com/css/racer'
    }
    page.title = "EA Fórumula USA"
    page.window.resizable= False
    page.window.full_screen = False      # Não permite tela cheia
    page.window.maximized = False
    page.window.maximizable = False
    page.window.width =1200
    page.window.height = 800
    page.window.center()

    # Declaração de variáveis

    # Botões

    # Botão Miami
    botao1 = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text(value="MIAMI", size=50, color=ft.Colors.BLACK, font_family='Racer'),
                ],
            ),
            width=320,
            height=160,
            bgcolor=ft.Colors.WHITE
        ),
    )

    # Botão Texas
    botao2 = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text(value="TEXAS", size=50, color=ft.Colors.BLACK, font_family='Racer'),
                ],
            ),
            width=320,
            height=160,
            bgcolor=ft.Colors.WHITE
        ),
    )

    # Botão Vegas
    botao3 = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text(value="LAS VEGAS", size=50, color=ft.Colors.BLACK),
                ],
            ),
            width=320,
            height=100,
            bgcolor=ft.Colors.WHITE,
            border=ft.border.all(2, ft.Colors.BLACK),  # Borda de 2px preta
            border_radius=10
        ),
    )

    # Organização dos containers(div)

    # Espaço para fomulário que alimentará um SQLite
    container_form = ft.Container(
        height=600,
        width=500,
        bgcolor=ft.Colors.TRANSPARENT
    )

    # Espaço para se visualizar dados de nosso SQLite
    container_list = ft.Container(
        height=600,
        width=700,
        bgcolor=ft.Colors.TRANSPARENT
    )

    # Local onde estará os três principais botões
    # Miami, Texas e Las Vegas
    container_buttons = ft.Container(
        height=200,
        width=1200,
        bgcolor=ft.Colors.TRANSPARENT,
        content=ft.Row(
            controls=[
                botao1,
                botao2,
                botao3
            ]
        )
    )


    # Agrupamento de containers em linha
    # tipo um display flex do css
    container01 = ft.Row(
        spacing = 0,
        controls=[container_form, container_list],
        width=1200
    )

    # Agrupamento de containers em coluna
    # tipo "flex-flow: column"
    container_main = ft.Column(
        spacing=0,
        controls=[container01, container_buttons]
    )
    simple_main = ft.Stack(
        controls=[
            ft.Container(ft.Image(
                src="vegasf1.png",
                height=800,
                width=1500,
            )),
            container_main,
        ]
    )
        
    page.add(simple_main)

ft.app(target=main)

