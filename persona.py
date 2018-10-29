class Persona:
    nombre =""
    edad = 0
    nacionalidad = ""

    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad


    def saludar(self):
        print("hola mi nombre es ", self.nombre)