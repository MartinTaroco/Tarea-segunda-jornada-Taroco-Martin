def cuenta_regresiva(n):
  lista = []    #Crea lista vacia
  m = n + 1    #variable auxiliar  
  for i in range(m):         
    lista.append(i)          #Agregar los numeros naturales hasta el anterior al m
  
  lista.reverse()            #Nueva lista con los números ordenada al reves para poder imprimir uno a uno
  for i in lista:
    print(i)
  def es_par(lista):             
    for i in lista:
      if i % 2 == 0:                    #Si el módulo de la división entre 2 es 0 es par
        print(f"{i} es par")                 
      else:
        print(f"{i} es impar")                
  es_par(lista)            
  
cuenta_regresiva(10)

