from datetime import datetime
from typing import List, Optional


class RegistroEntrada:

    _historial: List["RegistroEntrada"] = []

    def __init__(
        self,
        id_registro: int,
        id_cliente: int,
        fecha_hora_entrada: Optional[datetime] = None,
        fecha_hora_salida: Optional[datetime] = None,
        estado_entrada: str = "Pendiente",
    ):
        self.id_registro = id_registro
        self.id_cliente = id_cliente
        self.fecha_hora_entrada = fecha_hora_entrada or datetime.now()
        self.fecha_hora_salida = fecha_hora_salida
        self.estado_entrada = estado_entrada

    def validarAcceso(self, fecha_hora_entrada: datetime) -> bool:
        """
        Devuelve True si la hora de entrada está dentro del horario
        permitido (ejemplo: 06:00‑22:00); False en otro caso.
        """
        hora = fecha_hora_entrada.time()
        return datetime.strptime("06:00", "%H:%M").time() <= hora <= datetime.strptime(
            "22:00", "%H:%M"
        ).time()

    def registrarEntrada(self) -> bool:
        """
        Registra la entrada actual en el historial si el acceso es válido.
        """
        if not self.validarAcceso(self.fecha_hora_entrada):
            self.estado_entrada = "Denegado"
            return False

        self.estado_entrada = "Permitido"
        RegistroEntrada._historial.append(self)
        return True

    @classmethod
    def consultarHistorialEntradas(
        cls,
        id_cliente: int,
        fecha_inicio: Optional[datetime] = None,
        fecha_fin: Optional[datetime] = None,
    ) -> List["RegistroEntrada"]:
        """
        Devuelve una lista de registros del cliente en el rango indicado.
        Si no se dan fechas, devuelve todo el historial del cliente.
        """
        resultados = [
            reg
            for reg in cls._historial
            if reg.id_cliente == id_cliente
            and (fecha_inicio is None or reg.fecha_hora_entrada >= fecha_inicio)
            and (fecha_fin is None or reg.fecha_hora_entrada <= fecha_fin)
        ]
        return resultados
