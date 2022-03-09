import random

def iniciar():
  lista = []:
  longuitud = int(input("Especifica la longuitud de la lista: ")) #n valores de la lista
  n_minimo = int(input("Especifica el mínimo del rango numérico de la lista: ")) #para generar numeros entre 25 y 100 meter 25
  n_maximo = int(input("Especifica el máximo del rango numérico de la lista: ")) #para generar numeros entre 25 y 100 meter 100
  for i in range(longuitud):
    lista.append(int(random.radint(n_minimo, n_maximo)))
  segmento_min
  segmento_max