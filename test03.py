import flet as ft
from datetime import timedelta

def main(page: ft.Page):
    page.title = "Adicionar Tempo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Campos de entrada
    minutos_input = ft.TextField(label="Minutos", width=100, value="0")
    segundos_input = ft.TextField(label="Segundos", width=100, value="0")
    milesimos_input = ft.TextField(label="Milésimos", width=100, value="0")

    resultado = ft.Text(value="Tempo total: 00:00.000", size=20)

    def adicionar_tempo(e):
        try:
            minutos = int(minutos_input.value)
            segundos = int(segundos_input.value)
            milesimos = int(milesimos_input.value)

            # Converte para timedelta
            tempo_total = timedelta(
                minutes=minutos,
                seconds=segundos,
                milliseconds=milesimos
            )

            # Formata como mm:ss.mmm
            total_segundos = int(tempo_total.total_seconds())
            milissegundos = int(tempo_total.microseconds / 1000)
            minutos_fmt = total_segundos // 60
            segundos_fmt = total_segundos % 60

            resultado.value = f"Tempo total: {minutos_fmt:02d}:{segundos_fmt:02d}.{milissegundos:03d}"
            page.update()

        except ValueError:
            resultado.value = "Entrada inválida!"
            page.update()

    botao = ft.ElevatedButton("Adicionar", on_click=adicionar_tempo)

    page.add(
        ft.Row([minutos_input, segundos_input, milesimos_input, botao], alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(),
        resultado
    )

ft.app(target=main)



