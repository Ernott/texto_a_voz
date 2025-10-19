# 🗣️ Texto a Voz – Conversión de Artículos en Audio

Este repositorio contiene las herramientas, scripts y tutoriales necesarios para convertir artículos web en archivos de audio reproducibles en formato MP3. El proyecto está diseñado para facilitar la transformación de contenido escrito en voz sintetizada, ideal para accesibilidad, consumo en movimiento o distribución de contenido en formato auditivo.

## 🎯 Objetivo del Proyecto

El propósito principal es desarrollar un programa que:

1. Reciba una URL de un artículo.
2. Extraiga el texto del artículo.
3. Procese y limpie el contenido textual (opcional).
4. Convierta el texto en voz utilizando síntesis de voz.
5. Guarde el resultado como un archivo MP3.

## 🧰 Herramientas Utilizadas

Este proyecto se apoya en tres bibliotecas clave de Python:

| Biblioteca    | Función principal                                                               |
| ------------- | ------------------------------------------------------------------------------- |
| `newspaper3k` | Descarga y extracción del texto del artículo desde una URL.                     |
| `nltk`        | Limpieza, tokenización y procesamiento del texto (opcional pero útil).          |
| `gtts`        | Conversión de texto a voz utilizando Google Text-to-Speech y guardado como MP3. |

## 🚀 Instalación

Puedes instalar las dependencias necesarias usando `pip`:

```bash
pip install newspaper3k nltk gtts
```
