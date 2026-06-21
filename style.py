import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


#   Crear funciones para cada estilo de mensaje, ej error, exito, pregunta, etc


def Titulo(texto: str) -> str:
    return f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}{texto}{Style.RESET_ALL}" #Titulos en blanco brillante

def Error(texto: str) -> str:
    return f"{Fore.LIGHTRED_EX}{Style.BRIGHT}❌ {texto}{Style.RESET_ALL}" #Utilizar principalmente para errores o algo muy muy importante 

def Exito(texto: str) -> str:
    return f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}✅ {texto}{Style.RESET_ALL}" #Utilizar para mensajes de exito

def Pregunta(texto: str) -> str:
    return f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT} {texto}{Style.RESET_ALL}" #Preguntas en azul 

def Progreso(texto: str) -> str:
    return f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}⏳ {texto}{Style.RESET_ALL}" 

def Rutas(texto: str) -> str:
    return f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}📁 {texto}{Style.RESET_ALL}" #Usar para Rutas de archivos
def Advertencia(texto: str) -> str:
    return f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT} {texto}{Style.RESET_ALL}" #utilizar para cosas importantes 