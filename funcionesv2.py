print("Más sobre funciones")
# Aquí se escriben las funciones
def suma_ab(a,b):
    s= a + b
    return s
def resta_ab(a,b):
    r= a - b
    return r
def multi_ab(a,b):
    m= a * b
    return m
def div_ab(a,b):
    d= a / b
    return d
    
# Llamadas a función
print("---Calculando suma---")
n1=int(input("Ingresa el primer número "))
n2=int(input("Ingresa el segundo número "))
suma=suma_ab(n1,n2)
print(f"La suma de {n1} + {n2} es: {suma}")

print("---Calculando resta---")
v1=int(input("Ingresa el primer número "))
v2=int(input("Ingresa el segundo número "))
resta=resta_ab(v1,v2)
print(f"La resta de {v1} - {v2} es: {resta}")

print("---Calculando multiplicación---")
x1=int(input("Ingresa el primer número "))
x2=int(input("Ingresa el primer número "))
multi=multi_ab(x1,x2)
print(f"La multiplicación de {x1} x {x2} es: {multi}")

print("---Calculando división---")
y1=float(input("Ingresa el primer número "))
y2=float(input("Ingresa el primer número "))
div=div_ab(y1,y2)
print(f"La división de {y1} x {y2} es: {div}")


