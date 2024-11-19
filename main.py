from models.paciente import Paciente

class Initialize():
    def show_menu(self):
        print('Bem vindo ao sistema hospitalar.')
        print('1- Cadastrar um paciente')
        print('4- Consultar paciente')
    
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

        elif option == "4":
            id_paciente = input("Digite o ID do paciente que deseja consultar: ")
            p = Paciente(id_paciente)
            p.consultarPaciente()