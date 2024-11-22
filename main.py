from models.paciente import Paciente

class Initialize():
    def show_menu(self):
        print("1. Inserir novo paciente")
        print("2. Editar paciente existente")
        print("3. Excluir paciente")
        print("4. Consultar paciente")
        print("5. Sair")

    
    def choose_option(self):
        option = input('Escolha uma das opções:\n')
        if option not in ['1', '2', '3', '4']:
            print('\nInvalid option!')
        return option

if __name__ == '__main__':
    init = Initialize()

    option = ''

    while option != '3':
        init.show_menu()

        option = init.choose_option()

        if option == '1':
            print('Você escolheu Cadastrar um novo paciente.')
            nome_paciente = input("Digite o nome do paciente: ")
            data_nascimento = input("Digite a data de nascimento do paciente (DD/MM/AAAA): ")
            sexo_paciente = input("Digite o sexo do paciente: ")
            p = Paciente(None, nome_paciente, data_nascimento, sexo_paciente)
            p.inserirPaciente()
        
        elif option == '2':
            id_paciente = input('Insira o ID do paciente que você deseja editar: ')
            p = Paciente(id_paciente)  
            novos_dados = p.coletar_dados_para_edicao() 
            if novos_dados:
                p.editarPaciente(novos_dados) 
            else:
                print("Nenhuma alteração foi feita.")
        
        elif option == '3':  # Opção para excluir um paciente
            id_paciente = input('Insira o ID do paciente que você deseja excluir: ')

            # Inicializa um objeto Paciente com apenas o ID
            p = Paciente(id_paciente=id_paciente)

            # Tenta excluir o paciente
            confirmacao = input(f"Tem certeza de que deseja excluir o paciente com ID {id_paciente}? (s/n): ").lower()
            if confirmacao == 's':
                p.excluirPaciente()  # Chama o método para excluir
                print(f"Paciente com ID {id_paciente} foi excluído com sucesso.")
            else:
                print("Operação de exclusão cancelada.")

        elif option == "4":
            id_paciente = input("Digite o ID do paciente que deseja consultar: ")
            p = Paciente(id_paciente)
            p.consultarPaciente()