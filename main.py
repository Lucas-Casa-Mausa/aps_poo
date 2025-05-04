from datetime import datetime
from hotel import Hotel
from quarto import TipoQuarto, QuartoBasico, QuartoSuite
from hospede import Hospede

def mostra_menu():
    print("\n=== MENU DO HOTEL ===")
    print("1. Listar quartos disponíveis")
    print("2. Fazer reserva")
    print("3. Cancelar reserva")
    print("4. Cadastrar novo quarto")
    print("5. Cadastrar hóspede")
    print("6. Sair")

def ler_data(mensagem: str) -> datetime:
    while True:
        data_str = input(mensagem).strip()
        try:
            return datetime.strptime(data_str, "%d/%m/%Y")
        except ValueError:
            print(f"Formato inválido! Use DD/MM/AAAA. Exemplo: 20/10/2024")

def main():
    hotel = Hotel('Hotel Plaza')

    hotel.adicionar_quarto(QuartoBasico(101, 200.0, tem_frigobar=True))
    hotel.adicionar_quarto(QuartoSuite(201, 500.0, taxa_servico=100.0))

    while True:
        mostra_menu()
        opcao = input('Escolha uma opção:').strip()

        if opcao == "1":
            print("\n--- QUARTOS DISPONÍVEIS ---")
            tipo = input("Filtrar por tipo (BASICO/SUITE/LUXO) ou deixe em branco: ").upper()
            try:
                tipo_quarto = TipoQuarto[tipo] if tipo else None
            except KeyError:
                print("Tipo inválido! Listando todos.")
                tipo_quarto = None

            quartos = hotel.buscar_quartos_disponiveis(tipo_quarto)
            for quarto in quartos:
                print(quarto)

        elif opcao == "2":
            try:
                print("\n--- NOVA RESERVA ---")
                quarto_num = int(input("Número do quarto: "))
                data_inicio = ler_data("Data de início (DD/MM/AAAA): ")
                data_fim = ler_data("Data de fim (DD/MM/AAAA): ")

                reserva = hotel.fazer_reserva(quarto_num, data_inicio, data_fim)
                print(f"\n✅ Reserva #{reserva.id} confirmada!")
                print(f"Valor total: R${reserva.calcular_valor_total():.2f}")

            except Exception as e:
                print(f"\n❌ Erro: {e}")

        elif opcao == "3":
            try:
                print("\n--- CANCELAR RESERVA ---")
                id_reserva = int(input("ID da reserva: "))
                hotel.cancelar_reserva(id_reserva)
                print("\n✅ Reserva cancelada!")

            except Exception as e:
                print(f"\n❌ Erro: {e}")


        elif opcao == "4":
            try:
                print("\n--- CADASTRAR QUARTO ---")
                numero = int(input("Número do quarto: "))
                tipo = input("Tipo (BASICO/SUITE): ").upper()
                preco = float(input("Preço da diária: R$"))

                if tipo == "BASICO":
                    frigobar = input("Tem frigobar? (S/N): ").upper() == "S"
                    quarto = QuartoBasico(numero, preco, frigobar)
                elif tipo == "SUITE":
                    taxa = float(input("Taxa de serviço: R$"))
                    quarto = QuartoSuite(numero, preco, taxa)
                else:
                    print("Tipo inválido!")
                    continue

                hotel.adicionar_quarto(quarto)
                print("\n✅ Quarto cadastrado!")

            except Exception as e:
                print(f"\n❌ Erro: {e}")

        elif opcao == "5":
            print("\n--- CADASTRAR HÓSPEDE ---")
            nome = input("Nome: ")
            documento = input("Documento: ")
            hospede = Hospede(nome, documento)
            print(f"\n✅ Hóspede {nome} cadastrado!")

        # Opção 6: Sair
        elif opcao == "6":
            print("\nAté logo! 👋")
            break

        else:
            print("\n❌ Opção inválida!")

if __name__ == "__main__":
    main()
