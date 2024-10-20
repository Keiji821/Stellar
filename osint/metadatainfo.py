import exifread
import os

# Cambiamos el directorio de trabajo al directorio storage
os.chdir(os.path.expanduser("~/storage/dcim/Mi chica hermosa"))

# Abrimos el archivo de imagen
with open("IMG_20241012_122145_908.jpg", 'rb') as f:
    # Leemos los metadatos
    tags = exifread.process_file(f)

    # Verificamos si hay metadatos
    if tags:
        print("Metadatos encontrados:")
        for tag in tags.keys():
            if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                print(f"{tag}: {tags[tag]}")
    else:
        print("No se encontraron metadatos en la imagen")
