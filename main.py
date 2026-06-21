# esta parte es solo entradas y salidas de la consola

import os

from configuracion import DOWNLOAD_ROOT
from items_media import Single, Playlist,Video
from dowloader import Downloader
from style import Titulo,Error,Exito, Pregunta, Progreso, Rutas, Advertencia

#ACA AGREGAR PROXIMAMENTE UN DEF PARA AGREGAR METADATA
def Limite_canciones_playlist():
  #aca el usuario ingresara el maximo de canciones para su playlist a descargar, si no quiere limitarlo, solo dejara el campo vacio
  while True:
    print(Pregunta("¿QUIERES AGREGAR LIMITE DE CANCIONES A DESCARGAR POR PLAYLIST?"))
    print("Si ese es el caso INGRESA VALOR NUMERICO")
    Entrada = input("SI NO QUIERES LIMITE, DEJA EL CAMPO VACIO: ").strip()
    if Entrada.isdigit():
      limite = int(Entrada)
      if limite > 0:
        return limite
      else:
        print(Advertencia("EL NUMERO DEBE SER MAYOR A CERO"))
    else:
      if Entrada == "":
        return None
      else:
        print(Error("ENTRADA NO VALIDA, POR FAVOR INGRESA UN NUMERO O DEJA EL CAMPO VACIO"))


def crear_item_url(url: str, MaxCanciones: int = None):
 print("creacion item")
 #Factri detectara si es una playlist o una sola cancion, y creara el item correspondiente
 if "playlist?list=" in url or "&list=" in url:
  return Playlist(url, MaxCanciones)
 elif "watch?v=" in url: # esta es la parte mas basica, detecta si es un video individual
  return Single(url)
 else:
  raise ValueError((Error("URL no reconocida. Asegura de que solo sea un video o una playlist de YOUTUBE :D")))



def Limite_calidad_video():
    opciones ={'1': 720, '2': 480, '3': 360}
    # se le consultara al usuario la calidad del video en caso de ser un video
    while True:
        print(Pregunta("¿QUIERES UNA RESOLUCION ESPECIFICA DEL VIDEO?"))
        print("Si ese es el caso INGRESA UNA DE LAS OPCIONES A CONTINUACION")
        print("              1. 720p")
        print("              2. 480p")
        print("              3. 360p")
        EntradaVID = input("SI NO QUIERES LIMITE, DEJA EL CAMPO VACIO (videos mas pesados): ").strip()
        if EntradaVID == "":
           print(Advertencia("DESCARGANDO VIDEO EN LA MEJOR CALIDAD DISPONIBLE"))
           return None #max calidad
        elif EntradaVID in opciones:
            print(Exito(f"DESCARGANDO VIDEO EN CALIDAD {opciones[EntradaVID]}p"))
            return opciones[EntradaVID]
        else:
           print(Error("NO VALIDO, HAGA CASO A LAS INSTRUCCIONES POR FAVOR"))



def main():
 print(Titulo("   Bienvenido al este Programa de Descarga de Musica Por Favor sigue las Instrucciones"))
 print("------------- 1: Selecciona el video que deseas descargar -------------------------------")
 print("------------- 2: Copia y pega la URL del video o playlist de YouTube --------------------")
 print("------------- 2.5: Se recomienda usar enlace de YT.Music para caratulas lindas-----------")
 print("------------- 2.8: Se recomienda usar enlace solo de youtube para videos(no music)-------")
 print("------------- 3: Espera a que se descargue tu musica ------------------------------------")
 print("------------- 4: Disfruta tu musica descargada ------------------------------------------")
 print("-----------------------------------------------------------------------------------------")
 print(Advertencia("              REQUISITOS: TENER FFMPEG INSTALADO"))
 print("SER COMUNISTA Y COMPARTIR TU MUSICA DESCARGADA CON TUS AMIGOS :D")
 print(Rutas(f"📁 Las descargas se guardan en: {DOWNLOAD_ROOT}"))
 print("-----------------------------------------------------------------------------------------")
 while True:
  url = input("📎 Pega el enlace (video o playlist): ").strip()
  print(Progreso("🔍 Analizando URL..."))
  print("----------------------------------------------------------------------------------------")
  print(Pregunta("¿Deseas descargar un video en lugar de una cancion o playlist?"))
  print("      Presiona 'V' para video")
  Tipo = input(" Para una cancion o Playlis presiona Enter ").strip()


  try:
            if Tipo.lower() == 'v':
    # ─── DESCARGA DE VIDEO ───
              calidad = Limite_calidad_video()
              item = Video(url, calidad=calidad)
            else:
    # ─── DESCARGA DE MÚSICA ───
              if "list=" in url:
                  limite = Limite_canciones_playlist()
                  item = crear_item_url(url, limite)
              else:
                  item = crear_item_url(url)
            
            downloader = Downloader(item)
            downloader.download()
            print(Exito("✅ Descarga completada con éxito"))
            print("------------------------------------------------------------------------------------")
            print(Pregunta("¿ Desea descargar mas Canciones o Playlist?"))
            FinalDesition = input(Pregunta(" Si deseas descargar mas Presiona ENTER, sino presiona X: ")).strip().lower()
            if FinalDesition == "X".lower():
              print("Gracias por Usar este Programa, DISFRUTA EL ARTE :3")
              break
            else:
              print(Advertencia("------------- RECUERDA SEGUIR LOS PASOS PARA USAR BIEN EL SISTEMA ---------------"))
              print("------------- 1: Selecciona el video que deseas descargar -----------------------")
              print("------------- 2: Copia y pega la URL del video o playlist de YouTube ------------")
              print("------------- 2.5: Se recomienda usar enlace de YT.Music para caratulas lindas---")
              print("------------- 3: Espera a que se descargue tu musica ----------------------------")
              print("------------- 4: Disfruta tu musica descargada ----------------------------------")
              print("---------------------------------------------------------------------------------")
              print(Advertencia("              REQUISITOS: TENER FFMPEG INSTALADO"))
              print("SER COMUNISTA Y COMPARTIR TU MUSICA DESCARGADA CON TUS AMIGOS :D")
              print(Rutas(f"📁 Las descargas se guardan en: {DOWNLOAD_ROOT}"))
              print("---------------------------------------------------------------------------------")
              print(Progreso("🔄 Reiniciando el programa..."))


          # hasta esta zona se pueden agregar mas cosas
  except Exception as e:
          print(f"❌ Error: {e}")

    




if __name__ == "__main__":
    main()



