import tkinter as tk
from tkinter import messagebox

def enviar_opinion():
    opinion = entry_opinion.get()
    if opinion:
        messagebox.showinfo("Gracias", "¡Gracias por tu opinión!")
        entry_opinion.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa tu opinión antes de enviar.")

ventana = tk.Tk()
ventana.title("Opinión de Galleta")
ventana.geometry("300x400")
ventana.configure(bg="#f7f3f1")

titulo = tk.Label(ventana, text="Tu opinión es lo más importante!", font=("Helvetica", 16, "bold"), bg="#f7f3f1", fg="#000")
titulo.pack(pady=20)

descripcion = tk.Label(ventana, text="Nuestra base de datos se nutre con las opiniones de los clientes de la pastelería, y así como acabas de vivir una experiencia agradable que te permitió probar la mejor galleta en base a tus gustos, ahora danos tu opinión más sincera de la galleta que acabas de probar y ayúdanos a brindarle esta misma experiencia a un próximo cliente merecedor de una perfecta galleta al estilo Beiked.", wraplength=250, justify="left", bg="#f7f3f1", fg="#000")
descripcion.pack(pady=10)

entry_opinion = tk.Entry(ventana, width=40, borderwidth=2, relief="groove")
entry_opinion.pack(pady=20)

boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_opinion, bg="#d7bdbd", fg="#000", font=("Helvetica", 12, "bold"))
boton_enviar.pack(pady=10)

ventana.mainloop()
