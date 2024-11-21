from models.paciente import Paciente
from models.procedimento import Procedimento

class Initialize():
    def show_menu(self):

        print('1- Cadastrar um paciente')
        print('4- Consultar paciente')
        print('2- Cadastrar um procedimento')
        print('5- Consultar procedimento')
        print('6- Editar procedimento')
        print('7- Excluir procedimento')
    
    def choose_option(self):
        option = input('Escolha uma das opções:\n')
        if option not in ['1', '2', '3', '4', '5','6', '7']:
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

        elif option == "2":
            print('Você escolheu Cadastrar um novo procedimento.')
            nome_procedimento = input("Digite o nome do procedimento: ")
            descricao_procedimento = input("Digite a descrição do procedimento: ")
            p = Procedimento(None, nome_procedimento, descricao_procedimento)
            p.inserirProcedimento()

        elif option == "5":
            id_procedimento = input('Você escolheu consultar procedimento. Digite o ID do procedimento que deseja consultar: ')
            p = Procedimento(id_procedimento)
            p.consultarProcedimento()

        elif option == "6":
            id_procedimento = input('Você escolheu editar procedimento. Digite o ID do procedimento que deseja alterar: ')
        
            p = Procedimento(id_procedimento)

            if p.consultarProcedimento():
                nome_procedimento = input("Digite o novo nome do procedimento: ")
                descricao_procedimento = input("Digite a nova descrição do procedimento: ")

                novos_dados = {
                    "nome_procedimento": nome_procedimento,
                    "descricao_procedimento": descricao_procedimento
                }

                p.editarProcedimento(novos_dados)
            

        elif option == '7':
            id_procedimento = input('Você escolheu excluir procedimento. Digite o ID do procedimento que deseja excluir:')
            p = Procedimento(id_procedimento)
            p.excluir_procedimento()
    

