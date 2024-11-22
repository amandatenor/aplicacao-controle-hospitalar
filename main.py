from models.paciente import Paciente
from models.procedimento import Procedimento
from models.consulta import Consulta

class Initialize():
    def show_menu(self):

        print('1- Cadastrar um paciente')
        print('2- Consultar paciente')
        print('3- Editar paciente')
        print('4- Excluir paciente')

        print('5- Cadastrar consulta')
        print('6- Consultar consulta')
        print('7- Editar consulta')
        print('8- Excluir consulta')

        print('9- Cadastrar um procedimento')
        print('10- Consultar procedimento')
        print('11- Editar procedimento')
        print('12- Excluir procedimento')

        print('13- Sair')
    
    def choose_option(self):
        option = input('Escolha uma das opções:\n')
        if option not in ['1', '2', '3', '4', '5','6', '7', '8', '9', '10', '11', '12','13']:
            print('\nInvalid option!')

        if option == '1':
            print('Você escolheu Cadastrar um novo paciente.')
            nome_paciente = input("Digite o nome do paciente: ")
            data_nascimento = input("Digite a data de nascimento do paciente (DD/MM/AAAA): ")
            sexo_paciente = input("Digite o sexo do paciente: ")
            p = Paciente(None, nome_paciente, data_nascimento, sexo_paciente)
            p.inserirPaciente()

        elif option == '2':
            id_paciente = input("Digite o ID do paciente que deseja consultar: ")
            p = Paciente(id_paciente)
            p.consultarPaciente()

        elif option == '4': 
            id_paciente = input('Insira o ID do paciente que você deseja excluir: ')

            # Inicializa um objeto Paciente com apenas o ID
            p = Paciente(id_paciente=id_paciente)

            confirmacao = input(f"Tem certeza de que deseja excluir o paciente com ID {id_paciente}? (s/n): ").lower()
            if confirmacao == 's':
                p.excluirPaciente() 
                print(f"Paciente com ID {id_paciente} foi excluído com sucesso.")
            else:
                print("Operação de exclusão cancelada.")
        
        elif option == "3":

            id_paciente = input('Insira o ID do paciente que você deseja editar: ')
            p = Paciente(id_paciente)  
            novos_dados = p.coletar_dados_para_edicao() 
            if novos_dados:
                p.editarPaciente(novos_dados) 
            else:
                print("Nenhuma alteração foi feita.")

        elif option == "5":
            print('Você escolheu Cadastrar uma nova consulta.')
            descricao = input("Digite a descrição da consulta: ")
            paciente = input("Digite o ID do paciente: ")
            lista_procedimentos = input("Digite os IDs dos procedimentos realizados (separados por vírgula): ").split(',')
            data = input("Digite a data da consulta (formato: DD/MM/AAAA): ")

            consulta = Consulta(None, descricao, paciente, lista_procedimentos, data)
            consulta.inserirConsulta()

        elif option == "6":
            id_consulta = input('Você escolheu consultar uma consulta. Digite o ID da consulta que deseja consultar: ')
            consulta = Consulta(id_consulta)
            consulta.consultarConsulta()

        elif option == "7":
            id_consulta = input('Você escolheu editar uma consulta. Digite o ID da consulta que deseja alterar: ')

            consulta = Consulta(id_consulta)

            if consulta.consultarConsulta():
                descricao = input("Digite a nova descrição da consulta: ")
                paciente = input("Digite o novo ID do paciente: ")
                lista_procedimentos = input("Digite os novos IDs dos procedimentos realizados (separados por vírgula): ").split(',')
                data = input("Digite a nova data da consulta (formato: DD/MM/AAAA): ")

                novos_dados = {
                    "descricao": descricao,
                    "paciente": paciente,
                    "lista_procedimentos": lista_procedimentos,
                    "data": data
                }

                consulta.editarConsulta(novos_dados)

        elif option == "8":
            id_consulta = input('Você escolheu excluir uma consulta. Digite o ID da consulta que deseja excluir: ')
            consulta = Consulta(id_consulta)
            consulta.excluirConsulta()


        elif option == "9":
            print('Você escolheu Cadastrar um novo procedimento.')
            nome_procedimento = input("Digite o nome do procedimento: ")
            descricao_procedimento = input("Digite a descrição do procedimento: ")
            p = Procedimento(None, nome_procedimento, descricao_procedimento)
            p.inserirProcedimento()

        elif option == "10":
            id_procedimento = input('Você escolheu consultar procedimento. Digite o ID do procedimento que deseja consultar: ')
            p = Procedimento(id_procedimento)
            p.consultarProcedimento()

        elif option == "11":
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

        elif option == '12':
            id_procedimento = input('Você escolheu excluir procedimento. Digite o ID do procedimento que deseja excluir:')
            p = Procedimento(id_procedimento)
            p.excluir_procedimento()
        return option

if __name__ == '__main__':
    init = Initialize()

    option = ''

    while option != '13':
        init.show_menu()

        option = init.choose_option()

        # if option == '1':
        #     print('Você escolheu Cadastrar um novo paciente.')
        #     nome_paciente = input("Digite o nome do paciente: ")
        #     data_nascimento = input("Digite a data de nascimento do paciente (DD/MM/AAAA): ")
        #     sexo_paciente = input("Digite o sexo do paciente: ")
        #     p = Paciente(None, nome_paciente, data_nascimento, sexo_paciente)
        #     p.inserirPaciente()

        # elif option == '2':
        #     id_paciente = input("Digite o ID do paciente que deseja consultar: ")
        #     p = Paciente(id_paciente)
        #     p.consultarPaciente()

        # elif option == '4': 
        #     id_paciente = input('Insira o ID do paciente que você deseja excluir: ')

        #     # Inicializa um objeto Paciente com apenas o ID
        #     p = Paciente(id_paciente=id_paciente)

        #     confirmacao = input(f"Tem certeza de que deseja excluir o paciente com ID {id_paciente}? (s/n): ").lower()
        #     if confirmacao == 's':
        #         p.excluirPaciente() 
        #         print(f"Paciente com ID {id_paciente} foi excluído com sucesso.")
        #     else:
        #         print("Operação de exclusão cancelada.")
        
        # elif option == "3":

        #     id_paciente = input('Insira o ID do paciente que você deseja editar: ')
        #     p = Paciente(id_paciente)  
        #     novos_dados = p.coletar_dados_para_edicao() 
        #     if novos_dados:
        #         p.editarPaciente(novos_dados) 
        #     else:
        #         print("Nenhuma alteração foi feita.")

        # elif option == "5":
        #     print('Você escolheu Cadastrar uma nova consulta.')
        #     descricao = input("Digite a descrição da consulta: ")
        #     paciente = input("Digite o ID do paciente: ")
        #     lista_procedimentos = input("Digite os IDs dos procedimentos realizados (separados por vírgula): ").split(',')
        #     data = input("Digite a data da consulta (formato: DD/MM/AAAA): ")

        #     consulta = Consulta(None, descricao, paciente, lista_procedimentos, data)
        #     consulta.inserirConsulta()

        # elif option == "6":
        #     id_consulta = input('Você escolheu consultar uma consulta. Digite o ID da consulta que deseja consultar: ')
        #     consulta = Consulta(id_consulta)
        #     consulta.consultarConsulta()

        # elif option == "7":
        #     id_consulta = input('Você escolheu editar uma consulta. Digite o ID da consulta que deseja alterar: ')

        #     consulta = Consulta(id_consulta)

        #     if consulta.consultarConsulta():
        #         descricao = input("Digite a nova descrição da consulta: ")
        #         paciente = input("Digite o novo ID do paciente: ")
        #         lista_procedimentos = input("Digite os novos IDs dos procedimentos realizados (separados por vírgula): ").split(',')
        #         data = input("Digite a nova data da consulta (formato: DD/MM/AAAA): ")

        #         novos_dados = {
        #             "descricao": descricao,
        #             "paciente": paciente,
        #             "lista_procedimentos": lista_procedimentos,
        #             "data": data
        #         }

        #         consulta.editarConsulta(novos_dados)

        # elif option == "8":
        #     id_consulta = input('Você escolheu excluir uma consulta. Digite o ID da consulta que deseja excluir: ')
        #     consulta = Consulta(id_consulta)
        #     consulta.excluirConsulta()


        # elif option == "9":
        #     print('Você escolheu Cadastrar um novo procedimento.')
        #     nome_procedimento = input("Digite o nome do procedimento: ")
        #     descricao_procedimento = input("Digite a descrição do procedimento: ")
        #     p = Procedimento(None, nome_procedimento, descricao_procedimento)
        #     p.inserirProcedimento()

        # elif option == "10":
        #     id_procedimento = input('Você escolheu consultar procedimento. Digite o ID do procedimento que deseja consultar: ')
        #     p = Procedimento(id_procedimento)
        #     p.consultarProcedimento()

        # elif option == "11":
        #     id_procedimento = input('Você escolheu editar procedimento. Digite o ID do procedimento que deseja alterar: ')
        
        #     p = Procedimento(id_procedimento)

        #     if p.consultarProcedimento():
        #         nome_procedimento = input("Digite o novo nome do procedimento: ")
        #         descricao_procedimento = input("Digite a nova descrição do procedimento: ")

        #         novos_dados = {
        #             "nome_procedimento": nome_procedimento,
        #             "descricao_procedimento": descricao_procedimento
        #         }

        #         p.editarProcedimento(novos_dados)

        # elif option == '12':
        #     id_procedimento = input('Você escolheu excluir procedimento. Digite o ID do procedimento que deseja excluir:')
        #     p = Procedimento(id_procedimento)
        #     p.excluir_procedimento()
    

