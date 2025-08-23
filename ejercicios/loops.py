#bucles/loops
#while/mientras

import math

numero = int(input("digite un numero:"))

while numero<0:
    print("Error, ingrese un numero positivo")
    numero = int(input("digite un numero:"))
print(f"\nSu raiz cuadrada es:{(math.sqrt(numero)):.2f}")
          

#-------------------------------------------------------------------------
i=1

while i<=100:
    print(i)
    i += 1

print("fin del programa")
