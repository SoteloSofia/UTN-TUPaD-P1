import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print("Números: ", numeros_aleatorios)
print("Moda: ", moda)
print("Mediana: ", mediana)
print("Media: ", media)

if media > mediana and mediana > moda:
    print("Hay sesgo positivo (a la derecha)")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo (a la izquierda)")
else:
    print("No hay sesgo")
