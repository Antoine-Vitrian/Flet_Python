import flet as ft
import sqlite3


# 🔧 Função para criar banco se não existir
def criar_banco():
    con = sqlite3.connect("voltas.db")
    cursor = con.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS voltas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        minutos INTEGER,
        segundos INTEGER,
        milesimos INTEGER,
        equipe TEXT
    )
    """)
    con.commit()
    con.close()


def main(page: ft.Page):
    criar_banco()  # cria banco na inicialização

    page.window_width = 1000
    page.window_height = 600
    page.title = "Corridas Vegas"

    # 🏁 Campos do formulário
    nome = ft.TextField(label="Nome", width=150)
    minutos = ft.TextField(label="Minutos", width=100)
    segundos = ft.TextField(label="Segundos", width=100)
    milesimos = ft.TextField(label="Milésimos", width=100)
    equipe = ft.TextField(label="Equipe", width=150)

    # 📄 Lista onde aparecem os dados
    lista_voltas = ft.Column(scroll="AUTO")

    container_list = ft.Container(
        content=lista_voltas,
        width=500,
        height=500,
        bgcolor=ft.Colors.GREY_900,
        padding=10
    )

    # 🔥 Função para inserir dados
    def adicionar_volta(e):
        con = sqlite3.connect("voltas.db")
        cursor = con.cursor()
        cursor.execute("""
            INSERT INTO voltas (nome, minutos, segundos, milesimos, equipe)
            VALUES (?, ?, ?, ?, ?)
        """, (
            nome.value,
            int(minutos.value) if minutos.value else 0,
            int(segundos.value) if segundos.value else 0,
            int(milesimos.value) if milesimos.value else 0,
            equipe.value
        ))
        con.commit()
        con.close()

        nome.value = ""
        minutos.value = ""
        segundos.value = ""
        milesimos.value = ""
        equipe.value = ""

        atualizar_lista()
        page.update()

    # 🔍 Função para atualizar lista na tela
    def atualizar_lista():
        lista_voltas.controls.clear()

        con = sqlite3.connect("voltas.db")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM voltas")
        dados = cursor.fetchall()
        con.close()

        for linha in dados:
            id, nome_, min_, seg_, mil_, equipe_ = linha
            texto = f"#{id} | {nome_} - {min_}:{seg_}.{mil_} | {equipe_}"
            lista_voltas.controls.append(
                ft.Text(texto, color=ft.Colors.WHITE)
            )

        page.update()

    # 🚀 Botão
    botao = ft.ElevatedButton(
        text="Adicionar Volta",
        on_click=adicionar_volta
    )

    # 🧠 Container do formulário
    container_form = ft.Container(
        content=ft.Column([
            nome,
            ft.Row([minutos, segundos, milesimos]),
            equipe,
            botao
        ]),
        width=400,
        padding=10
    )

    # Layout
    page.add(
        ft.Row([container_form, container_list])
    )

    # Inicializa lista carregando dados do banco
    atualizar_lista()


ft.app(target=main)





