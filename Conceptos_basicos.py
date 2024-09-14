#Print
print("Hola mundo")

#Variables
name="Diego"
last_name="Sanchez"

print(last_name)

#Numeros

num1=20
num2=5

sum=num1+num2
rest=num1-num2
division=num1/num2
diventero=num1//num2
mult=num1*num2
potencia=num1 ** num2

print(potencia)

#Cadenas

name2="Diego 'Alonso' Sanchez"
name3= "Parra"

print('Me llamo: '+name2+' '+name3)
print(f'Me llamo: {name2} {name3}')


#Listas

list = ["Python","Django","React","Vue"]

list[1]="Flutter" #Modificar

list.append("Angular") #Añadir
list.insert(2,"Angular") #Añadir en una ubicacion especifica

print(list)

#Tuplas
list2 = ["Python","Django","React","Vue"]

tupla= ("Python","Django","React","Vue")

#No se puede modificar datos dentro de una tupla

print(tupla)

#Diccionarios

data={'name': 'Diego', 'last_name': 'Sanchez', 'edad':25}

data['city'] = 'Lima'

del data["edad"]

print(data)
print(data['city'])
print(len(data))