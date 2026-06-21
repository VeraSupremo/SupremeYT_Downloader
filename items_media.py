# aca vendran las clases
from abc import ABC, abstractmethod
from configuracion import DOWNLOAD_ROOT,FILE_NAMING_TEMPLATE_SINGLE, FILE_NAMING_TEMPLATE_PLAYLIST
from configuracionvideo import DOWNLOAD_ROOT_VIDEO, FILE_NAMING_TEMPLATE_VIDEO, VIDEO_QUALITY_720, MAX_RETRIES, SLEEP_BETWEEN_DOWNLOADS, VIDEO_QUALITY_MAX
#true
class Media(ABC):
    # esta clase es la clase padre de todas las clases de medios, como canciones, videos
    def __init__(self, url: str):
        self.url = url
        # A continuacion de atributos que llenara el extractor 
        self.title = None
        self.uploader = None
        self.duration = None

    @abstractmethod
    def get_ydl_options(self) -> dict:
        # esta funcion tiene un diccionario como valor de retorno,
        #  es la que devuelve las opciones para el extractor, dependiendo del tipo de medio
        pass
    def __str__(self):
        return f"{self.__class__.__name__}: {self.url}"
    

# ahora vendran las clases hijos 
class Single(Media):
    #solo vera una cancion solita
    def get_ydl_options(self) -> dict:
        return{
            'outtmpl': f"{DOWNLOAD_ROOT}/{FILE_NAMING_TEMPLATE_SINGLE}",
            'ignoreerrors': False,
        }
    
class Playlist(Media):
    MaxCanciones = None
    # esta clase es para las playlist, que pueden tener varias canciones, y se guardaran en una subcarpeta con el nombre de la playlist
    def __init__(self, url: str, MaxCanciones: int = None): # max canciones se definira despues como proeunta al usuario ojala
        super().__init__(url)
        self.video_count = 0   # Se puede obtener durante la extracción
        self.current_index = 0 # servira para una barra mas visual
        self.MaxCanciones = MaxCanciones


 
    def get_ydl_options(self) -> dict:
        opciones = {
            'outtmpl': f"{DOWNLOAD_ROOT}/{FILE_NAMING_TEMPLATE_PLAYLIST}",
            'ignoreerrors': True,  # Mejor True para playlists
            'playliststart': 1,
        }
        if self.MaxCanciones is not None:
            opciones['playlistend'] = self.MaxCanciones
        # Si no hay límite, NO pongas 'playlistend' y descargará todo
        return opciones
        

class Video(Media):
    #Utiliza esta clase por si deseas descargar videos, es importante recordad
    #que la opcion de video la elegira el usuario al iniciar el programa
    def __init__(self, url: str, calidad: int = None):
        super().__init__(url)
        self.calidad = calidad

    def get_ydl_options(self, Vid_Res_User: int = None) -> dict:
        if self.calidad is not None:
            # Limita a la altura indicada, preferentemente mp4
            formato = (
                f'bestvideo[height<={self.calidad}][ext=mp4]+bestaudio[ext=m4a]'
                f'/bestvideo[height<={self.calidad}][ext=mp4]+bestaudio[ext=mp4]'
                f'/best[height<={self.calidad}][ext=mp4]'
                f'/bestvideo[height<={self.calidad}]+bestaudio[ext=m4a]'
                f'/best[height<={self.calidad}]'
                f'/best'
            )
        else:
            # Sin límite: la mejor calidad disponible
            formato = (
                'bestvideo[ext=mp4]+bestaudio[ext=m4a]'
                '/bestvideo[ext=mp4]+bestaudio[ext=mp4]'
                '/best[ext=mp4]'
                '/bestvideo+bestaudio[ext=m4a]'
                '/best'
            )
          ##  formato = VIDEO_QUALITY_MAX  # o VIDEO_QUALITY_720 si quieres un default

        return {
            'outtmpl': f"{DOWNLOAD_ROOT_VIDEO}/{FILE_NAMING_TEMPLATE_VIDEO}",
            'format': formato,
            'merge_output_format': 'mp4',
            'ignoreerrors': False,
            'writethumbnail': False,
            # a continuacion video tendra su propio postprocesado
            'postprocessors': [
                {'key': 'FFmpegMetadata', 'add_metadata': True, 'add_chapters': False}
            ],
        }
    