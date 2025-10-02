import pandas as pd

def ejercicio_05():
    # Crear una lista de diccionarios con información de empleados
    empleados = [
        {"empleado": "Carlos", "salario": 2500, "departamento": "Ventas"},
        {"empleado": "Ana", "salario": 3000, "departamento": "Marketing"},
        {"empleado": "Luis", "salario": 2800, "departamento": "TI"}
    ]

    # Convertir la lista a DataFrame
    df = pd.DataFrame(empleados)

    # Mostrar el DataFrame completo
    print("DataFrame de empleados:")
    print(df)

    # Acceder a filas específicas usando índices
    print("\nPrimera fila (índice 0):")
    print(df.loc[0])

    print("\nSegunda fila (índice 1):")
    print(df.loc[1])


if __name__ == "__main__":
    ejercicio_05()
