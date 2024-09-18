# Boas vindas a loja
print('Bem-vindo a loja de roupas do Matheus Dantas de Souza')
print('_____________________________________________________')


# Construção do menu e layout do mesmo
def modelo():
    while True:
        print("Modelos diponiveis")
        print('_________________________________________')
        print("|MCS - Camiseta Manga Curta Simples     |")
        print("|MLS - Camiseta Manga Longa Simples     |")
        print("|MCE - Camiseta Manga Curta Com Estampa |")
        print("|MLE - Camiseta Manga Longa Com Estampa |")
        print('-----------------------------------------\n')

        camiseta = input("Digite o modelo desejado (MCS/MLS/MCE/MLE): ").upper()

        if camiseta == 'MCS':
            return 'Camiseta Manga Curta Simples', 1.80
        elif camiseta == 'MLS':
            return 'Camiseta Manga Longa Simples', 2.10
        elif camiseta == 'MCE':
            return 'Camiseta Manga Curta Com Estampa', 2.90
        elif camiseta == 'MLE':
            return 'Camiseta Manga Longa Com Estampa', 3.20
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Definindo condições de quantidade
def quantidade():
    while True:
        try:
            quantidade = int(input("Digite o número de camisetas: "))
            if quantidade > 20000:
                print("Número de camisetas excede o máximo permitido de 20000. Tente novamente.")
            elif quantidade < 20:
                return quantidade, 1.0  # Sem desconto
            elif 20 <= quantidade < 200:
                return quantidade, 0.95  # 5% de desconto
            elif 200 <= quantidade < 2000:
                return quantidade, 0.93  # 7% de desconto
            elif 2000 <= quantidade <= 20000:
                return quantidade, 0.88  # 12% de desconto
        except ValueError:
            print("Valor inválido. Por favor, digite um número inteiro.")
def frete():
    while True:
        print(' ')
        print("Escolha o tipo de frete:")
        print("0 - Retirar na fábrica (grátis)")
        print("1 - Transportadora (R$100)")
        print("2 - Sedex (R$200)")
        frete = input("Digite o número correspondente ao tipo de frete: ")

        if frete == '0':
            return 'Retirar na fábrica', 0
        elif frete == '1':
            return 'Transportadora', 100
        elif frete  == '2':
            return 'Sedex', 200
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

def main():
    try:
        modelo_str, preco_unitario = modelo()
        qtd, desconto = quantidade()
        frete_str, custo_frete = frete()

        # Calculando quantidade com desconto
        quantidade_com_desconto = qtd * desconto

        # Calculando preço total
        preco_total = (preco_unitario * quantidade_com_desconto) + custo_frete

        # Exibição do resultado
        print(' ')
        print(f"Total: R$ {preco_total:.2f} (Modelo: {preco_unitario:.2f} * Quantidade(com desconto): {quantidade_com_desconto} + frete: {custo_frete:.2f})")
        print(' ')
        print("Obrigado por comprar na loja do Matheus Dantas de Souza")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
main()
