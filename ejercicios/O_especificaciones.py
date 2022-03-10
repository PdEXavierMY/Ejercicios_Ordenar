import random

def craft_lista(l, minimol, maximol, minimos, maximos):
  lista = []
  for i in range(l):
    lista.append(int(random.randint(minimol, maximol)))
  print("Esta es la lista inicial:\n" + str(lista))
  segmento = []
  n_random = int(input("¿Cuantos segmentos quieres formar dentro del segmento?(min 2): "))
  for j in range(n_random):
    if j == 0:
      intervalo1 = minimos
      intervalo2 = int(input("Especifica el limite del rango del " + str((j+1)) + " segmento del segmento: "))
    elif j == n_random-1:
      intervalo1 = intervalo2+1 
      intervalo2 = maximos
    else:
      intervalo1 = intervalo2+1
      intervalo2 = int(input("Especifica el limite del rango del " + str((j+1)) + " segmento del segmento: "))
    subsegmento = []
    for z in range((intervalo1-1), intervalo2):
      subsegmento += [lista[z]]
    segmento += [subsegmento]
  lista.insert((minimos-1), segmento)
  for y in range(minimos, (maximos+1)):
    lista.pop(minimos)
  return lista

def especificaciones(lista, minimos):
  n = 1
  for i in lista[minimos-1]:
    maximo = max(lista[minimos-1][n-1])
    print("El máximo del segmento " + str(n) + " es " + str(maximo))
    print("Ahora trasladaremos el máximo al final del segmento")
    i.remove(maximo)
    i.append(maximo)
    n += 1
  print("Así queda la lista finalmente modificada:\n" + str(lista))
  return lista

def iniciar():
  longuitud = int(input("Especifica la longuitud de la lista: ")) #n valores de la lista
  n_minimo = int(input("Especifica el mínimo del rango numérico de la lista: ")) #para generar numeros entre 25 y 100 meter 25
  n_maximo = int(input("Especifica el máximo del rango numérico de la lista: ")) #para generar numeros entre 25 y 100 meter 100
  segmento_min = int(input("Especifica el mínimo del rango a segmentar de la lista: "))
  segmento_max = int(input("Especifica el máximo del rango a segmentar de la lista: "))
  lista = craft_lista(longuitud, n_minimo, n_maximo, segmento_min, segmento_max)
  print("Esta es la lista inicial ya fragmentada:\n" + str(lista))
  especificaciones(lista, segmento_min)