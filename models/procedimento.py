from utils.armazenamento import Armazenamento
from utils.log import Log

class Procedimento:
    contador_id = 1 

    def __init__(self, id_procedimento=None, nome_procedimento='', descricao_procedimento=''):
        # Gerar ID em sequência para os pacientes cadastrados
        if id_procedimento is None:
            self.id_procedimento = str(Procedimento.contador_id)
            Procedimento.contador_id += 1
        else:
            self.id_procedimento = id_procedimento  # Para edição ou consulta

        self.nome_procedimento = nome_procedimento
        self.descricao_procedimento = descricao_procedimento
        self.__armazenamento = Armazenamento('out/pacientes.csv', 'out/procedimento.csv', 'out/consulta.csv')
        
    def inserirProcedimento(self):
        """Insere o procedimento no armazenamento."""
        # Usa os atributos do próprio objeto em vez de solicitar novamente os dados
        if not all([self.nome_procedimento, self.descricao_procedimento]):
            print("Por favor, forneça todas as informações necessárias do procedimento.")
            return

        # Salva os dados no armazenamento
        self.__armazenamento.salvar_procedimento(self.id_procedimento, self.nome_procedimento, self.descricao_procedimento)
        print(f'Procedimento {self.nome_procedimento} com ID {self.id_procedimento} inserido com sucesso.')

        #Registra os dados no Log 
        Log.registrar_log(f"Procedimento inserido: {self.id_procedimento}, {self.nome_procedimento}, {self.descricao_procedimento}")

    def consultarProcedimento(self):
        """Consulta o procedimento no armazenamento"""
        
        procedimento = self.__armazenamento.consultar_procedimento(self.id_procedimento)

        if procedimento:
            self.nome_procedimento, self.descricao_procedimento = procedimento

            #Registra os dados no Log 
            Log.registrar_log(f"Procedimento consultado: {procedimento}")

            print(f'Procedimento encontrado : {self.nome_procedimento}, Descrição: {self.descricao_procedimento}')
            return True 
        
        else:
            print(f'Procedimento com o ID {self.id_procedimento} não encontrado.')
            return False

    def editarProcedimento(self, novos_dados):
        """Edita os dados de um procedimento no armazenamento."""
        
        # Atualiza os atributos com base nos novos dados, se fornecidos
        self.nome_procedimento = novos_dados.get("nome_procedimento", self.nome_procedimento)
        self.descricao_procedimento = novos_dados.get("descricao_procedimento", self.descricao_procedimento)

        # Salva as alterações no armazenamento (arquivo)
        self.__armazenamento.editar_procedimento(self.id_procedimento, self.nome_procedimento, self.descricao_procedimento)

        print(f'Procedimento {self.nome_procedimento} com ID {self.id_procedimento} atualizado com sucesso.')

        #Registra os dados no Log 
        Log.registrar_log(f"Procedimento editado: {self.id_procedimento}, {self.nome_procedimento}, {self.descricao_procedimento}")

        
    def excluir_procedimento(self):
        #Exclui o paciente do armazenamento.
        if self.__armazenamento.remover_procedimento(self.id_procedimento):
            print(f'Procedimento com ID {self.id_procedimento} foi excluído.')

            # Registra os dados no Log
            Log.registrar_log(f"Procedimento excluído: {self.id_procedimento}")
        else:
            print(f'Procedimento com ID {self.id_procedimento} não foi encontrado.')