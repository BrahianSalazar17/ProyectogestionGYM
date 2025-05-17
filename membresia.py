from datetime import date

class Membresia:
    def __init__(self, id_membresia, tipo: str, costo: float):
        self.id_membresia = id_membresia
        self.tipo = tipo
        self.costo = costo
        self.fecha_inicio = None
        self.fecha_fin = None
        self.estado = "Inactiva"

    def activarMembresia(self, fechaInicio: date, fechaFin: date) -> bool:
        if fechaInicio >= fechaFin:
            return False  # Fechas inválidas
        self.fecha_inicio = fechaInicio
        self.fecha_fin = fechaFin
        self.estado = "Activa"
        return True

    def verificarVencimiento(self, fechaActual: date) -> bool:
        if self.fecha_fin is None:
            return False
        return fechaActual > self.fecha_fin

    def renovarMembresia(self, nuevaFechaFin: date) -> bool:
        if self.fecha_fin is None or nuevaFechaFin <= self.fecha_fin:
            return False  # No se puede renovar con una fecha menor o igual
        self.fecha_fin = nuevaFechaFin
        self.estado = "Activa"
        return True

