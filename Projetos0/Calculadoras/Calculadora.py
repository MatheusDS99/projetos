
def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return None  


def calculadora():
    while True:
        print("\nEscolha a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Digite sua escolha (1/2/3/4/5): ")

        if escolha == '5':
            print("Encerrando a calculadora.")
            break

        if escolha in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Erro: Por favor, insira números válidos.")
                continue

            if escolha == '1':
                print(f"Resultado: {num1} + {num2} = {adicionar(num1, num2)}")
            elif escolha == '2':
                print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
            elif escolha == '3':
                print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
            elif escolha == '4':
                resultado = dividir(num1, num2)
                if resultado is None:
                    print("Erro: Divisão por zero")
                else:
                    print(f"Resultado: {num1} / {num2} = {resultado}")
        else:
            print("Escolha inválida, tente novamente.")



calculadora()
