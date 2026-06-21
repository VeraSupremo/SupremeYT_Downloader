# Configuraciones principales del las descargas
import os
import sys
import ctypes
from ctypes import wintypes, windll, create_unicode_buffer



VIDEO_QUALITY_720 = 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720]/best'
VIDEO_QUALITY_MAX = 'bestvideo+bestaudio/best'
SLEEP_BETWEEN_DOWNLOADS = 2
MAX_RETRIES = 10

# Plantilla para EL VIDEO INDIVIDUAL
FILE_NAMING_TEMPLATE_VIDEO = "%(title)s.%(ext)s"

# Plantilla para playlist (subcarpeta con nombre de playlist y numeración)
#FILE_NAMING_TEMPLATE_PLAYLIST = "%(playlist_title)s/%(playlist_index)02d - %(title)s.%(ext)s"

def configurar_Carpeta_descarga_Video():
    if os.name == 'nt':  # Windows
        try:
             CSIDL_MYVIDEO = 14
             buf = create_unicode_buffer(wintypes.MAX_PATH)

             if windll.shell32.SHGetFolderPathW(None, CSIDL_MYVIDEO, None, 0, buf) == 0:
                 ruta = buf.value
                 if ruta and os.path.isdir(ruta):
                     return ruta
        except Exception:
                pass
        print(f"📁 Carpeta de descargas para video: {DOWNLOAD_ROOT_VIDEO}")

    #ACA SE CREARA UN FALLBACK DE PREVENCION
    base = os.path.expanduser('~')
    for nombre in ['Videos', 'Mis Videos', 'My Videos']:
        posible = os.path.join(base, nombre)
        if os.path.isdir(posible):
            return posible
        
    Ultima_Opcion_Dirvid = os.path.join(base,'Videos')
    os.makedirs(Ultima_Opcion_Dirvid,exist_ok=True)
    return Ultima_Opcion_Dirvid



CARPETA_VIDEO = configurar_Carpeta_descarga_Video()
DOWNLOAD_ROOT_VIDEO = os.path.join(CARPETA_VIDEO, 'YouTube_Videos')
# Crear la carpeta si no existe
os.makedirs(DOWNLOAD_ROOT_VIDEO, exist_ok=True)

         

         

