from datetime import date

class Cliente:
    def __init__(self, fechaRegistro=None, estado="", membresia=""):
        self.fechaRegistro = fechaRegistro
        self.estado = estado
        self.membresia = membresia

    def registrarCliente(self, datosCliente: dict) -> bool:
        try:
            self.fechaRegistro = datosCliente.get('fechaRegistro', date.today())
            self.estado = datosCliente.get('estado', "Activo")
            self.membresia = datosCliente.get('membresia', "")
            return True
        except Exception as e:
            print(f"Error al registrar cliente: {e}")
            return False

    def consultarEstadoMembresia(self) -> str:
        return self.estado

