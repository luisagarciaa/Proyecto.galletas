import flet as ft

def main(page: ft.Page):
    page.title = "TU GALLETA IDEAL ES... "
    
    page.add(
        # Texto de titulo
        ft.Text("TU GALLETA IDEAL ES...",
            color=ft.colors.BLACK,
            weight=ft.FontWeight.BOLD,
            font_family="Berlin Sans FB",
            text_align=ft.TextAlign.CENTER, 
            size=23.6,
            bgcolor="#efe4e1"
            ),
         # Texto explicativo
        ft.Text("Gracias a nuestro sistema operativo , la galleta que debes de probar es:",
            color=ft.colors.BLACK,
            font_family="Bodoni MT", 
            text_align=ft.TextAlign.CENTER, 
            size=11.7
            ),
        # Imagen de galletas
        ft.Image(
            src="imagen.jpg",
            height=100,
            width=100
            ),
        #resultado galleta
        ft.Text("Descripción de la galleta y porque se recomendó (ejemplo: Galleta de Salted caramel y pecan butter crumb. Pues, basándonos en tus elecciones, amas el toque salado en tus dulces preferidos )",
            color=ft.colors.BLACK,
            font_family="Bodoni MT", 
            text_align=ft.TextAlign.CENTER, 
            size=11.7
            ),
        )
    
ft.app(target=main)
