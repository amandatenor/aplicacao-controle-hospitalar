from utils.armazenamento import Armazenamento
from utils.log import Log

class Consulta:
    contador_id = 1  # Inicializa com 1; pode ser alterado com base no maior ID existente

    def __init__(self, id_consulta=None, descricao='', paciente='', lista_procedimentos=None, data=None):
        # Gerar ID em sequência para as consultas cadastradas
        if id_consulta is None:
            self.id_consulta = str(Consulta.contador_id)
            Consulta.contador_id += 1
        else:
            self.id_consulta = id_consulta  # Para edição ou consulta

        self.descricao = descricao
        self.paciente = paciente
        self.lista_procedimentos = lista_procedimentos if lista_procedimentos else []
        self.data = data
        self.__armazenamento = Armazenamento('out/pacientes.csv', 'out/procedimento.csv', 'out/consulta.csv')

    def inserirConsulta(self):
        """Insere a consulta no armazenamento."""
        if not all([self.descricao, self.paciente, self.data]):
            print("Por favor, forneça todas as informações necessárias da consulta.")
            return
        
        # Salva os dados no armazenamento
        self.__armazenamento.salvar_consulta(
            self.id_consulta,
            self.descricao,
            self.paciente,
            self.lista_procedimentos,
            self.data
        )
        print(f'Consulta com ID {self.id_consulta} inserida com sucesso.')

         # Registra os dados no Log
        Log.registrar_log(f"Consulta inserida: {self.id_consulta}, {self.descricao}, Paciente: {self.paciente}, Procedimento:{self.lista_procedimentos}, Data: {self.data}")

    def consultarConsulta(self):
        """Consulta os detalhes de uma consulta no armazenamento."""
        consulta = self.__armazenamento.consultar_consulta(self.id_consulta)

        if consulta:
            self.descricao, self.paciente, self.lista_procedimentos, self.data = consulta

            # Registra os dados no Log
            Log.registrar_log(f"Consulta consultada: {consulta}")

            print(f'Consulta encontrada: Descrição: {self.descricao}, Paciente: {self.paciente}, Data: {self.data}\n '
                  f'Procedimentos: {", ".join(self.lista_procedimentos)}')
            return True
        else:
            print(f'Consulta com o ID {self.id_consulta} não encontrada.')
            return False

    def editarConsulta(self, novos_dados):
        """Edita os dados de uma consulta no armazenamento."""
        # Atualiza os atributos com base nos novos dados, se fornecidos
        self.descricao = novos_dados.get("descricao", self.descricao)
        self.paciente = novos_dados.get("paciente", self.paciente)
        self.lista_procedimentos = novos_dados.get("lista_procedimentos", self.lista_procedimentos)
        self.data = novos_dados.get("data", self.data)

        # Salva as alterações no armazenamento
        self.__armazenamento.editar_consulta(
            self.id_consulta,
            self.descricao,
            self.paciente,
            self.lista_procedimentos,
            self.data
        )
        print(f'Consulta com ID {self.id_consulta} atualizada com sucesso.')

        # Registra os dados no Log
        Log.registrar_log(f"Consulta editada: {self.id_consulta}, {self.descricao}, Paciente: {self.paciente}, Data: {self.data}")

    def excluirConsulta(self):
        """Exclui uma consulta do armazenamento."""
        if self.__armazenamento.remover_consulta(self.id_consulta):
            print(f'Consulta com ID {self.id_consulta} foi excluída.')

            # Registra os dados no Log
            Log.registrar_log(f"Consulta excluída: {self.id_consulta}")
        else:
            print(f'Consulta com ID {self.id_consulta} não foi encontrada.' )
