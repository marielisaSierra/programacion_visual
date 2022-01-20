lista_mayores = []
lista_menores = []

for i in range(7):

  print("dime tu nombre ")
  nombre = input()
  print("dime tu edad")
  edad = int(input() )

  if (edad >= 18):
    lista_mayores.append(edad)

  else:


   
    lista_menores.append(edad)  
    

      
print("Estos son mayores",lista_mayores)
print("Estos son menores",lista_menores)

