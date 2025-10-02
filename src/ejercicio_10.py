import requests
import pandas as pd

def ejercicio_10():
    url = "https://playground.mockoon.com/users"

    try:
        # Realizar la petición GET
        response = requests.get(url)

        # Verificar que la respuesta sea exitosa
        if response.status_code == 200:
            # Convertir la respuesta JSON a DataFrame
            df = pd.DataFrame(response.json())

            print("Primeras 5 filas del DataFrame:")
            print(df.head())

            print("\nInformación del DataFrame:")
            print(df.info())
        else:
            print(f"Error: La API respondió con el código {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar a la API.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    ejercicio_10()
