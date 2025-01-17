from yt_dlp import YoutubeDL

# URL do vídeo
url = "https://www.youtube.com/watch?v=9Azyhn2UUyw"

# Configurações para o download
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # Melhor qualidade de vídeo e áudio
    'outtmpl': 'videos/video.mp4',         # Nome e diretório do arquivo
}

# Realizar o download
with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download concluído!")
