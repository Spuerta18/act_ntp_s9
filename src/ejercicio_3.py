import pandas as pd

def ejercicio_03():
    # Crear las Series de precios y descuentos
    precios = pd.Series([100, 150, 200])
    descuentos = pd.Series([10, 20, 15])

    print("Precios originales:")
    print(precios)

    print("\nDescuentos:")
    print(descuentos)

    # Operación de resta (elemento por elemento)
    precios_con_descuento = precios - descuentos
    print("\nPrecios después de aplicar descuentos:")
    print(precios_con_descuento)

    # Multiplicar por un escalar (ejemplo: IVA 16%)
    precios_con_iva = precios * 1.16
    print("\nPrecios con IVA (16%):")
    print(precios_con_iva)

    # Mostrar cómo las operaciones son elemento por elemento
    print("\nDemostración elemento por elemento:")
    for i in range(len(precios)):
        print(f"Precio {precios[i]} - Descuento {descuentos[i]} = {precios_con_descuento[i]}")

