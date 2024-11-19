from utils.armazenamento import Armazenamento

class Paciente:
    contador_id = 1  # Inicializa com 1; pode ser alterado com base no maior ID existente

    def __init__(self, id_paciente=None, nome_paciente='', data_nascimento='', sexo_paciente=''):
        # Gerar ID em sequência para os pacientes cadastrados
        if id_paciente is None:
            self.id_paciente = str(Paciente.contador_id)
            Paciente.contador_id += 1
        else:
            self.id_paciente = id_paciente  # Para edição ou consulta

        self.nome_paciente = nome_paciente
        self.data_nascimento = data_nascimento
        self.sexo_paciente = sexo_paciente
        self.__armazenamento = Armazenamento('out/pacientes.csv', 'out/procedimento.csv', 'out/consulta.csv')

    def inserirPaciente(self):
        """Insere o paciente no armazenamento."""
        # Usa os atributos do próprio objeto em vez de solicitar novamente os dados
        if not all([self.nome_paciente, self.data_nascimento, self.sexo_paciente]):
            print("Por favor, forneça todas as informações necessárias do paciente.")
            return

        # Salva os dados no armazenamento
        self.__armazenamento.salvar_paciente(self.id_paciente, self.nome_paciente, self.data_nascimento, self.sexo_paciente)
        print(f'Paciente {self.nome_paciente} com ID {self.id_paciente} inserido com sucesso.')

    def editarPaciente(self, novos_dados):
        """Edita o paciente com base nos novos dados fornecidos."""
        if not isinstance(novos_dados, dict):
            print("Os novos dados devem ser fornecidos como um dicionário.")
            return

        # Atualiza os atributos com base nos novos dados, se fornecidos
        self.nome_paciente = novos_dados.get("nome_paciente", self.nome_paciente)
        self.data_nascimento = novos_dados.get("data_nascimento", self.data_nascimento)
        self.sexo_paciente = novos_dados.get("sexo_paciente", self.sexo_paciente)

        # Salva as alterações no armazenamento
        self.__armazenamento.editar_paciente(self.id_paciente, self.nome_paciente, self.data_nascimento, self.sexo_paciente)
        print(f'Paciente {self.nome_paciente} com ID {self.id_paciente} atualizado com sucesso.')

    def excluirPaciente(self):
        """Exclui o paciente do armazenamento."""
        self.__armazenamento.remover_paciente(self.id_paciente)
        print(f'Paciente com ID {self.id_paciente} foi excluído.')

    def consultarPaciente(self):
        """Consulta as informações do paciente no armazenamento."""
        paciente = self.__armazenamento.consultar_paciente(self.id_paciente)
        if paciente:
            self.nome_paciente, self.data_nascimento, self.sexo_paciente = paciente
            print(f'Paciente encontrado: {self.nome_paciente}, Nascimento: {self.data_nascimento}, Sexo: {self.sexo_paciente}.')
        else:
            print(f'Paciente com ID {self.id_paciente} não encontrado.')
