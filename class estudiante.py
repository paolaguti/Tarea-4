class estudiante
    def __init__(self, nombre, edad, codigo, carrera):
        try:
            if not nombre or not codigo or not carrera:
                raise ValueError("los campos nombre ,codigo y carrera no
                puedan estar vacios")
            if edad <= 0:
                raise ValueError ("la edad debe ser mayor que cero")
            
            self.nombre = nombre
            self.edad = edad
            self.codigo = codigo
            self.carrera = carrera
        except ValueError as e:
            print (f"error al crear el estudiante: {e}")
            
    def mostrar_datos (self):
        return f"nombre: {self.nombre}, Edad: {self.edad}, codigo: {self.codigo}, carrera: {self.carrera}
    
    def presentarse(self):
        return f"hola, mi nombre es {self.nombre} y estudio {self.carrera}."
