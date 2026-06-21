# Funciones auxiliares, como limpiar etc
# utils.py
import re
import os

def limpiar_nombre_archivo(texto: str) -> str:
    """Elimina caracteres inválidos para nombres de archivo en Windows/Linux/Mac."""
    # Caracteres no permitidos en Windows: \ / : * ? " < > |
    return re.sub(r'[\\/*?:"<>|]', "", texto)

def asegurar_carpeta(ruta: str) -> None:
    """Crea la carpeta si no existe."""
    os.makedirs(ruta, exist_ok=True)

def mostrar_progreso_hook(d):
    """Función de callback para mostrar progreso de descarga (opcional)."""
    if d['status'] == 'downloading':
        # Podrías mostrar porcentaje, velocidad, etc.
        pass