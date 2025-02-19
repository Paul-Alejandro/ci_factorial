"""Módulo que contiene la función factorial
La función factorial calcula el factorial de un número entero positivo."""
def factorial(n):
    """Calcula el factorial de un número n.

    Parámetros:
        n (int): Número entero no negativo.

    Levanta:
        TypeError: Si n no es un entero.
        ValueError: Si n es negativo.

    Retorna:
        int: Factorial de n
    """
    if not isinstance(n, int):
        raise TypeError("El número debe ser un entero")
    if n < 0:
        raise ValueError("El número debe ser positivo")
    if n in (0,1):
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
