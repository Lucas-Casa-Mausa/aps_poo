from datetime import datetime, timedelta
from quarto import QuartoBasico, QuartoSuite, TipoQuarto
from hotel import Hotel
from hospede import Hospede

hotel = Hotel("Teste Hotel")

quarto1 = QuartoBasico(101, 250.0, tem_frigobar=True)
quarto2 = QuartoSuite(201, 500.0, taxa_servico=100.0)
hotel.adicionar_quarto(quarto1)
hotel.adicionar_quarto(quarto2)

hospede = Hospede("Maria Silva", "987.654.321-00")

data_inicio = datetime(2024, 10, 1)
data_fim = data_inicio + timedelta(days=3)
reserva = hotel.fazer_reserva(201, data_inicio, data_fim)
hospede.adicionar_reserva(reserva)

print("\n--- Quartos disponíveis ---")
for q in hotel.buscar_quartos_disponiveis():
    print(q)

print("\n--- Reserva realizada ---")
print(reserva)
print(f"Valor total: R${reserva.calcular_valor_total():.2f}")

hotel.cancelar_reserva(reserva.id)
print("\n--- Após cancelamento ---")
print(f"Quarto 201 disponível? {'SIM' if quarto2.disponivel else 'NÃO'}")