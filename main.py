def ordenar_normal(lista):
  for i in lista:
    for j in range(len(lista)):
      if i < lista[j]:
        elemento = lista.remove(i)
        lista.insert(j-1, elemento)
        break

lista = ["medium", "adiós", "3", "bebé", "ola", "guerra", "espectro", "5", "sed", "secta", "código", "confusión", "2", "clara"] #lista modificable(o str o int/float)
ordenar_normal(lista)