import flet as ft

def main(page: ft.page):
    page.add(
        ft.Text("Tu opinión es lo más importante!"),
        ft.text("Nuestra base de datos se nutre con las opiniones de los clientes de la pastelería, y así como acabas de vivir una experiencia agradable que te permitió probar la mejor galleta en base a tus gustos, ahora danos tu opinión mas sincera de la galleta que acabas de probar y ayúdanos a brindarle esta misma experiencia a un próximo cliente merecedor de una perfecta galleta al estilo Beiked. "),
        ft.ElevatedButton(text="¿Recomendarias esta galleta?"),
        ft.ElevatedButton(text="¿Recomendarias esta galleta a alguien que no le guste empalagarse? "),
        ft.ElevatedButton(text="¿Recomendarias esta galleta a alguien que le guste el chocolate oscuro? "),
        ft.ElevatedButton(text="¿Recomendarias esta galleta a alguien que le guste el chocolate blanco? "),
        
    )