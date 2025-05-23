import flet as ft
import sqlite3


# Função principal
def main(page: ft.Page):
    page.title = "EA Fórumla Vegas"
    page.window.resizable= False
    page.window.full_screen = False      # Não permite tela cheia
    page.window.maximized = False
    page.window.maximizable = False
    page.window.width =1200
    page.window.height = 800
    page.window.center()

    # Cria ou conecta o banco
    connection = sqlite3.connect("volta.db")
    cursor = connection.cursor()

    # Declaração de variáveis
    nome = ft.TextField(label="Digite seu Nome", width=320, border_color="white")
    equipe = ft.TextField(label="Digite a Equipe", width=320, border_color="white")
    minutos = ft.TextField(label="Minutos", width=100, border_color="white")
    segundos = ft.TextField(label="Segundos", width=100, border_color="white")
    milesimos = ft.TextField(label="Milésimos", width=100, border_color="white")
    s1 = ft.TextField(label="S1", width=100, border_color="white")                      
    s2 = ft.TextField(label="S2", width=100, border_color="white")                       
    s3 = ft.TextField(label="S3", width=100, border_color="white")

    # Banco de dados
    def adicionar_volta(e):
        # Tabela Victor
        if nome.value == "Victor":
        # Deletando a tabela
            cursor.execute("""
        DROP TABLE IF NOT EXISTS voltas_vats
        """)
            
            # Criando tabela
            cursor.execute("""
        CREATE TABLE IF NOT EXISTS voltas_vats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                minutos INTEGER NOT NULL,
                segundos INTEGER NOT NULL,
                milesimos INTEGER NOT NULL,
                s1 REAL NOT NULL,
                s2 REAL NOT NULL,
                s3 REAL NOT NULL,
                equipe TEXT
        )""")
            
            # Adiciona Valores na tabela 
            cursor.execute("""
        INSERT INTO (nome, minutos, segundos, milesimos, s1, s2, s3, equipe)
        VALUES( ?, ?, ?, ?, ?, ?, ?, ?)
        """), nome.value, minutos.value, segundos.value, milesimos.value, s1.value, s2.value, s3.value, equipe.value

            
        # Tabela Gabriel
        elif nome.value == "Gabriel":
            # Deletando a tabela
            cursor.execute("""
        DROP TABLE IF NOT EXISTS voltas_gvts
        """)
            
            # Criando tabela
            cursor.execute("""
        CREATE TABLE IF NOT EXISTS voltas_gvts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                minutos INTEGER NOT NULL,
                segundos INTEGER NOT NULL,
                milesimos INTEGER NOT NULL,
                s1 REAL NOT NULL,
                s2 REAL NOT NULL,
                s3 REAL NOT NULL,
                equipe TEXT
        )""")
            
            # Adiciona valores na tabela
            cursor.execute("""
        INSERT INTO (nome, minutos, segundos, milesimos, s1, s2, s3, equipe)
        VALUES( ?, ?, ?, ?, ?, ?, ?, ?)
        """), nome.value, minutos.value, segundos.value, milesimos.value, s1.value, s2.value, s3.value, equipe.value
            
        # Se não for nenhum dos dois, simplesmente não faz nada
        else:
            pass

        # Atualiza o banco de dados
        connection.commit()
        connection.close()
        page.update() 

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
                            minutos,
                            segundos,
                            milesimos
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
                            s1,
                            s2,
                            s3
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
                            nome
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
                            equipe,
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
                        size=30,
                    )
                )
            ]
        )
    )

    # Espaço para se visualizar dados de nosso SQLite
    container_list = ft.Container(
        height=600,
        width=700,
        bgcolor=ft.Colors.TRANSPARENT,
        content=ft.Column(
            controls=[
                ft.Text(
                    value="   Melhores Voltas",
                    color="white",
                    size=60,
                    italic=True  
                )
            ]
        )
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