import flet as ft
import sqlite3


def main(page: ft.Page):
    page.title = "EA Fórmula Vegas"
    page.window.resizable = False
    page.window.full_screen = False
    page.window.maximized = False
    page.window.maximizable = False
    page.window.width = 1200
    page.window.height = 800
    page.window.center()

    # Banco de dados
    connection = sqlite3.connect("volta.db")
    cursor = connection.cursor()

    # Cria tabela (geral)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS voltas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            minutos INTEGER NOT NULL,
            segundos INTEGER NOT NULL,
            milesimos INTEGER NOT NULL,
            s1 REAL NOT NULL,
            s2 REAL NOT NULL,
            s3 REAL NOT NULL,
            equipe TEXT
        )
    """)

    # Inputs
    nome = ft.TextField(label="Digite seu Nome", width=320, border_color="white")
    equipe = ft.TextField(label="Digite a Equipe", width=320, border_color="white")
    minutos = ft.TextField(label="Minutos", width=100, border_color="white")
    segundos = ft.TextField(label="Segundos", width=100, border_color="white")
    milesimos = ft.TextField(label="Milésimos", width=100, border_color="white")
    s1 = ft.TextField(label="S1", width=100, border_color="white")
    s2 = ft.TextField(label="S2", width=100, border_color="white")
    s3 = ft.TextField(label="S3", width=100, border_color="white")

    # Lista de melhores voltas
    lista_voltas = ft.Column()

    def carregar_voltas():
        lista_voltas.controls.clear()
        voltas = cursor.execute(
            "SELECT nome, minutos, segundos, milesimos, s1, s2, s3 FROM voltas ORDER BY minutos, segundos, milesimos LIMIT 4"
        ).fetchall()

        for v in voltas:
            lista_voltas.controls.append(
                ft.Text(f"{v[0]} - {v[1]}:{v[2]}.{v[3]}", color=ft.Colors.WHITE, size=55)
            ),
            lista_voltas.controls.append(
                ft.Text(f"S1 - {v[4]}    S2 - {v[5]}    S3 - {v[6]}", color=ft.Colors.WHITE, size=20, weight=ft.FontWeight.BOLD
)
            )

        page.update()

    # Adicionar volta
    def adicionar_volta(e):
        try:
            cursor.execute("""
                INSERT INTO voltas (nome, minutos, segundos, milesimos, s1, s2, s3, equipe)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                nome.value,
                int(minutos.value),
                int(segundos.value),
                int(milesimos.value),
                float(s1.value),
                float(s2.value),
                float(s3.value),
                equipe.value
            ))
            connection.commit()

            # Limpa os campos
            for campo in [nome, equipe, minutos, segundos, milesimos, s1, s2, s3]:
                campo.value = ""

            carregar_voltas()

        except Exception as erro:
            print("Erro ao adicionar volta:", erro)

    # Formulário
    container_form = ft.Container(
        height=600,
        width=500,
        bgcolor=ft.Colors.TRANSPARENT,
        padding=30,
        alignment=ft.alignment.top_left,
        content=ft.Column(
            controls=[
                ft.Text("Adicione sua Volta", size=40, color=ft.Colors.WHITE),
                ft.Row([minutos, segundos, milesimos]),
                ft.Text("Setores", size=40, color=ft.Colors.WHITE),
                ft.Row([s1, s2, s3]),
                ft.Text("Pessoa", size=40, color=ft.Colors.WHITE),
                nome,
                ft.Text("Equipe", size=40, color=ft.Colors.WHITE),
                equipe,
                ft.Container(height=10),
                ft.ElevatedButton(
                    width=320,
                    bgcolor=ft.Colors.CYAN,
                    content=ft.Text("Adicionar Volta", color=ft.Colors.WHITE, size=30),
                    on_click=adicionar_volta
                )
            ]
        )
    )

    # Lista de voltas
    container_list = ft.Container(
        height=600,
        width=500,
        bgcolor=ft.Colors.TRANSPARENT,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("Melhores Voltas", color="white", size=60, italic=True),
                lista_voltas
            ]
        )
    )

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

    container01 = ft.Row(spacing=0, controls=[container_form, container_list], width=1200)
    container_main = ft.Column(spacing=0, controls=[container01, container_buttons])

    simple_main = ft.Stack(
        controls=[
            ft.Container(ft.Image(src="vegasf1.png", height=800, width=1500)),
            ft.Container(height=800, width=1500, bgcolor=ft.Colors.BLACK, opacity=0.4),
            container_main,
        ]
    )

    page.add(simple_main)
    carregar_voltas()


ft.app(target=main)
