#Nome completo no inicio do código
print("Bem-vindos a loja do Matheus Dantas de Souza")
print('-'*45)

# Implementação do input 'ValordoPedido' e 'QuantidadeParcelas'
valorDoPedido = float(input("Entre com o valor do pedido: "))

 # Para caso de valor nulo, por erro de digitação, por exemplo
if valorDoPedido == 0:
    print("Valor não registrado, encerrando aplicação")
    exit()

quantidadeParcelas = int(input("Entre com a quantidade de parcelas: "))
# Para caso de, por erro de digitação ou interpretar erroneamente, o cliente digite 0 nas parcelas.
if quantidadeParcelas == 0:
    print("Por favor, em caso de não haver parcelas e o pagamento for feito à vista, digite '1'")
    exit()

# Implementação dos juros de acordo com as condições dadas no trabalho 
if quantidadeParcelas < 4:
    juros = 0 / 100
elif 4 <= quantidadeParcelas < 6:
    juros = 4 / 100
elif 6 <= quantidadeParcelas < 9:
    juros = 8 / 100
elif 9 <= quantidadeParcelas < 13:
    juros = 16 / 100
else:
    juros = 32 / 100

# Implementação do cálculo do Valor do Pedido e da Quantidade das Parcelas
valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeParcelas
valorTotalParcelado = valorDaParcela * quantidadeParcelas



# Apresentação do valor das parcelas e valor total parcelado

if quantidadeParcelas < 4:
        # Parcelamento sem juros: quantidade de parcelas menor do que 4
        print(f"O valor das parcelas é de: R${valorDaParcela:.2f}")
        print(f"O valor total parcelado é de: R${valorTotalParcelado:.2f}")

       # Parcelamento com juros: quantidade de parcelas maior ou igual a 4.
elif quantidadeParcelas >= 4:
    # Exigência de saída de console 2 de 2: Mostrar parcelamento com Juros
    print(f"O valor das parcelas é de: R${valorDaParcela:.2f}")
    print(f"O valor total parcelado é de: R${valorTotalParcelado:.2f}")
    # Também acrescentei uma função para mostrar a quantidade de juros, e limitei a quantidade de decimais para 2.
    print(f"A quantidade de juros é de: R${round(valorTotalParcelado - valorDoPedido, 2) }\n")


# Mostrar nome completo ao finalizar o código
print("Programa desenvolvido por Matheus Dantas de Souza")

