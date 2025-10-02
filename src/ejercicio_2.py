import pandas as pd

def ejercicio_02():
    # Crear la Serie con índices personalizados
    serie = pd.Series([85, 92, 78], index=['Matemáticas', 'Ciencias', 'Historia'])

    # Acceder a un valor específico
    valor_ciencias = serie['Ciencias']
    print("Calificación en Ciencias:", valor_ciencias)

    # Mostrar información básica de la Serie
    print("\nSerie completa:")
    print(serie)

    print("\nInformación de la Serie:")
    print(serie.describe())

    # Calcular estadísticas básicas
    suma = serie.sum()
    promedio = serie.mean()

    print("\nSuma de calificaciones:", suma)
    print("Promedio de calificaciones:", promedio)


if __name__ == "__main__":
    ejercicio_02()
