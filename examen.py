#!usr/bin/python3
class Estudiante (object):
    def __init__(self, FechaDeIngreso, Cedula, Nombre, Apellido):
        self.FechaDeIngreso=FechaDeIngreso
        self.Cedula=Cedula
        self.Nombre=Nombre
        self.Apellido=Apellido

    def MostrarEstudiante (self):

        print ("El estudiante", self. Nombre + self. Apellido + "Tiene: ")

class Egresado (Estudiante):
    def __Nadie__ (self, AnioDeEgreso, ):
        self.__AnioDeEgreso=AnioDeEgreso
    

class Retirado (Estudiante):
    def LaMayoria (self, FechaDeRetiro, ):
        self.FechaDeRetiro=FechaDeRetiro


class NoGraduado (Estudiante):
    def Todos (self, InscribirMateria, RetirarMateria, MostrarCursosInscritos):
        self.InscribirMateria=InscribirMateria
        self.RetirarMateria=RetirarMateria
        self.MostrarCursosInscritos=MostrarCursosInscritos

KeinerMerlo = NoGraduado ("2019","27736034", "Keiner", "Merlo")
KeinerMerlo.Todos ("Ingles", "Matematica", "Matematica")
KeinerMerlo.MostrarEstudiante ()

