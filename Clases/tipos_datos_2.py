# tipos_datos_python.py

"""
Este archivo explica los tipos de datos en Python,
clasificándolos en dos grandes categorías:

1. Tipos de datos simples o primitivos
2. Tipos de datos compuestos

Cada sección incluye ejemplos y explicaciones en comentarios.
"""

# ====================================================
# 1. TIPOS DE DATOS SIMPLES O PRIMITIVOS
# ====================================================

# Entero (int): representa números enteros, positivos o negativos, sin parte decimal.
entero = 42
# float: representa números reales (con punto decimal).
flotante = 3.14159
# bool: representa valores de verdad (True o False).
booleano = True
# str: cadena de caracteres, representada entre comillas simples o dobles.
cadena = "Hola, mundo"

# Ejemplo de uso:
print("Entero:", entero)        # salida: 42
print("Flotante:", flotante)    # salida: 3.14159
print("Booleano:", booleano)    # salida: True
print("Cadena:", cadena)        # salida: Hola, mundo

# También se puede verificar el tipo con la función type():
print(type(entero))     # <class 'int'>
print(type(cadena))     # <class 'str'>


# ====================================================
# 2. TIPOS DE DATOS COMPUESTOS
# ====================================================

# Los tipos compuestos pueden almacenar múltiples valores
# y pueden ser heterogéneos (de distintos tipos).

# Lista (list): colección ordenada y mutable de elementos.
lista = [1, 2, 3, "cuatro", True]

# Tupla (tuple): colección ordenada e inmutable de elementos.
tupla = (10, 20, "treinta")

# Conjunto (set): colección no ordenada de elementos únicos.
conjunto = {1, 2, 3, 2, 1}  # automáticamente elimina duplicados

# Diccionario (dict): colección de pares clave-valor.
diccionario = {"nombre": "Ana", "edad": 30, "activo": True}

# Ejemplo de acceso y operaciones básicas:
print("Lista:", lista)               # salida: [1, 2, 3, 'cuatro', True]
print("Tupla:", tupla)               # salida: (10, 20, 'treinta')
print("Conjunto:", conjunto)         # salida: {1, 2, 3}
print("Diccionario:", diccionario)   # salida: {'nombre': 'Ana', 'edad': 30, 'activo': True}

# Acceso a un valor del diccionario por su clave
print(diccionario["nombre"])         # salida: Ana

# Añadir un valor a la lista
lista.append("nuevo")
print("Lista modificada:", lista)

# Verificación de tipos compuestos
print(type(lista))        # <class 'list'>
print(type(tupla))        # <class 'tuple'>
print(type(conjunto))     # <class 'set'>
print(type(diccionario))  # <class 'dict'>

# ====================================================
# NOTAS ADICIONALES:
# ====================================================
# - Python es un lenguaje de tipado dinámico: las variables no necesitan
#   declarar su tipo explícitamente.
# - También existen tipos de datos derivados como NoneType, usado para representar
#   la ausencia de valor (None).
# - Existen estructuras de datos personalizadas que se pueden definir con clases.