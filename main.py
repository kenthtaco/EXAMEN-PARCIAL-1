#CREACION DE UNA CLASE QUE CONTENGA UN METODO Y SU OBJETO IMPRESO EJECUTANDO EL METODO __str__

from Escuela import Escuela 
class Estudiante():
    Nombre   = str
    Apellido = str 
    Cedula   = int 
    Edad     = int    
    Paralelo = int 
    
    def __init__ (self, Nombre, Apellido, Cedula, Edad, Paralelo):
         self.Nombre   = Nombre 
         self.Apellido = Apellido 
         self.Cedula   = Cedula 
         self.Edad     = Edad 
         self.Paralelo = Paralelo
         
        
         
Estudiante = Estudiante("Luis", "Padilla", 1753725074, 10, "B")
print(vars(Estudiante))

#CREACION DE UNA CLASE QUE CONTENGA UN METODO Y SU OBJETO IMPRESO EJECUTANDO EL METODO.

class PadreEstudiante():
    Nombre   = str
    Apellido = str
    Cedula   = str  

    
    def __init__(self, Nombre, Apellido, Edad, Cedula):
       
        self.Nombre   = Nombre
        self.Apellido = Apellido 
        self.Cedula   = Cedula  
        
PadreEstudiante = PadreEstudiante("Rogelio", "Padilla", 35, 173452233)
print(vars(PadreEstudiante))
