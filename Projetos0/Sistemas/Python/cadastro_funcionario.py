# Mensagem de boas vindas
print("Bem vindos a area de cadastro da MDS - Empresa de Matheus Dantas de Souza")
print('-'*73)

# Lista de armazenamento dos funcionários e inicializa com o ID global
lista_funcionarios = []
id_global = 4516241

# Função para cadastrar um novo funcionário, gerando seu ID
def cadastrar_funcionario(id):
    # Exibe o ID do funcionário
    print('-'*14,'Menu de Cadastro','-'*14)
    print(f"ID do funcionário: {id}")
    # Pede as informações do funcionário para cadastro
    nome = input("Nome do funcionário: ")
    setor = input("Setor do funcionário: ")
    salario = input("Salário do funcionário: ")
    # Cria um dicionário com os dados do funcionário
    funcionario = {"id": id, "nome": nome, "setor": setor, "salario": salario}
    # Adiciona uma cópia do dicionário à lista de funcionários
    lista_funcionarios.append(funcionario.copy())
    print("Funcionário cadastrado com sucesso!")

# Função para consultar funcionários
def consultar_funcionarios():
    while True:
        # Menu para consultar funcionarios cadastrados
        print('-'*14,'Menu de Consulta','-'*14)
        opcao = input("1. Consultar Todos\n2. Consultar por Id\n3. Consultar por Setor\n4. Retornar ao menu\nEscolha uma opção: ")
        print('-'*14)  # Adiciona separador após o menu
        if opcao == '1':
            # Exibição dos funcionários
            print('-'*14)
            for funcionario in lista_funcionarios:
                print(f"Id: {funcionario['id']}\nNome: {funcionario['nome']}\nSetor: {funcionario['setor']}\nSalário: {funcionario['salario']}\n")
        elif opcao == '2':
            # Exibição por ID
            id_consulta = int(input("Informe o id do funcionário: "))
            encontrado = False
            for funcionario in lista_funcionarios:
                if funcionario["id"] == id_consulta:
                    print(f"Id: {funcionario['id']}\nNome: {funcionario['nome']}\nSetor: {funcionario['setor']}\nSalário: {funcionario['salario']}\n")
                    encontrado = True
                    break
            if not encontrado:
                print("Funcionário não encontrado.")
        elif opcao == '3':
            # Consulta e exibe funcionários por setor
            setor_consulta = input("Informe o setor: ")
            encontrados = [funcionario for funcionario in lista_funcionarios if funcionario["setor"] == setor_consulta]
            if encontrados:
                for funcionario in encontrados:
                    print(f"Id: {funcionario['id']}\nNome: {funcionario['nome']}\nSetor: {funcionario['setor']}\nSalário: {funcionario['salario']}\n")
            else:
                print("Nenhum funcionário encontrado no setor informado.")
        elif opcao == '4':
            # Retorna ao menu principal
            return
        else:
            # Opção inválida
            print("Opção inválida")

# Função para remover um funcionário
def remover_funcionario():
    while True:
        # Solicita o ID do funcionário a ser removido
        id_remover = int(input("Informe o id do funcionário a ser removido: "))
        for funcionario in lista_funcionarios:
            if funcionario["id"] == id_remover:
                # Remove o funcionário da lista
                lista_funcionarios.remove(funcionario)
                print("Funcionário removido com sucesso!")
                return
        print("Id inválido")

# Menu principal do programa
while True:
    # Exibe o menu principal
    print('-'*14,'Menu Principal','-'*14)
    opcao = input("1. Cadastrar Funcionário\n2. Consultar Funcionário\n3. Remover Funcionário\n4. Encerrar Programa\nEscolha uma opção: ")
    print('-'*14)  # Adiciona separador após o menu principal
    if opcao == '1':
        # Incrementa o ID global e cadastra um novo funcionário
        id_global += 1
        cadastrar_funcionario(id_global)
    elif opcao == '2':
        # Chama a função para consultar funcionários
        consultar_funcionarios()
    elif opcao == '3':
        # Chama a função para remover um funcionário
        remover_funcionario()
    elif opcao == '4':
        # Encerra o programa
        print("Programa encerrado.")
        break
    else:
        # Em caso de erro
        print("Opção inválida")

