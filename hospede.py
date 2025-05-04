from typing import List
from reserva import Reserva

class Hospede:
    def __init__(self, nome: str, documento: str):
        self._nome = nome
        self._documento = documento
        self._reservas: List[Reserva] = []

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def documento(self) -> str:
        return self._documento

    def adicionar_reserva(self, reserva: Reserva) -> None:
        self._reservas.append(reserva)

    def listar_reservas(self) -> List[Reserva]:
        return self._reservas

    def __str__(self) -> str:
        return f"Hóspede: {self._nome} | Documento: {self._documento} | Reservas: {len(self._reservas)}"