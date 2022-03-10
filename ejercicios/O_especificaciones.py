import random

class Especificaciones():

  def craft_lista(self, l, minimol, maximol, minimos, maximos): #crea la lista aleatoria con los segmentos correspondientes
    self.lista = []
    for i in range(l):
      self.lista.append(int(random.randint(minimol, maximol))) #lista aleatoria
    print("Esta es la lista inicial:\n" + str(self.lista))
    self.segmento = []
    self.n_random = int(input("¿Cuantos segmentos quieres formar dentro del segmento?(min 2): "))
    for j in range(self.n_random): #segmentos de la lista
      if j == 0:
        self.intervalo1 = minimos
        self.intervalo2 = int(input("Especifica el limite del rango del " + str((j+1)) + " segmento del segmento: "))
      elif j == self.n_random-1: #último segmento
        self.intervalo1 = self.intervalo2+1
        self.intervalo2 = maximos
      else:
        self.intervalo1 = self.intervalo2+1
        self.intervalo2 = int(input("Especifica el limite del rango del " + str((j+1)) + " segmento del segmento: "))
      self.subsegmento = []
      for z in range((self.intervalo1-1), self.intervalo2): #añade los segmentos
        self.subsegmento += [self.lista[z]]
      self.segmento += [self.subsegmento]
    self.lista.insert((minimos-1), self.segmento)
    for y in range(minimos, (maximos+1)): #elimina los elementos que han sido introducidos al/los segmento/s
      self.lista.pop(minimos)
    return self.lista
  
  def especificaciones(self, lista, minimos):
    self.n = 1
    for i in lista[minimos-1]:
      self.maximo = max(lista[minimos-1][self.n-1])
      print("El máximo del segmento " + str(self.n) + " es " + str(self.maximo))
      print("Ahora trasladaremos el máximo al final del segmento")
      i.remove(self.maximo)
      i.append(self.maximo)
      self.n += 1
    print("Así queda la lista finalmente modificada:\n" + str(lista))
    return lista
  
  def iniciar(self):
    print("Vas a crear una lista, dividirla en 3 partes y segmentar una de esas partes. Para ello, introducza los siguientes valores requeridos:")
    self.longuitud = int(input("Especifica la longuitud de la lista: ")) #n valores de la lista
    self.n_minimo = int(input("Especifica el mínimo del rango numérico de la lista: ")) #para generar numeros entre 25 y 100 meter 25
    self.n_maximo = int(input("Especifica el máximo del rango numérico de la lista: ")) #para generar numeros entre 25 y 100 meter 100
    self.segmento_min = int(input("Especifica el mínimo del rango a segmentar de la lista(>= 1): "))
    self.segmento_max = int(input("Especifica el máximo del rango a segmentar de la lista(<= el maximo introducido antes): "))
    self.lista = Especificaciones().craft_lista(self.longuitud, self.n_minimo, self.n_maximo, self.segmento_min, self.segmento_max)
    print("Esta es la lista inicial ya fragmentada:\n" + str(self.lista))
    Especificaciones().especificaciones(self.lista, self.segmento_min)