
'''
Paso 1 - funcion_factorial_1_pasa
def factorial(n):
    return 1  # Retornamos 1 directamente solo para que pase el test

'''

'''
Paso 2 : para el tipo de dato

def factorial(n):
    if not isinstance(n, int):
        raise TypeError("El número debe ser un entero")
    return 1  # Retornamos 1 directamente solo para que pase el test
'''
'''
Paso 3 : para números negativos

def factorial(n):
    if not isinstance(n, int):
        raise TypeError("El número debe ser un entero")
    if n < 0:
        raise ValueError("El número debe ser positivo")
    return 1  # Retornamos 1 directamente solo para que pase el test

'''

def factorial(n):
    if not isinstance(n, int):
        raise TypeError("El número debe ser un entero")
    if n < 0:
        raise ValueError("El número debe ser positivo")
    if n == 0 or n == 1:
        return 1
    
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
