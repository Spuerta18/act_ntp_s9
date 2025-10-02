import numpy as np
import pandas as pd

def ejercicio_09():
    # Crear un array de NumPy 2D con datos de ventas trimestrales
    ventas = np.array([
        [1500, 2000, 2500],
        [1800, 2200, 2600],
        [1700, 2100, 2400]
    ])

    # Crear el DataFrame con nombres de columnas
    df = pd.DataFrame(ventas, columns=['Q1', 'Q2', 'Q3'])

    # Mostrar el DataFrame
    print("DataFrame de ventas trimestrales:")
    print(df)

    # Verificar tipos de datos
    print("\nTipos de datos en el DataFrame:")
    print(df.dtypes)


if __name__ == "__main__":
    ejercicio_09()
