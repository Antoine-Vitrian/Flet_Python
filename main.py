import flet as ft
import time

def main(page: ft.Page):
    t = ft.Text(value="EA Formula USA", color="white", size=120)
    page.controls.append(t)
    page.update()

    t = ft.Text(text_align="end", width=1000)
    page.add(t)

    page.add(
        ft.Row(controls=[
            ft.TextField(label="Your name"),
            ft.ElevatedButton(text="Say my name!")
        ])
    )
    cont = 0
    def button_clicked(e):
        if cont <=1:
            page.add(ft.Text("Clicked!"))
            

    page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))

    for i in range(10):
        t.value = f"Step {i}"
        page.update()
        time.sleep(1)

    page.add(
        ft.Row(controls=[
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C")
        ])
    )
    
ft.app(main)