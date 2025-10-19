from newspaper import Article
from gtts import gTTS

# URL del artículo que quieres analizar
url = 'https://www.3djuegos.com/juegos/no-mans-sky/noticias/este-jugador-no-mans-sky-se-ha-encontrado-frente-a-frente-mismisima-estrella-muerte-imponente-que-le-ha-roto-partida'

# Crear objeto del artículo
articulo = Article(url, language='es')  # Usa 'en' para inglés

# Descarga y analiza 
articulo.download()
articulo.parse()

# Usa el texto extraído en lugar del objeto Article
tts = gTTS(text=articulo.text, lang='es')
tts.save("articulo.mp3")