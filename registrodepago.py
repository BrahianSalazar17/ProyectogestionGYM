from datetime import date
from typing import List

class RegistroPago:
    _pagos: List["RegistroPago"] = []

    def __init__(self, id_registro_pago: int, id_cliente: int, monto: float, fecha_pago: date, tipo_pago):
        self.id_registro_pago = id_registro_pago
        self.id_cliente = id_cliente
        self.monto = monto
        self.fecha_pago = fecha_pago
        self.tipo_pago = tipo_pago
        self.id_membresia = None

    def registrarPago(self) -> bool:
        if self.monto <= 0 or self.tipo_pago is None:
            return False
        RegistroPago._pagos.append(self)
        return True

    @classmethod
    def consultarPagosCliente(cls, id_cliente: int) -> List["RegistroPago"]:
        return [p for p in cls._pagos if p.id_cliente == id_cliente]

    def asociarPagoMembresia(self, id_membresia: int) -> bool:
        if id_membresia <= 0:
            return False
        self.id_membresia = id_membresia
        return True
