import flet as ft
import ui.selection as selection
import data as dt

def main(page: ft.Page):
    page.title = "¿Quieres una galleta que alegre tu día?"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 500
    page.window_height = 700
    page.window_center()
    
    def show_menu(e):
        page.views.clear()
        page.views.append(
            ft.View(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Text("¿Quieres una galleta que alegre tu día?", size=18, weight="bold", color="#4C322E"),
                            ft.Text("Cuéntanos un poco de tus preferencias más dulces! y así, podremos brindar la mejor galleta para ti", size=12, color="#4C322E"),
                            ft.Text("Selecciona las opciones que más te gusten", size=12, color="#4C322E"),
                            selection.card1,
                            selection.card2,
                            selection.card3,
                            selection.card4,
                            selection.card5,
                            selection.card6,
                            selection.card7,
                            selection.card8,
                            selection.card9,
                            selection.card10,
                            ft.ElevatedButton(text="Terminar y seleccionar", bgcolor="#4C322E", color="white", on_click=show_cookie),
                            ft.Text("Habla con nosotros en nuestro chat", size=12, color="#4C322E"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=5,
                        scroll=ft.ScrollMode.ADAPTIVE
                    )
                ]
            )
        )
        page.update()
    
    def show_cookie(e):
        selected_options = selection.show_selection(e)
        galletas = dt.seleccionar_galletas(selected_options)
        
        if not selected_options:
            page.views.clear()
            page.views.append(
                ft.View(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text("¡Ups!", size=24, weight="bold", color="#4C322E"),
                                ft.Text("Por favor, selecciona al menos una opción para poder recomendarte una galleta", size=16, color="#4C322E"),
                                ft.ElevatedButton(text="Volver a intentar", bgcolor="#4C322E", color="white", on_click=show_menu),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=10,
                        )
                    ]
                )
            )
            page.update()
        
        elif not galletas:
            page.views.clear()
            page.views.append(
                ft.View(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text("¡Lo sentimos!", size=24, weight="bold", color="#4C322E"),
                                ft.Text("No encontramos una galleta que se ajuste a tus gustos", size=16, color="#4C322E"),
                                ft.Text("¡Inténtalo de nuevo!", size=16, color="#4C322E"),
                                ft.ElevatedButton(text="Volver a intentar", bgcolor="#4C322E", color="white", on_click=show_menu),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=10,
                        )
                    ]
                )
            )
            page.update()
        else:
            galletas_mostrar = [ft.Text(galleta, size=20, weight="bold", color="#4C322E") for galleta in galletas]

            page.views.clear()
            page.views.append(
                ft.View(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text("TU GALLETA IDEAL ES...", size=24, weight="bold", color="#4C322E"),
                                ft.Image("galletas.png", width=300, height=300),
                                ft.Text("Gracias a nuestro algoritmo, las galletas que podrias probar son:", size=16, color="#4C322E"),
                                ft.Card(
                                    content=ft.Column(
                                        controls=galletas_mostrar,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        spacing=10,
                                    ),
                                    elevation=2,
                                    color="#D8B4A0"
                                ),
                                ft.Text("¡Disfruta de tu galleta!", size=16, color="#4C322E"),
                                ft.ElevatedButton(text="Volver a intentar", bgcolor="#4C322E", color="white", on_click=show_menu),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=10,
                        )
                    ]
                )
            )
            page.update()
    
    def show_start(e):
        page.views.clear()
        page.views.append(
            ft.View(controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Image("inicio.png", width=850, height=500),
                        ],
                    ),
                    
                ),
                ft.Container(
                    content=ft.ElevatedButton("INGRESAR", on_click=show_menu, color="#fbf6fe", bgcolor="#d78486"),
                    alignment=ft.alignment.center,
                )
            ])
        )
                
        page.update()
    
    show_start(e=None)

ft.app(target=main)