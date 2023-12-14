#INSTALAR PRIMERO pip install ttkthemes


import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import webbrowser

# Función para abrir el formulario en Google
def abrir_formulario():
    enlace_formulario = "https://docs.google.com/forms/d/1YbNVXMPh-Y7ljloeZ7AhvU7pgwj3t5FLkbHwuJSv0J8/edit"
    webbrowser.open(enlace_formulario)

# Función para abrir la página web
def abrir_pagina_web():
    enlace_web = "https://sirjoseph21.github.io/web/"
    webbrowser.open(enlace_web)

# Crear una instancia de ThemedTk en lugar de Tk
ventana = ThemedTk(theme="arc")

# Establecer el título de la ventana
ventana.title("Violencia de Género")

# Configurar el color de fondo de la ventana
ventana.configure(bg='#fff')

# Crear un frame contenedor con relleno
frame_contenedor = ttk.Frame(ventana, padding=(10, 10))
frame_contenedor.pack(expand=True, fill='both')

# Cargar una imagen y colocarla en un marco con borde sólido
imagen = tk.PhotoImage(file="Logo.png")
marco_imagen = ttk.Frame(frame_contenedor, borderwidth=2, relief="solid")
marco_imagen.grid(row=0, column=0, padx=10, pady=10)
etiqueta_imagen = ttk.Label(marco_imagen, image=imagen)
etiqueta_imagen.pack()

# Crear una etiqueta para el título con un fondo blanco y centrar el texto
etiqueta_titulo = ttk.Label(frame_contenedor, text="Tema: Violencia de Género en contra de la mujer", font=("Arial", 16), background='#fff', justify="center")
etiqueta_titulo.grid(row=1, column=0, pady=10)

# Crear una etiqueta para la información con fondo blanco, centrar el texto y envolver después de 300 píxeles
etiqueta_informacion = ttk.Label(frame_contenedor, text="¡Bienvenidos a una exploración esencial! Adéntrate en nuestra revista digital para descubrir el significado detrás de la violencia de género contra la mujer. Invitamos a todos a conocer más sobre este importante tema, entender sus implicaciones y contribuir a la creación de un futuro donde la igualdad y el respeto sean la norma. Juntos, hagamos que la conciencia sea el primer paso hacia un cambio significativo", font=("Arial", 12),
                                  wraplength=300, background='#fff', justify="center")
etiqueta_informacion.grid(row=2, column=0, pady=10)

# Agregar un separador horizontal en el cuarto row del contenedor
separador = ttk.Separator(frame_contenedor, orient="horizontal")
separador.grid(row=3, column=0, sticky="ew", pady=10)

# Crear botones con comandos asociados y configurar el cursor para indicar interactividad
boton_formulario = ttk.Button(frame_contenedor, text="Abrir Formulario", command=abrir_formulario, cursor="hand2")
boton_formulario.grid(row=4, column=0, pady=10)

boton_web = ttk.Button(frame_contenedor, text="Abrir Página Web", command=abrir_pagina_web, cursor="hand2")
boton_web.grid(row=5, column=0, pady=20)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
