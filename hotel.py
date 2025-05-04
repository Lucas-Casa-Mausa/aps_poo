from typing import Dict, List
from quarto import Quarto, TipoQuarto
from reserva import Reserva
from datetime import datetime

class Hotel:

    def __init__(self, nome: str):
        self._nome = nome
        self._quartos: Dict[int, Quarto] = {}
        self._reservas: Dict[int, Reserva] = {}

    def adicionar_quarto(self, quarto: Quarto) -> None:
        if quarto.numero in self._quartos:
            raise ValueError('Quarto já existente.')
        self._quartos[quarto.numero] = quarto

    def buscar_quartos_disponiveis(self, tipo: TipoQuarto = None) -> List[Quarto]:
        return [q for q in self._quartos.values()
                if q.disponivel and (tipo is None or q.tipo == tipo)]

    def fazer_reserva(self, quarto_num: int, data_inicio: datetime, data_fim: datetime) -> Reserva:
        quarto = self._quartos.get(quarto_num)
        if not quarto:
            raise ValueError('Quarto não encontrado.')

        for reserva in self._reservas.values():
            if reserva.quarto.numero == quarto_num and not (
                data_fim <= reserva.data_inicio or data_inicio >= reserva.data_fim
            ):
                raise ValueError("Período já reservado para este quarto.")

        nova_reserva = Reserva(
            id_reserva=len(self._reservas) + 1,
            quarto=quarto,
            data_inicio=data_inicio,
            data_fim=data_fim
        )

        self._reservas[nova_reserva.id] = nova_reserva
        return nova_reserva

    def cancelar_reserva(self, id_reserva: int) -> None:
        reserva = self._reservas.get(id_reserva)
        if not reserva:
            raise ValueError('Reserva não encontrada.')
        reserva.cancelar()
        del self._reservas[id_reserva]

    def __str__(self) -> str:
        return (
            f"Hotel {self._nome} | Quartos: {len(self._quartos)} | "
            f"Reservas Ativas:{len([r for r in self._reservas.values() if r.status == 'Ativa'])}"
            )