def ordenar_dicotomia(lista1, lista2):
  for i in range(1, (len(lista1)-1)):
    mitad = int((len(lista2)-1)/2)
    if lista1[i] < lista2[mitad]:
      for j in range(mitad, -1, -1):
        if j-1 < 0 or (lista1[i] > lista2[j-1]):
          lista2.insert(j, lista1[i])
          break
    elif lista1[i] > lista2[mitad]:
      for j in range(mitad, (len(lista2))):
        if j+1 > (len(lista2)-1) or (lista1[i] < lista2[j+1]):
          lista2.insert(j+1, lista1[i])
          break

def iniciar():
  lista = ["medium", "adiós", "3", "bebé", "ola", "guerra", "espectro", "5", "sed", "secta", "código", "confusión", "2", "clara"] #lista modificable(o str o int/float)
  lista_o = [] #lista modificable(o str o int/float)(podrían ponerse elementos adicionales y ordenaría todo junto)
  lista_o.append(lista[0])
  sorted(lista_o)
  ordenar_dicotomia(lista, lista_o)
  print("Así quedaría la lista ordenada usando solo esta(método sorted)" + str(sorted(lista)))
  print("Así quedaría la lista ordenada con la ayuda de otra lista y dicotomía" + str(lista_o))
iniciar()