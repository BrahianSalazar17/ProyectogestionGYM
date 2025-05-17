class Persona:
    def __init__(self, id_persona, nombre, correo, telefono, direccion):
        self.id_persona = id_persona
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion

    def actualizarDatos(self, nuevosDatos: dict) -> bool:
        if not nuevosDatos:
            return False  # No hay datos para actualizar
        
        # Actualizar solo los atributos 
        if 'nombre' in nuevosDatos:
            self.nombre = nuevosDatos['nombre']
        if 'correo' in nuevosDatos:
            self.correo = nuevosDatos['correo']
        if 'telefono' in nuevosDatos:
            self.telefono = nuevosDatos['telefono']
        if 'direccion' in nuevosDatos:
            self.direccion = nuevosDatos['direccion']
        
        return True
