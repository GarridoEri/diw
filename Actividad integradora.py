lst = []
for i in range(5):
    lst.append(int(input("Introduce un número: ")))
    
def suma(lst):
    total_suma = 0
    for numero in lst:
        total_suma = total_suma + numero
    return total_suma
suma_total = suma(lst)
print("el resultado de la suma es: ", suma_total)

def prom(lst):
    promedio=0
    contador=0

    for i in range(len(lst)):
        promedio=promedio+lst[i]
        contador=promedio/len(lst)
    return contador
promedio = prom(lst)
print("el promedio de los numeros es: ", promedio)

def maximo(lst):
    max=lst[0]
    for numero in lst:
        if numero>max:
            max=numero
    return max
max = maximo(lst)
print("el maximo es: ", max)

def minimo(lst):
    min=lst[0]
    for numero in lst:
        if numero<min:
            min=numero
    return min
min = minimo(lst)
print("el minimo es: ", min)

