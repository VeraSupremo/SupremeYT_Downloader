import yt_dlp
from configuracion import AUDIO_QUALITY, SLEEP_BETWEEN_DOWNLOADS, MAX_RETRIES
from auxiliares import mostrar_progreso_hook
from items_media import Media

class Downloader:
    def __init__(self, item: Media, progress_hooks=None):
        self.item = item
        self.progress_hooks = progress_hooks or []

    def download(self):
        # Opciones base para cualquier descarga
        opciones_base = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': AUDIO_QUALITY,
            },
            { # aqui estara el metadata
                'key': 'FFmpegMetadata',
                'add_metadata': True,
                'add_chapters': False,
            },
            { #aqui estara la portada
                'key': 'EmbedThumbnail',
                'already_have_thumbnail': False,
            }],
            'writethumbnail': True,
            'sleep_interval': SLEEP_BETWEEN_DOWNLOADS,         
            'max_sleep_interval': SLEEP_BETWEEN_DOWNLOADS + 3, 
            'retries': MAX_RETRIES,
            'quiet': False,
            'verbose': True,  
            'progress_hooks': [mostrar_progreso_hook],
            'progress_hooks': self.progress_hooks,
        }

        # Combinar con opciones específicas del item (Single o Playlist)
        opciones = {**opciones_base, **self.item.get_ydl_options()}

        print(f"🔧 Opciones configuradas: {opciones.get('outtmpl', 'No especificada')}")

        try:
            with yt_dlp.YoutubeDL(opciones) as ydl:
                print(f"⬇️  Iniciando descarga: {self.item}")
                ydl.download([self.item.url])
                print("✅ Descarga finalizada.")
                return True
        except Exception as e:
            print(f"❌ Error durante la descarga: {e}")
            return False