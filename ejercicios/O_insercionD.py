def ordenar_dicotomia(n, m, lista1, lista2):
  if n < len(lista1):
    if lista1[n] < lista2[m]:
      if m-1 < 0 or (lista1[n] > lista2[m-1]):
        lista2.insert(m, lista1[n])
      else:
        ordenar_dicotomia(n, m-1, lista1, lista2)
    elif lista1[n] > lista2[m]:
      if m+1 > (len(lista2)-1) or (lista1[n] < lista2[m+1]):
        lista2.insert(m+1, lista1[n])
      else:
        ordenar_dicotomia(n, m+1, lista1, lista2)
    ordenar_dicotomia(n+1, m, lista1, lista2)

def iniciar():
  lista = ["medium", "adiós", "3", "bebé", "ola", "guerra", "espectro", "5", "sed", "secta", "código", "confusión", "2", "clara"]
  lista_o = []
  lista_o.append(lista[0])
  centro = int((len(lista_o)-1)/2)
  ordenar_dicotomia(1, centro, lista, lista_o)
  print(sorted(lista))
  print(str(lista_o))
iniciar()