class Ordenar():

  def __init__(self):
    self.lista = ["medium", "adiós", "3", "bebé", "ola", "guerra", "espectro", "5", "sed", "secta", "código", "confusión", "2", "clara"] #lista modificable(o str o int/float)
    self.lista_o = [] #Podrían ordenarse junto a otros elementos

  def ordenarlista(self, lista): #ordena en la propia lista
    for i in range(len(lista)):
      for j in range(i, len(lista)):
        if lista[j] < lista[i]:
          lista[i], lista[j] = lista[j], lista[i]
    return lista
  
  def ordenar_dicotomia(self, lista1, lista2):
    for i in range(1, len(lista1)):
      self.mitad = int((len(lista2)-1)/2) #compara los elementos de la lista con el elemento medio de la nueva lista en la que se apoya para ordenar
      if lista1[i] < lista2[self.mitad]:
        for j in range(self.mitad, -1, -1):
          if j-1 < 0 or (lista1[i] > lista2[j-1]):
            lista2.insert(j, lista1[i])
            break
      elif lista1[i] > lista2[self.mitad]:
        for j in range(self.mitad, (len(lista2))):
          if j+1 > (len(lista2)-1) or (lista1[i] < lista2[j+1]):
            lista2.insert(j+1, lista1[i])
            break
    return lista2
  
  def iniciar(self):
    print("La lista es la siguiente:\n" + str(self.lista))
    self.lista_o.append(self.lista[0])
    sorted(self.lista_o)
    listadico = Ordenar().ordenar_dicotomia(self.lista, self.lista_o)
    print("Así quedaría la lista ordenada usando método sorted:\n" + str(sorted(self.lista)))
    print("Así quedaría la lista ordenada usando solo la propia lista):\n" + str(Ordenar().ordenarlista(self.lista)))
    print("La lista ordenada con la ayuda de otra lista y dicotomía queda igual:\n" + str(listadico))