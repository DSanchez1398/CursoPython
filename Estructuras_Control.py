#Condicionales

edad=int(input("Introduce tu edad: "))
mes = int(input("Introduce tu mes de nacimiento: "))

if edad >= 18:
    print("Eres mayor de edad")
    if mes==1:
        print("Naciste en ENERO")
elif edad == 16:
    print("Bienvenido")
elif not edad == 16:
    print("Hola")
else:
    print("Eres menor de edad")
    


#Bucle For

numeros=[1, 55, 88, 43, 4, 7, 9, 8, 22]
array=range(0, 20)

for num in numeros:
    print(num)    

tabla= int(input("¿Que tabla quieres ver?: "))
nums=range(0, 11)

for num in nums:
    result = tabla * num
    print(f'{tabla} x {num} = {result}')

#Bucle While

tabla2= int(input('¿QUe tabla quieres ver?'))
count=1

while count <= 20:
    print(f'{tabla} x {count} = {tabla*count}')
    count = count + 1