import sys
sys.path.insert(1, './ejercicios')
from ejercicios import iniciar, ejecutar, activar

def run():
  if __name__ == "__main__":
    inicio = int(input("Elige el ejercicio a realizar(1=Ordenar por Dicotomía,2=Ordenación topológica,3=Especificaciones): "))
    if inicio == 1 or inicio == 2 or inicio == 3:
      if inicio == 1:
        ejecutar()
      elif inicio == 2:
        activar()
      elif inicio == 3:
        iniciar()
    else:
      print("Has elegido salir o no has introducido correctamente el número del ejercicio.")
run()