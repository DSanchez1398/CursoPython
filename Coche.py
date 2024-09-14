class Coche:
    marca = ""
    color = "Blanco"
    __encendido = False
    
    def __init__(self,marca,color):
        self.marca = marca
        self.color = color
    
    def encender(self):
        self.__encendido = True
    
    def get_encendido(self):
        return self.__encendido

#Herencia Multiple
class Coche4x4:
    size_ruedas = 19

#Herencia
class CocheDeportivo(Coche, Coche4x4):
    cv = 60
    
    def __init__(self, marca, color, cv, size_ruedas):
        self.marca = marca
        self.color = color
        self.cv = cv
        self.size_ruedas = size_ruedas