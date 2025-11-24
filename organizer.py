from pathlib import Path
import shutil
import sys


# -------------------------------------------------------------
# 1. Obtener la ruta de la carpeta a organizar desde argumentos
# -------------------------------------------------------------
# Si el usuario no pasa un argumento, mostramos cómo usar el script
if len(sys.argv) < 2:
    print("Uso: python organizer.py /ruta/a/la/carpeta")
    sys.exit(1)

# Guardamos la ruta pasada por el usuario
carpeta_objetivo = Path(sys.argv[1])

# Verificamos que la carpeta exista
if not carpeta_objetivo.exists():
    print(f"La carpeta {carpeta_objetivo} no existe.")
    sys.exit(1)


# -------------------------------------------------------------
# 2. Creamos un diccionario donde mapeamos extensiones a carpetas
# -------------------------------------------------------------
categorias = {
    "imagenes": [".jpg", ".jpeg", ".png", ".gif"],
    "documentos": [".pdf", ".docx", ".txt"],
    "excel": [".xlsx", ".csv"],
    "videos": [".mp4", ".mov"],
}

# Carpeta para archivos no categorizados
otros = carpeta_objetivo / "otros"
otros.mkdir(exist_ok=True)


# -------------------------------------------------------------
# 3. Recorremos todos los archivos de la carpeta
# -------------------------------------------------------------
for archivo in carpeta_objetivo.iterdir():

    # Saltamos carpetas para no moverlas
    if archivo.is_dir():
        continue

    # Obtenemos la extensión del archivo (en minúsculas por seguridad)
    extension = archivo.suffix.lower()

    # Buscamos a qué categoría pertenece
    movido = False
    for categoria, extensiones in categorias.items():
        if extension in extensiones:
            destino = carpeta_objetivo / categoria
            destino.mkdir(exist_ok=True)  # Creamos carpeta si no existe
            
            shutil.move(str(archivo), str(destino / archivo.name))
            print(f"Movido: {archivo.name} -> {categoria}")
            movido = True
            break

    # Si no coincide con ninguna categoría → va a "otros"
    if not movido:
        shutil.move(str(archivo), str(otros / archivo.name))
        print(f"Movido: {archivo.name} -> otros")


print("\nOrganización completada exitosamente.")
