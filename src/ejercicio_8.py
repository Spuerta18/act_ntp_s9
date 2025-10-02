import json
import pandas as pd

def ejercicio_08():
    nombre_archivo = "vehiculos.json"

    # Lista de diccionarios que representan vehículos
    vehiculos = [
        {"marca": "Toyota", "modelo": "Corolla", "año": 2020},
        {"marca": "Ford", "modelo": "Focus", "año": 2018},
        {"marca": "Chevrolet", "modelo": "Onix", "año": 2021}
    ]

    # Guardar la lista como archivo JSON
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(vehiculos, archivo, ensure_ascii=False, indent=4)

    # Leer el archivo JSON con manejo de errores
    try:
        df = pd.read_json(nombre_archivo)
        print("DataFrame leído desde JSON:")
        print(df)

        # Mostrar los tipos de datos de cada columna
        print("\nTipos de datos de cada columna:")
        print(df.dtypes)

    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no existe.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    ejercicio_08()
