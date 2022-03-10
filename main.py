import sys
sys.path.insert(1, './ejercicios')
from ejercicios import O_insercionD, O_especificaciones, O_topologica

def ejecutar():
  if __name__ == "__main__":
    inicio = int(input("Elige el ejercicio a realizar(1=Ordenar por Dicotomía,2=Ordenación topológica,3=Especificaciones): "))
    if inicio == 1 or inicio == 2 or inicio == 3:
      if inicio == 1:
        O_insercionD.Ordenar().iniciar()
      elif inicio == 2:
        O_especificaciones.Especificaciones().iniciar()
      elif inicio == 3:
        O_topologica.Topologia().iniciar()
    else:
      print("Has elegido salir o no has introducido correctamente el número del ejercicio.")

ejecutar()