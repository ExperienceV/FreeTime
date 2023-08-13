from Operators.AdOps.Operations import *
from Operators.BasicOps.Operations import *

print("------------------------------------------")
print("-------------Calculadora------------------")
print("------------------------------------------")

options=input("¿Qué desea hacer?")
  
  #MULTIPLICACION
if options.lower() == "multiplicar" or options.lower() == "multiplicación":
    print("Ingrese los siguientes valores: ")
    a=float(input("Ingrese el multiplicando: "))
    b=float(input("Ingrese el multiplicador: "))
    while True:
        if a == str or b == str:
            print("Haz ingresado un valor incorrecto, intentalo otra vez ")
            a=float(input("Ingrese el multiplicando: "))
            b=float(input("Ingrese el multiplicador: "))
        break
    product=multiplicación(a,b)
    print(f"El producto de su multiplicación es {product}")
  
  
  #DIVISION
if options.lower() == "dividir" or options.lower() == "división":
    print("Ingrese los siguientes valores: ")
    a=float(input("Ingrese el dividendo: "))
    b=float(input("Ingrese el divisor: "))
    while True:
        if a == str or b == str or a == 0 or b == 0:
            print("Haz ingresado un valor incorrecto, intentalo otra vez ")
            a=float(input("Ingrese el dividendo: "))
            b=float(input("Ingrese el divisor: "))
        break
    cociente=división(a,b)
    resto= cociente % 2
    print(f"El cociente de su división es {cociente} y el resto {resto}")
  
  
   #SUMA
if options.lower() == "suma" or options.lower() == "sumar":
    print("Ingrese los siguientes valores: ")
    a=float(input("Ingrese el 1er valor: "))
    b=float(input("Ingrese el 2do valor: "))
    while True:
        if a == str or b == str:
            print("Haz ingresado un valor incorrecto, intentalo otra vez ")
            a=float(input("Ingrese el 1er valor: "))
            b=float(input("Ingrese el 2do valor: "))
        break
    total= sumar(a,b)
    print(f"El total de la suma es {total}")
   

   #RESTA
if options.lower() == "resta" or options.lower() == "restar":
    print("Ingrese los siguientes valores: ")
    a=float(input("Ingrese el 1er valor: "))
    b=float(input("Ingrese el 2do valor: "))
    while True:
        if a == str or b == str:
            print("Haz ingresado un valor incorrecto, intentalo otra vez ")
            a=float(input("Ingrese el 1er valor: "))
            b=float(input("Ingrese el 2do valor: "))
        break
    total= restar(a,b)
    print(f"El total de la resta es {total}")
   
   #EXPONENCIACIÓN
if options.lower() == "exponenciar" or options.lower() == "exponenciación":
    print("Ingrese los siguientes valores: ")
    a=float(input("Ingrese el valor base: "))
    b=float(input("Ingrese el exponente: "))
    while True:
        if a == str or b == str:
            print("Haz ingresado un valor incorrecto, intentalo otra vez ")
            a=float(input("Ingrese el valor base: "))
            b=float(input("Ingrese el exponente: "))
        break
    potencia= Exponentiation(a,b)
    print(f"El la potencia de la exponeciación es {potencia}")
   
   #IntDiv
if options.lower() == "división entera" or options.lower() == "dividir entero":
    print("Ingrese los siguientes valores: ")
    a=float(input("Ingrese el dividendo: "))
    b=float(input("Ingrese el divisor: "))
    while True:
        if a == str or b == str or a == 0 or b == 0:
            print("Haz ingresado un valor incorrecto, intentalo otra vez ")
            a=float(input("Ingrese el dividendo: "))
            b=float(input("Ingrese el divisor: "))
        break
    cociente=IntDiv(a,b)
    resto= cociente % 2
    print(f"El cociente de su división es {cociente} y el resto {resto}")
