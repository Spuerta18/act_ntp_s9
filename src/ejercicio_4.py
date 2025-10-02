import pandas as pd

def ejercicio_04():
    # Crear un diccionario con datos de productos
    productos = {
        "Producto": ["Laptop", "Smartphone", "Tablet"],
        "Precio": [3500, 2000, 1500],
        "Categoria": ["Electrónica", "Electrónica", "Electrónica"]
    }

    # Convertir el diccionario a DataFrame
    df = pd.DataFrame(productos)

    # Mostrar el DataFrame completo
    print("DataFrame de productos:")
    print(df)

    # Acceder a una columna específica
    print("\nColumna de precios:")
    print(df["Precio"])

    # Mostrar información básica del DataFrame
    print("\nInformación del DataFrame:")
    print(df.info())


if __name__ == "__main__":
    ejercicio_04()
