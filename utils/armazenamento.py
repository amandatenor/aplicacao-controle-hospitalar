class Armazenamento():
    def __init__(self, arquivo_pacientes, arquivo_procedimentos, arquivo_consultas):
        self.arquivo_pacientes = arquivo_pacientes
        self.arquivo_procedimentos = arquivo_procedimentos
        self.arquivo_consultas = arquivo_consultas

    
    def salvar_paciente(self, id_paciente, nome_paciente, data_nascimento, sexo_paciente): # etc
        '''Adiciona uma linha no arquivo de pacientes'''

        with open(self.arquivo_pacientes, 'a+') as f:
            f.writelines(f'{id_paciente}, {nome_paciente}, {data_nascimento}, {sexo_paciente}\n')

    def obter_proximo_id(self, arquivo):
    #Lê o arquivo de pacientes e retorna o próximo ID disponível.
        try:
            with open(arquivo, 'r') as f:
                linhas = f.readlines()

            if not linhas:
                return 1  # Caso o arquivo esteja vazio, o primeiro ID será 1.

            # Extrai os IDs, converte para inteiros e retorna o próximo número na sequência.
            ids = [int(linha.split(',')[0]) for linha in linhas if linha.strip()]
            return max(ids) + 1
        except Exception: # FileNotFound ou ids sendo vazio
            return 1  # Caso o arquivo não exista, o primeiro ID será 1.

    def consultar_paciente(self, id_paciente):
        '''Percorre arquivo de pacientes e retorna dados da linha correspondente ao codigo passado'''

        with open(self.arquivo_pacientes, 'r') as f:  # Alterado para 'r' para leitura
            campos = []
            for linha in f.readlines():
                campos = [campo.strip() for campo in linha.strip().split(',')]
                codigo = campos[0]  # Primeiro campo é o código

            if codigo == id_paciente:  # Compara com o id_paciente passado
                # Retorna os dados restantes
                nome = campos[1]
                data_nascimento = campos[2]
                sexo = campos[3]
                return nome, data_nascimento, sexo

        return None


    def editar_paciente(self, id_paciente, nome_paciente=None, data_nascimento=None, sexo_paciente=None):
        #Lê o arquivo de pacientes e substitui a linha correspondente ao código passado com os dados passados
        
        linhas = None

        with open(self.arquivo_pacientes, 'r') as f:
            linhas = f.readlines()

        paciente_encontrado = False  # Para verificar se o paciente foi encontrado

        for i in range(len(linhas)):
            # Remove espaços em branco antes e depois da linha
            linha = linhas[i].strip()

            # Verifica se a linha não está vazia e tem o formato esperado (4 campos separados por vírgula)
            if linha:
                dados = linha.split(',')

                if len(dados) == 4:  # Se houver exatamente 4 campos
                    codigo, nome, data_nascimento_lido, sexo = dados
                    if codigo == id_paciente:
                        nome = nome_paciente or nome
                        data_nascimento_lido = data_nascimento or data_nascimento_lido
                        sexo = sexo_paciente or sexo

                        # Atualiza a linha com os dados modificados
                        linhas[i] = f'{codigo},{nome},{data_nascimento_lido},{sexo}\n'
                        paciente_encontrado = True
                        break
                else:
                    print(f"Erro de formatação na linha: {linha}")
                    continue

        if not paciente_encontrado:
            return False

        # Reescreve o arquivo com as alterações
        with open(self.arquivo_pacientes, 'w') as f:
            f.writelines(linhas)

        return True


    def remover_paciente(self, id_paciente):
        #Le arquivo de pacientes e remove linha correspondente ao codigo passado

        linhas = None

        # Lê todas as linhas do arquivo
        with open(self.arquivo_pacientes, 'r') as f:
            linhas = f.readlines()

        indice_paciente = None

        # Percorre as linhas para encontrar o paciente
        for i in range(len(linhas)):
            dados = linhas[i].strip().split(',')  # Divide a linha em campos
            codigo = dados[0]  # O primeiro campo é o ID do paciente

            if codigo == id_paciente:
                indice_paciente = i
                break

        # Verifica se o paciente foi encontrado
        if indice_paciente is None:
            return False

        # Remove a linha correspondente ao paciente
        del linhas[indice_paciente]

        # Remove as consultas associadas ao paciente
        self.remover_consulta_do_paciente(id_paciente)

        # Reescreve o arquivo com as linhas restantes
        with open(self.arquivo_pacientes, 'w') as f:
            f.writelines(linhas)

        return True

    def salvar_procedimento(self, id_procedimento, nome_procedimento, descricao_procedimento):
        '''Adiciona uma linha no arquivo de procedimentos'''

        with open(self.arquivo_procedimentos, 'a+') as f:
            f.write(f'{id_procedimento},{nome_procedimento},{descricao_procedimento}\n')

    def consultar_procedimento(self, id_procedimento):
        '''Percorre arquivo de procedimentos e retorna dados da linha
        correspondente ao codigo passado'''

        with open(self.arquivo_procedimentos, 'r') as f:
            for linha in f.readlines():
                campos = [campo.strip() for campo in linha.strip().split(',')]
                codigo = campos[0]

                if codigo == id_procedimento:
                    nome = campos[1]
                    descricao = campos[2]
                    
                    return nome, descricao # TODO: retornar classe

        return None

          
    def editar_procedimento(self, id_procedimento, nome_procedimento=None, descricao_procedimento=None):
        '''Le arquivo de procedimentos e substitui a linha
        correspondente ao codigo passado com os dados passados'''

        with open(self.arquivo_procedimentos, 'r') as f:
            linhas = f.readlines()

        procedimento_encontrado = False

        for i in range(len(linhas)):
            campos = [campo.strip() for campo in linhas[i].strip().split(',')]
            codigo = campos[0]

            if codigo == id_procedimento:
                procedimento_encontrado = True
               
                nome_atualizado = nome_procedimento if nome_procedimento else campos[1]
                descricao_atualizada = descricao_procedimento if descricao_procedimento else campos[2]
                
                linhas[i] = f'{id_procedimento},{nome_atualizado},{descricao_atualizada}\n'
                break

        if procedimento_encontrado:
            with open(self.arquivo_procedimentos, 'w') as f:
                f.writelines(linhas)

            return True
        else:
            return False
            


    def remover_procedimento(self, id_procedimento):
        '''Le arquivo de procedimentos e remove linha correspondente
        ao codigo passado'''

        with open(self.arquivo_procedimentos, 'r') as f:
            linhas = f.readlines()

        indice_procedimento = None

        for i in range(len(linhas)):
            campos = [campo.strip() for campo in linhas[i].strip().split(',')]
            codigo = campos[0]

            if codigo == id_procedimento:
                indice_procedimento = i
                break 

        if indice_procedimento is None:
            return False  

        del linhas[indice_procedimento]

        self.remover_consulta_do_procedimento(id_procedimento)

        with open(self.arquivo_procedimentos, 'w') as f:
            f.writelines(linhas)

        return True  

    
    def salvar_consulta(self, id_consulta, descricao, paciente, lista_procedimentos, data):
        """Adiciona uma linha no arquivo de consultas."""
        procedimentos_str = '|'.join(lista_procedimentos)  # Converte a lista para uma string separada por "|"
        with open(self.arquivo_consultas, 'a+') as f:
            f.write(f'{id_consulta},{descricao},{paciente},{procedimentos_str},{data}\n')


    def consultar_consulta(self, id_consulta):
        """Percorre arquivo de consultas e retorna dados da linha correspondente ao código passado."""
        with open(self.arquivo_consultas, 'r') as f:
            for linha in f.readlines():
                campos = [campo.strip() for campo in linha.strip().split(',')]
                codigo = campos[0]

                if codigo == id_consulta:
                    descricao = campos[1]
                    paciente = campos[2]
                    lista_procedimentos = campos[3].split('|')  # Converte a string de volta para uma lista
                    data = campos[4]

                    return descricao, paciente, lista_procedimentos, data

        return None

    def editar_consulta(self, id_consulta, descricao=None, paciente=None, lista_procedimentos=None, data=None):
        """Lê arquivo de consultas e substitui a linha correspondente ao código passado com os dados passados."""
        with open(self.arquivo_consultas, 'r') as f:
            linhas = f.readlines()

        consulta_encontrada = False

        for i in range(len(linhas)):
            campos = [campo.strip() for campo in linhas[i].strip().split(',')]
            codigo = campos[0]

            if codigo == id_consulta:
                consulta_encontrada = True

                descricao_atualizada = descricao if descricao else campos[1]
                paciente_atualizado = paciente if paciente else campos[2]
                lista_procedimentos_atualizada = '|'.join(lista_procedimentos) if lista_procedimentos else campos[3]
                data_atualizada = data if data else campos[4]

                linhas[i] = f'{id_consulta},{descricao_atualizada},{paciente_atualizado},{lista_procedimentos_atualizada},{data_atualizada}\n'
                break

        if consulta_encontrada:
            with open(self.arquivo_consultas, 'w') as f:
                f.writelines(linhas)

            return True
        else:
            return False


    def remover_consulta(self, codigo_consulta):
        '''Le arquivo de consultas e remove linha correspondente ao
        codigo passado'''

        linhas = None

        with open(self.arquivo_consultas, 'r') as f:
            linhas = f.readlines()

        indice_consulta = None

        for i in range(len(linhas)):
            dados = linhas[i][:-1].split(',')
            codigo = dados[0]

            if codigo == codigo_consulta:
                indice_consulta = i

        if indice_consulta == None:
            return False

        del linhas[indice_consulta]

        with open(self.arquivo_consultas, 'w') as f:
            f.writelines(linhas)
        
        return True


    def remover_consulta_do_paciente(self, id_paciente):
        '''Le arquivo de consultas e remove linha que contem o
        paciente correspondente ao codigo passado'''

        linhas = None

        with open(self.arquivo_consultas, 'r') as f:
            linhas = f.readlines()

        indices_consultas = []

        for i in range(len(linhas)):
            campos = [campo.strip() for campo in linhas[i].strip().split(',')]

            if len(campos) < 5:
                continue

            codigo, descricao, paciente, procedimentos, data = campos

            if paciente == id_paciente:
                indices_consultas.append(i)

        for indice_consulta in indices_consultas:
            del linhas[indice_consulta]

        with open(self.arquivo_consultas, 'w') as f:
            f.writelines(linhas)

        print(f'Consultas associadas ao paciente {id_paciente} foram removidas.')


    def remover_consulta_do_procedimento(self, id_procedimento):
        '''Le arquivo de consultas e remove linha que contem o
        procedimento correspondente ao codigo passado'''

        linhas = None

        with open(self.arquivo_consultas, 'r') as f:
            linhas = f.readlines()

        indices_consultas = []

        for i in range(len(linhas)):
            campos = [campo.strip() for campo in linhas[i].strip().split(',')]

            if len(campos) < 5:
                continue

            codigo, descricao, paciente, procedimentos, data = campos

            if id_procedimento in procedimentos.split('|'):
                indices_consultas.append(i)

        for indice_consulta in indices_consultas:
            del linhas[indice_consulta]

        with open(self.arquivo_consultas, 'w') as f:
            f.writelines(linhas)

        print(f'Consultas associadas ao procedimento {id_procedimento} foram removidas.')
