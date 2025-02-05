# estadisticas.py
def media(datos):
    #Este es un ejemplo de documentación, se activa poniendo """+TAB y se escoge args
    """Ésta función calcúla la media aritmética de una lista con valores numéricos.

    Args:
        datos (Lista): Lista de numeros

    Returns:
        Float: Flotante de la media aritmetica
    """
    
    return sum(datos) / len(datos)

def calcular_mediana(datos):
    datos_sorted = sorted(datos)
    n = len(datos)
    mid = n // 2
    if n % 2 == 0:
        return (datos_sorted[mid - 1] + datos_sorted[mid]) / 2.0
    else:
        return datos_sorted[mid]