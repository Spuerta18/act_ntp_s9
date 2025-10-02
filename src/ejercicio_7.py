import csv
import pandas as pd

def ejercicio_07():
    nombre_archivo = "cursos.csv"

    # Crear y escribir el archivo CSV
    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        # Escribir encabezados
        escritor.writerow(["curso", "instructor", "duracion"])
        # Escribir filas de datos
        escritor.writerow(["Python Básico", "Carlos Pérez", "30 horas"])
        escritor.writerow(["Análisis de Datos", "Ana Gómez", "40 horas"])
        escritor.writerow(["Machine Learning", "Luis Rodríguez", "50 horas"])

    # Leer el archivo CSV con manejo de errores
    try:
        df = pd.read_csv(nombre_archivo)
        print("DataFrame leído desde CSV:")
        print(df)
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no existe.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    ejercicio_07()
