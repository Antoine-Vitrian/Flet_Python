import flet as ft
import sqlite3
from datetime import timedelta

# Função principal
def main(page: ft.Page):
    page.fonts = {
        'Racer' : 'https://fonts.cdnfonts.com/css/racer'
    }
    page.title = "EA Fórumla Vegas"
    page.window.resizable= False
    page.window.full_screen = False      # Não permite tela cheia
    page.window.maximized = False
    page.window.maximizable = False
    page.window.width =1200
    page.window.height = 800
    page.window.center()

    # Declaração de variáveis
    nome = ft.TextField(label="Digite seu Nome", value="", width=320, border_color="white"),
    # Organização dos containers(div)

    # Espaço para fomulário que alimentará um SQLite
    container_form = ft.Container(
        height=600,
        width=500,
        bgcolor=ft.Colors.TRANSPARENT,
        padding=30,
        alignment=ft.alignment.top_left,
        content=ft.Column(
            controls=[
                ft.Text(
                    value="Adicione sua Volta",
                    size=40,
                    color=ft.Colors.WHITE
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.TextField(label="Minutos", width=100, value="", border_color="white"),
                            ft.TextField(label="Segundos", width=100, value="", border_color="white"),
                            ft.TextField(label="Milésimos", width=100, value="", border_color="white")
                        ]
                    )
                ),
                ft.Text(
                    value="Setores",
                    size=40,
                    color=ft.Colors.WHITE
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.TextField(label="S1", value="", width=100, border_color="white"),
                            ft.TextField(label="S2", value="", width=100, border_color="white"),
                            ft.TextField(label="S3", value="", width=100, border_color="white")
                        ]
                    )
                ),
                ft.Text(
                    value="Pessoa",
                    size=40,
                    color=ft.Colors.WHITE
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            

                        ]
                    )
                ),
                ft.Text(
                    value="Equipe",
                    size=40,
                    color=ft.Colors.WHITE
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.TextField(label="Digite a Equipe", value="", width=320, border_color="white"),
                        ]
                    )
                ),
                ft.Container(height=10),
                ft.ElevatedButton(
                    width=320,
                    bgcolor=ft.Colors.CYAN,
                    content=ft.Text(
                        value="Adicionar Volta",
                        color=ft.Colors.WHITE,
                        size=30
                    )
                )
            ]
        )
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
        alignment=ft.alignment.top_center,
        bgcolor=ft.Colors.TRANSPARENT,
        content=ft.Text(
            italic=True,
            value="EA Fórmula Vegas 2025",
            size=90,
            color=ft.Colors.WHITE
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
            ft.Container(
                height=800,
                width=1500,
                bgcolor=ft.Colors.BLACK,
                opacity=0.4
            ),
            container_main,
        ]
    )
        
    page.add(simple_main)

ft.app(target=main)

# Lista de coisas a fazer

# Interface
# Terminar os botões
# Alinhamento containers(div)
# formulario
# input
# melhor volta
# alternar entre páginas

# back-end
# criar sqlite
# interligar os dois