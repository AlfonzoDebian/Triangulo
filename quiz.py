# Quiz instrucciones condicionales
"""Dados tres números a, b y c, correspondientes a la longitud de los lados de una figura geométrica, determinar si pueden formar los lados de un triángulo."""

print("------------------------------")
print("----- VERIFICAR TRIANGULO ----")
print("------------------------------")


# Input
print("===================================")
a = int(input("Inserte el valor a: "))
b = int(input("Inserte el valor b: "))
c = int(input("Inserte el valor c: "))
print("===================================")

# processing
if a + b <= c:
    r = "No se puede formar un triangulo. "
elif a + c <= b:
    r = "No se puede formar un triagulo. "
elif b + c <= a:
    r = "No se puede formar un dialogo. "
else:
    r = "Se puede formar un triangulo. "
pass

# output

print(r)