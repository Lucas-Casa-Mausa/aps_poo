from enum import Enum


class TipoQuarto(Enum):
    BASICO = "Básico"
    SUITE = "Suite"
    LUXO = "Luxo"


class Quarto():

    def __init__(self, numero:int, tipo:str, precoDiaria:float):
        self._numero = numero
        self._tipo = tipo
        self._precoDiaria = precoDiaria
        self._disponivel = True

    def reservar(self) -> None:
        if not self._disponivel:
            raise ValueError("Quarto já está ocupado")
        self._disponivel = False


    def liberar(self) -> None:
        if self._disponivel:
            raise ValueError("Quarto está liberado")
        self._disponivel = True

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def tipo(self) -> str:
        return self._tipo

    @property
    def preco_diaria(self) -> float:
        return self._precoDiaria

    @property
    def disponivel(self) -> bool:
        return self._disponivel

    def __str__(self) -> str:
        return (f'O Quarto {self._numero} ({self._tipo}) -'
                f'R${self._precoDiaria}/Noite | Disponível: {'SIM' if self._disponivel else 'NÃO'}')

class QuartoBasico(Quarto):
    def __init__(self, numero: int, precoDiaria: float, tem_frigobar: bool):
        super().__init__(numero, TipoQuarto.BASICO, precoDiaria)
        self._tem_frigobar = tem_frigobar

    @property
    def tem_frigobar(self) -> bool:
        return self._tem_frigobar

    def __str__(self):
        return f'{super().__str__()} | Frigobar: {'SIM' if self._tem_frigobar else 'NÃO'}'


class QuartoSuite(Quarto):
    def __init__(self, numero: int, precoDiaria: float, taxa_servico: float):
        super().__init__(numero, TipoQuarto.SUITE, precoDiaria)
        self._taxa_servico = taxa_servico

    def calcular_preco_diario(self) -> float:
        return self._precoDiaria + self._taxa_servico

    def __str__(self):
        return (
            f"{super().__str__()} | Taxa de Serviço: R${self._taxa_servico:.2f}"
            )