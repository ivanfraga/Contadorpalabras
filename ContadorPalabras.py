palabras ={}#creacion del conjunto palabras
def iniciarContador():
  archivo= open('texto.txt','r') #Creacion del archivo en el IDE
  '''lee todo el archivo y lo transforma a string '''
  linea = archivo.readline()
  '''Convierte al string en una lista separandolo en palabras por cada espacio en blanco '''
  lineas = linea.split()
  '''Bucle que no cierra mientras el archivo no finalice'''
  while linea!="":
     '''bucle con extención por cada palabra de la lista líneas'''
     for palabraa in lineas:
      '''si alguna palabra de la lista lineas se encontraba dentro del conjunto palabras'''
      if palabraa in palabras:
        '''Se incrementa un contador, '''
        x=int(palabras[palabraa])
        palabras[palabraa]=x+1
      else:
        palabras[palabraa]=1
     linea = archivo.readline()
     lineas = linea.split()
  archivo.close()

def imprimir():
  for a in palabras:
    num = str(palabras[a])
    print(a+"= "+num)

iniciarContador()
print("Las palabras repetidas son ")
imprimir()
