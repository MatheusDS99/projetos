# Iniciando dando boas vindas e apresentando o nome para o cliente.

print("Bem-vindo(a) à Loja de Marmitas do Matheus Dantas de Souza!")

def menu():
    print("-----"*11)
    print(' '*20 ,"--Menu--", ' '*20)
    print("-----"*11)
    print("| Tamanho      | Bife Acebolado (BA)|Filé de Frango (FF)")
    print("-----"*11)
    print("| P (Pequeno)  | R$ 16.00           | R$ 15.00     |")
    print("| M (Médio)    | R$ 18.00           | R$ 17.00     |")
    print("| G (Grande)   | R$ 22.00           | R$ 21.00     |")
    print("-----"*11)

# menu
menu()

# Acumulador
total_pedidos = 0

while True:
    # Input dos sabores e caso de negação
    sabor = input("Por favor, escolha o sabor (BA/FF): ")
   
    if sabor != "BA" and sabor != "FF":
        print("Sabor inválido. Tente novamente.")
        print('\n')
        continue
    else:
        #Input do tamanho e caso de negação
        tamanho = input("Por favor, escolha o tamanho (P/M/G): ")

        if tamanho != "P" and tamanho != "M" and tamanho != "G":
            print("Tamanho inválido. Tente novamente.")
            continue
        else:
            # Aninhamento
            if sabor == "BA":
                if tamanho == "P":
                    print("Você escolheu uma marmita de Bife Acebolado tamanho P. O valor é R$ 16.00.")
                    total_pedidos += 16
                elif tamanho == "M":
                    print("Você escolheu uma marmita de Bife Acebolado tamanho M. O valor é R$ 18.00.")
                    total_pedidos += 18
                elif tamanho == "G":
                    print("Você escolheu uma marmita de Bife Acebolado tamanho G. O valor é R$ 22.00.")
                    total_pedidos += 22
            elif sabor == "FF":
                if tamanho == "P":
                    print("Você escolheu uma marmita de Filé de Frango tamanho P. O valor é R$ 15.00.")
                    total_pedidos += 15
                elif tamanho == "M":
                    print("Você escolheu uma marmita de Filé de Frango tamanho M. O valor é R$ 17.00.")
                    total_pedidos += 17
                elif tamanho == "G":
                    print("Você escolheu uma marmita de Filé de Frango tamanho G. O valor é R$ 21.00.")
                    total_pedidos += 21
                    print('\n')

    # Dando a possibilidade do cliente prosseguir com o pedido

    continuar = input("Deseja pedir mais alguma coisa? (sim/não): ").strip().lower()
    print('\n')
    if continuar != 'sim':
        
        break
      

# Total acumulado do pedido
print(f"O valor total dos pedidos é R$ {total_pedidos:.2f}\n")
print("Obrigado por comprar em nossa loja!")

