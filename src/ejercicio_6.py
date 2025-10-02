import pandas as pd

def ejercicio_06():
    # Crear una lista de listas donde cada sublista representa un libro
    datos_libros = [
        ["Cien Años de Soledad", "Gabriel García Márquez", 1967],
        ["Don Quijote de la Mancha", "Miguel de Cervantes", 1605],
        ["La Ciudad y los Perros", "Mario Vargas Llosa", 1963]
    ]

    # Definir nombres de las columnas
    nombres_columnas = ["Titulo", "Autor", "Año"]

    # Crear el DataFrame
    df = pd.DataFrame(datos_libros, columns=nombres_columnas)

    # Mostrar el DataFrame
    print("DataFrame de libros:")
    print(df)

    # Mostrar dimensiones del DataFrame
    print("\nDimensiones del DataFrame (filas, columnas):")
    print(df.shape)


if __name__ == "__main__":
    ejercicio_06()
