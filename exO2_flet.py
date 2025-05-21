import flet as ft
import sqlite3
from datetime import timedelta

# 🔗 Função para criar conexão com SQLite e tabela
def criar_banco():
    conn = sqlite3.connect("tempos.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tempos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            minutos INTEGER,
            segundos INTEGER,
            milesimos INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# 🔗 Função para inserir tempo no banco
def salvar_tempo(minutos, segundos, milesimos):
    conn = sqlite3.connect("tempos.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tempos (minutos, segundos, milesimos)
        VALUES (?, ?, ?)
    ''', (minutos, segundos, milesimos))
    conn.commit()
    conn.close()

# 🔗 Função para listar tempos do banco
def listar_tempos():
    conn = sqlite3.connect("tempos.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tempos')
    dados = cursor.fetchall()
    conn.close()
    return dados


# 🖥️ Interface Flet
def main(page: ft.Page):
    page.title = "Adicionar Tempo com SQLite"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    criar_banco()

    # Campos de entrada
    minutos_input = ft.TextField(label="Minutos", width=100, value="0")
    segundos_input = ft.TextField(label="Segundos", width=100, value="0")
    milesimos_input = ft.TextField(label="Milésimos", width=100, value="0")

    resultado = ft.Text(value="Tempo total: 00:00.000", size=20)
    lista_tempos = ft.Column()

    # 🔄 Atualizar lista na interface
    def atualizar_lista():
        lista_tempos.controls.clear()
        dados = listar_tempos()
        for d in dados:
            tempo = timedelta(
                minutes=d[1],
                seconds=d[2],
                milliseconds=d[3]
            )
            total_segundos = int(tempo.total_seconds())
            milissegundos = int(tempo.microseconds / 1000)
            minutos_fmt = total_segundos // 60
            segundos_fmt = total_segundos % 60

            texto = f"{minutos_fmt:02d}:{segundos_fmt:02d}.{milissegundos:03d}"
            lista_tempos.controls.append(
                ft.Text(f"ID {d[0]} → {texto}")
            )
        page.update()

    # ▶️ Ação do botão
    def adicionar_tempo(e):
        try:
            minutos = int(minutos_input.value)
            segundos = int(segundos_input.value)
            milesimos = int(milesimos_input.value)

            tempo_total = timedelta(
                minutes=minutos,
                seconds=segundos,
                milliseconds=milesimos
            )

            total_segundos = int(tempo_total.total_seconds())
            milissegundos = int(tempo_total.microseconds / 1000)
            minutos_fmt = total_segundos // 60
            segundos_fmt = total_segundos % 60

            resultado.value = f"Tempo total: {minutos_fmt:02d}:{segundos_fmt:02d}.{milissegundos:03d}"

            # 💾 Salvar no banco
            salvar_tempo(minutos, segundos, milesimos)

            # 🔄 Atualizar lista
            atualizar_lista()

            page.update()

        except ValueError:
            resultado.value = "Entrada inválida!"
            page.update()

    botao = ft.ElevatedButton(
        "Adicionar",
        on_click=adicionar_tempo,
        bgcolor="#4CAF50",
        color="white"
    )

    page.add(
        ft.Row(
            [minutos_input, segundos_input, milesimos_input, botao],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        resultado,
        ft.Divider(),
        ft.Text("Tempos Salvos:", weight=ft.FontWeight.BOLD),
        lista_tempos
    )

    atualizar_lista()

ft.app(target=main)

