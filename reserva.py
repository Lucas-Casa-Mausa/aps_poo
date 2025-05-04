from quarto import Quarto
from datetime import datetime

class Reserva():
    def __init__(self, id_reserva: int, quarto: Quarto, data_inicio: datetime, data_fim: datetime):
        if data_fim <= data_inicio:
            raise ValueError('A data de fim deve ser posterior à data de inicio.')

        if not quarto.disponivel:
            raise ValueError('Quarto está ocupado.')

        self._id = id_reserva
        self._quarto = quarto
        self._data_inicio = data_inicio
        self._data_fim = data_fim
        self._status = 'Ativa'

        quarto.reservar()

    @property
    def id(self) -> int:
        return self._id

    @property
    def quarto(self) -> Quarto:
        return self._quarto

    @property
    def status(self) -> str:
        return self._status

    def calcular_valor_total(self) -> float:
        dias = (self._data_fim - self._data_inicio).days
        return dias * self._quarto.preco_diaria

    def cancelar(self) -> None:
        self._quarto.liberar()
        self._status = "Cancelada"

    def __str__(self) -> str:
        return (
            f"Reserva #{self._id} | Quarto:{self._quarto.numero} | "
            f"Reservado de:{self._data_inicio.strftime('%d/%m/%Y')} a "
            f"{self._data_fim.strftime('%d/%m/%Y')} | Status:{self._status}"
        )