def orden_topologico(tareas, lista):
  x = ""
  for i in tareas:
    if i[1][0] == 0:
      lista.append(i[0])
      x = i[1][1]
      break
  for j in range(0, len(tareas)-1):
    if tareas[x-1][1][1] == "" or tareas[x-1][1][1] > len(tareas+1):
      lista.append("Orden interrumpido")
      print("Todas las tareas no pueden ordenarse(faltan tareas previas)")
      print("Las tareas que se pueden realizar en el orden adecuado son las siguientes:")
      break
    else:
      lista.append(tareas[x-1][0])
    x = tareas[x-1][1][1]
  return lista

def runnear():
  tareas = [["barrer",(8, 2)], #1
         ["fregar",(1, 6)], #2
         ["dormir",(5, 11)], #3
         ["cantar",(9, 5)], #4
         ["bailar",(4, 3)], #5
         ["estudiar",(2, 9)], #6
         ["comer",(10, 8)], #7
         ["relajarse",(7, 1)], #8
         ["reflexionar",(6, 4)], #9
         ["trabajar",(0, 7)]] #10
  orden = []
  orden_topologico(tareas, orden)
  print(orden)