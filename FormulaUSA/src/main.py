import flet as ft
import sqlite3

# --- Cria banco e tabela (caso ainda não exista) ---
def criar_banco():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# --- Insere um nome no banco ---
def inserir_usuario(nome):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome) VALUES (?)", (nome,))
    conn.commit()
    conn.close()

# --- Recupera todos os nomes do banco ---
def listar_usuarios():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM usuarios")
    dados = cursor.fetchall()
    conn.close()
    return dados

# --- Interface Flet ---
def main(page: ft.Page):
    page.title = "Flet + SQLite"
    criar_banco()

    nome_input = ft.TextField(label="Nome", width=300)
    lista_usuarios = ft.Column()

    # Atualiza a lista de nomes
    def atualizar_lista():
        lista_usuarios.controls.clear()
        for nome in listar_usuarios():
            lista_usuarios.controls.append(ft.Text(nome[0]))
        page.update()

    # Ao clicar em "Salvar"
    def salvar_click(e):
        nome = nome_input.value.strip()
        if nome:
            inserir_usuario(nome)
            nome_input.value = ""
            atualizar_lista()

    btn_salvar = ft.ElevatedButton("Salvar", on_click=salvar_click)

    page.add(
        ft.Column(
            controls=[
                nome_input,
                btn_salvar,
                ft.Text("Lista de usuários:"),
                lista_usuarios
            ]
        )
    )

    atualizar_lista()

ft.app(target=main)

