import flet as ft

def main(page: ft.Page):
    page.title = "TU GALLETA IDEAL ES... "
    
    imagen=ft.Image(
        src="imagen.jpg", height=100, width=100
    )

    page.add(
        ft.Text("TU GALLETA IDEAL ES...", 
                color=ft.colors.BLACK, 
                weight=ft.FontWeight.BOLD, 
                text_align=ft.TextAlign.CENTER, 
                size=20,
                bgcolor="#efe4e1"
                ),
        imagen,
        ft.CupertinoFilledButton(
            content=ft.Text("hola", color=ft.colors.BLUE_100), 
            opacity_on_click=0.9, 
            on_click=lambda e: 
                print("CupertinoFilledButton clicked!")),
        ft.Text("Gracias a nuestro sistema operativo , la galleta que debes de probar es:",
          color=ft.colors.BLACK,
           weight=ft.FontWeight.BOLD, 
           text_align=ft.TextAlign.CENTER, size=10)
        
                
       
          
        )
    
    

ft.app(target=main)
