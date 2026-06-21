from logging import root
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pywinstyles
from tkinter.font import Font
import sys
import os

from items_media import Video, Playlist,Single
from dowloader import Downloader


## configuracion de interfaz
ventana = tk.Tk()
ventana.title("SUPREME YT DOWNLOADER")
ventana.geometry("420x320")
ventana.resizable(False, False)
def resource_path(relative_path):
    try:
        
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

ventana.iconbitmap(resource_path("icons/SupremDowloader.ico"))

##estilo = ttk.Style()
##estilo.theme_use('winnative')
##FUENTE = ("MS Sans Serif", 8)
##estilo.configure('TLabel', font=FUENTE, padding=6)
# Fondo sólido clásico (gris plata)
##frame = tk.Frame(ventana, bg="#c0c0c0")
##frame.pack(expand=True, fill="both")


## intento de estilo de windows vista
try:
    pywinstyles.apply_style(ventana, "win7")   # o "mica", "aero"
except Exception:
    pass  # Si falla, queda el estilo clásico
estilo = ttk.Style()
estilo.theme_use('vista')
FUENTE = ("Segoe UI", 8)
estilo.configure('TLabel', font=FUENTE, padding = 6 )# Configura la fuente para los Label
frame = tk.Frame(ventana, bg="#f0f0f0")
frame.pack(expand=True, fill="both")


##estilo.configure('TLabel', font=FUENTE) # Configura la fuente para los Label
url_var = tk.StringVar()
limite_var = tk.StringVar(value="0")  



##----------Funciones de la pestaña----------------
def log_terminal(mensaje):
    
    terminal.insert('end', mensaje + '\n')
    terminal.see('end')
    ventana.update_idletasks()

def hook_terminal(d):
    """Hook que escribe el progreso en la terminal."""
    if d['status'] == 'downloading':
        nombre = d.get('filename', 'Desconocido')
        # Extraer solo el nombre del archivo
        import os
        nombre_corto = os.path.basename(nombre) if nombre != 'Desconocido' else nombre
        porcentaje = d.get('_percent_str', '0%')
        velocidad = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        
        mensaje = f"[{porcentaje}] {velocidad} - ETA: {eta} - {nombre_corto}"
        ventana.after(0, lambda: log_terminal(mensaje))
    
    elif d['status'] == 'finished':
        ventana.after(0, lambda: log_terminal("✅ Archivo descargado... :3"))

def DescargarMusica():
    url = url_var.get().strip()
    if not url:
        messagebox.showerror("Error", "INGRESA URL VALIDA")
        return
    terminal.delete('1.0', 'end')
    log_terminal("=" * 50)
    log_terminal("🎵 INICIANDO DESCARGA")
    log_terminal("=" * 50)
    try:
        limite = None
        texto_limite = limite_var.get().strip()
        if texto_limite.isdigit():
            num = int(texto_limite)
            if num > 0:
                limite = num
        
        if "list=" in url:
            item = Playlist(url, MaxCanciones=limite)
            log_terminal(f"Se identifico una Playlist📋")
        else:
            item = Single(url)
            log_terminal(f"Se identifico una Cancion🎵")
        log_terminal(f"🔗 URL: {url}")
        log_terminal("-" * 50)

        import threading
        def tarea():
            d = Downloader(item, progress_hooks=[hook_terminal])
            resultado = d.download()
            ventana.after(0, lambda: finalizar_descarga(resultado))
        
        threading.Thread(target=tarea, daemon=True).start()
    
    except Exception as e:
        log_terminal(f"❌ ERROR: {e}")
        messagebox.showerror("CUACK", f"❌ ERROR: {e}")


def DescargarVideo():
    url = url_var.get().strip()
    if not url:
        messagebox.showwarning("URL vacía", "PEGA UN ENLACE VALIDO")
        return
    
    terminal.delete('1.0', 'end')
    log_terminal("=" * 50)
    log_terminal("INICIANDO DESCARGA...")
    log_terminal("=" * 50)
    log_terminal(f"🔗 URL: {url}")
    log_terminal("-" * 50)
    
    try:
        item = Video(url, calidad=720)
        
        import threading
        def tarea():
            d = Downloader(item, progress_hooks=[hook_terminal])
            resultado = d.download()
            ventana.after(0, lambda: finalizar_descarga(resultado))
        
        threading.Thread(target=tarea, daemon=True).start()
    
    except Exception as e:
        log_terminal(f"❌ ERROR: {e}")
        messagebox.showerror("Error", f"❌ {e}")

def finalizar_descarga(exito):
    if exito:
        log_terminal("=" * 50)
        log_terminal("✅ DESCARGA COMPLETADA CON ÉXITO :3")
        log_terminal("=" * 50)
        messagebox.showinfo("ESPLENDIDO", "✅ DESCARGA COMPLETADA")
    else:
        log_terminal("❌ Descarga fallida")
        messagebox.showerror("CUACK", "❌ ERROR DURANTE LA DESCARGA")





##----------Interfaz----------------

#  Definir fuentes 
FUENTE_TITULO = ("Segoe UI", 11, "bold")
FUENTE_NORMAL = ("Segoe UI", 9)
FUENTE_BOTON  = ("Segoe UI", 10, "bold")

#aplicar estilo
estilo.configure('TLabel', font=FUENTE_NORMAL, padding=6)
estilo.configure('TButton', font=FUENTE_BOTON, foreground="#267528")
estilo.configure('TEntry', font=FUENTE_NORMAL)


ttk.Label(frame, text="Ingresa Url:", font=FUENTE_TITULO).grid(
    row=0, column=0, sticky='', pady=5
)
entry_url = ttk.Entry(frame, textvariable=url_var, width=50, font=FUENTE_NORMAL)
entry_url.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky='')

# Límite de canciones
ttk.Label(frame, text="Máx. canciones (0 = sin limite):", font=FUENTE_NORMAL).grid(
    row=1, column=0, sticky='w', pady=5
)
entry_limite = ttk.Entry(frame, textvariable=limite_var, width=6, font=FUENTE_NORMAL)
entry_limite.grid(row=1, column=1, sticky='w', padx=5)


boton_musica = ttk.Button(frame, text="Descargar Música (MP3)", command=DescargarMusica, style='TButton')
boton_musica.grid(row=2, column = 0, padx=10, pady=10)  

boton_video = ttk.Button(frame, text="Descargar Video (MP4)", command=DescargarVideo, style='TButton')
boton_video.grid(row=2, column = 2, padx=10, pady=10)
#barra progreso
#progreso = ttk.Progressbar(frame, orient='horizontal', mode='indeterminate')
#progreso.grid(row=3, column=0, columnspan=3, sticky='ew', padx=10, pady=10)

#estado_var = tk.StringVar(value="Esperando...")
#label_estado = ttk.Label(frame, textvariable=estado_var, font=FUENTE)
#label_estado.grid(row=4, column=0, columnspan=3, pady=5)

terminal_frame = tk.LabelFrame(frame,text=" Consola de Descarga ",bg="#c0c0c0",fg="black",
                               font=("MS Sans Serif", 8, "bold"),relief="sunken",bd=2)
terminal_frame.grid(row=3, column=0, columnspan=3, pady=10, padx=5, sticky='nsew')

# Widget de texto
terminal = tk.Text(terminal_frame,height=8,width=70,bg="black",fg="#00FF00",
    font=("Courier New", 8),insertbackground="#00FF00",relief="flat",borderwidth=0)
terminal.pack(side='left', fill='both', expand=True, padx=1, pady=1)

# Scrollbar para la terminal
scrollbar = ttk.Scrollbar(terminal_frame, command=terminal.yview)
scrollbar.pack(side='right', fill='y')
terminal.config(yscrollcommand=scrollbar.set)

# Hacer que la terminal no sea editable por el usuario
terminal.config(state='normal')  # Se puede escribir desde el código

terminal.insert('end', "🎵 SUPREME YT DOWNLOADER - LISTO\n")
terminal.insert('end', "📋 Esperando URL para descargar...\n")


frame.rowconfigure(3, weight=1)

# Configurar expansión de columnas
frame.columnconfigure(1, weight=1)   # la columna del entry se estira

entry_url.bind('<Return>', lambda event: DescargarMusica())

ventana.mainloop()