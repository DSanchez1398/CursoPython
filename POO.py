#Importacion
import Coche
from Coche import Coche #Traemos especificamente una clase

coche1= Coche("SEAT","Negro")
coche1.color="Azul"
coche1.encender()
coche_lujo= Coche("BWM", "Plata")

print(f'Marca: {coche1.marca}, Color: {coche1.color}')
print(f'Marca: {coche_lujo.marca}, Color: {coche_lujo.color}')
if coche1.encendido:
    print("El coche esta encendido")
else:
    print("El coche no esta encendido")

print(coche1.marca)
print(coche1.color)