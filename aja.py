import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Text("¿Quieres una galleta que alegre tu día?", size= 30),
        ft.Text("Cuéntanos un poco de tus preferencias más dulces! y así, podremos brindar la mejor galleta para ti"),
        ft.Text("Selecciona las opciones que más te gusten"),
        ft.ElevatedButton(text="Para ti, ¿El kinder bueno es buena opción? ")
    )
ft.app(target = main)
