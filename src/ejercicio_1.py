import pandas as pd

def analizar_ventas_diarias():
    # Crear una Serie con ventas diarias
    ventas = pd.Series([150, 200, 180, 220, 175, 190, 165], 
                       index=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])
    
    # Acceder al valor del índice 3
    valor_indice_3 = ventas[3]
    
    # Calcular el promedio de ventas
    promedio = ventas.mean()
    
    # Ordenar por valores
    ordenadas = ventas.sort_values()
    
    # Mostrar resultados
    print("Ventas diarias:\n", ventas)
    print("\nValor en el índice 3 (Jueves):", valor_indice_3)
    print("\nPromedio de ventas:", promedio)
    print("\nVentas ordenadas por valores:\n", ordenadas)

# Ejecutar la función
if __name__ == "__main__":
    analizar_ventas_diarias()
