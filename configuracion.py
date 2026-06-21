# Configuraciones principales del las descargas
import os
import sys
import ctypes
from ctypes import wintypes, windll, create_unicode_buffer



AUDIO_QUALITY = "320"
#DOWNLOAD_ROOT = "C:/Users/Asus/Music/Mp3" # el root se detectara automaticamente despues
SLEEP_BETWEEN_DOWNLOADS = 2
MAX_RETRIES = 10

# Plantilla para canción individual (sin número ni subcarpeta automática)
FILE_NAMING_TEMPLATE_SINGLE = "%(title)s.%(ext)s"

# Plantilla para playlist (subcarpeta con nombre de playlist y numeración)
FILE_NAMING_TEMPLATE_PLAYLIST = "%(playlist_title)s/%(playlist_index)02d - %(title)s.%(ext)s"

def configurar_Carpeta_descarga():
    if os.name == 'nt':  # Windows
        try:
             

             CSIDL_MYMUSIC = 13
             buf = create_unicode_buffer(wintypes.MAX_PATH)

             if windll.shell32.SHGetFolderPathW(None, CSIDL_MYMUSIC, None, 0, buf) == 0:
                 ruta = buf.value
                 if ruta and os.path.isdir(ruta):
                     return ruta
        except Exception:
                pass
        print(f"📁 Carpeta de descargas: {DOWNLOAD_ROOT}")
       

def Configurar_Carpeta_Descargas():
    if os.name == 'nt':  # Windows
         CSIDL_MYMUSIC = 13
         buf = create_unicode_buffer(wintypes.MAX_PATH)
         if windll.shell32.SHGetFolderPathW(None, CSIDL_MYMUSIC, None, 0, buf) == 0:
                ruta = buf.value
                if ruta and os.path.isdir(ruta):
                    return ruta
         return os.path.join(os.path.expanduser('~'), 'Music')
    
CARPETA_MUSICA = Configurar_Carpeta_Descargas()
DOWNLOAD_ROOT = os.path.join(CARPETA_MUSICA, 'YouTube_MP3')

# Crear la carpeta si no existe
os.makedirs(DOWNLOAD_ROOT, exist_ok=True)
         

         

