import sys
import logging
from datetime import datetime
#configuracion del sistema de logging
logging.basicConfig(
    filename="automation.log", #archivo donde se guardaran los logs
    level=logging.INFO,        #Nivel de severidad minimo (INFO=basico)
    format="%(asctime)s - %(levelname)s - %(message)s", #formato del log
)


def main():
    #validamos que el usuario haya pasado un argumento (nombre)
    if len(sys.argv) < 2:
        print("Uso: python hello_auto.py <tu_nombre>")
        return # si no hay un nombre, terminamos el programa

#Tomamos el nombre desde los argumentos de la consola 
nombre = sys.argv[1]

#registremos un mensaje en el log con el nombre de quien ejecuta
logging.info(f"script ejecutado por: {nombre}")

#creamos el texto que queremos escribir en el archivo
contenido = (
    f"Hola {nombre}, esta es tu primera automatizacion. "
    f"Fecha: {datetime.now()}"
)

#abrimos (o creamos) el archivo 'saludo.txt y escribimos dentro
with open("saludo.txt", "w", encoding="utf-8") as f:
    f.write(contenido)

#mensaje informativo en consola
print("Archivo 'saludo.txt' creado y log registrado.")

#punto de entrada del script (solo de ejecuta si lo llamas directamente)
if __name__ == "__main__":
    main()