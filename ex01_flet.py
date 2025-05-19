import flet as ft

# Declaração de variáveis
# Organização dos containers(div)

# Espaço para fomulário que alimentará um SQLite
container_form = ft.Container(
    height=600,
    width=500,
    bgcolor=ft.Colors.CYAN_100
)

# Espaço para se visualizar dados de nosso SQLite
container_list = ft.Container(
    height=600,
    width=700,
    bgcolor=ft.Colors.PURPLE
)

# Local onde estará os três principais botões
# Miami, Texas e Las Vegas
container_buttons = ft.Container(
    height=200,
    width=1200,
    bgcolor=ft.Colors.RED,
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

# Botões
def botoes():
    pass

botoes()

# Função principal
def main(page: ft.Page):
    page.title = "Imagem de Fundo"
    page.padding = 0
    page.window.resizable= False
    page.window.full_screen = False      # Não permite tela cheia
    page.window.maximized = False
    page.window.maximizable = False
    page.window.width =1200
    page.window.height = 800
    page.window.center()


    simple_main = ft.Stack(
        controls=[
            container_main,
            ft.Container(ft.Image(
                src="vegasf1.png",
                height=800,
                width=1500,
            ))
        ]
    )
        
    page.add(simple_main)

ft.app(target=main)

