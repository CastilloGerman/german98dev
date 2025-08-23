a = 4
b = 8

base_tri=20
alt_tri= 10  

lado_a=5
lado_b=4
lado_c=3

suma= a+b
resta=a-b
multi=a*b
div=a/b
porcentaje=a%b
exp=a**b

txt = 0

print("a+b=",suma)
print("a-b=",resta)
print("a*b=",multi)
print("a/b=",div)
print("a%b=",porcentaje,"%")
print("a**b=",exp)
print("---------------------------------------------------------------",txt)
#---------------------------------------------------------------
#calcular area de un rectangulo
length=10
width=20
area_rec= length*width
print("Area del rectangulo es:",area_rec)
print("---------------------------------------------------------------",txt)
#---------------------------------------------------------------
#calcular area de un circulo
radio=11
area_circ=3.14*radio**2
print("La superficie del circulo es:",area_circ)
print("---------------------------------------------------------------",txt)
#---------------------------------------------------------------
#calcular peso de un objeto
masa=74
grav=9.81
peso= masa*grav
print("Peso total:",peso,"N")
print("---------------------------------------------------------------",txt)
#---------------------------------------------------------------
#Calcular superficie triagngulo
 
super_tri = 0.5 * base_tri * alt_tri

print("Superficie del triangulo es:",super_tri)
print("---------------------------------------------------------------",txt)
#---------------------------------------------------------------
#Calcular perimetro de triangulo

perimeter = lado_a + lado_b + lado_c
print("el perimetro total del triangulo es:",perimeter)

print("---------------------------------------------------------------",txt)
#SIMBOLOGIA DE COMPARACION DE VALORES

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False
