a=input("Primer numero= ")
b=input("Segundo numero= ")
c=raw_input("Escribe S si quieres sumar, R resta, M multiplicacion o D para una division: ")

if c is "S":
    print a+b
if c is "R":
    print a-b
if c is "M":
    print a*b
if c is "D":
    print a/b
