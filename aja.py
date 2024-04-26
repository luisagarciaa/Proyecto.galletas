import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Text("¿Quieres una galleta que alegre tu día?", size= 30),
        ft.Text("Cuéntanos un poco de tus preferencias más dulces! y así, podremos brindar la mejor galleta para ti"),
        ft.Text("Selecciona las opciones que más te gusten"),
        ft.ElevatedButton(text="¿Te gusta empalagarte?"),
        ft.ElevatedButton(text="¿Te gusta el chocolate blanco?"),
        ft.ElevatedButton(text="¿Te gusta el chocolate oscuro?"),
        ft.ElevatedButton(text="Las nueces, ¿Te gustan?"),
        ft.ElevatedButton(text="¿Te gusta la canela?"),
        ft.ElevatedButton(text="¿Te gustan las galletas oreo?"),
        ft.ElevatedButton(text="¿Te gustan los sabores ácidos?"),
        ft.ElevatedButton(text="Cuando hablamos de dulce, ¿Te gustan los toques de sal?"),
        ft.ElevatedButton(text="¿Te gusta la crema de mani?"),
        ft.Text("Cuando termines de seleccionar tus opciones favoritas, da click aquí", size= 20),
        ft.IconButton( icon=ft.icons.PAUSE_CIRCLE_FILLED_ROUNDED,
                    icon_color="pink600",
                    icon_size=20,
                    tooltip="Pause record"
        )
    )
ft.app(target = main)
