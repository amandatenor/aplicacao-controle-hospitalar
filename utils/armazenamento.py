class Armazenamento():
    def __init__(self, arquivo_pacientes, arquivo_procedimentos, arquivo_consultas):
        self.arquivo_pacientes = arquivo_pacientes
        self.arquivo_procedimentos = arquivo_procedimentos
        self.arquivo_consultas = arquivo_consultas


    def salvar_paciente(self, id_paciente, nome_paciente, data_nascimento, sexo_paciente): # etc
        '''Adiciona uma linha no arquivo de pacientes'''

        with open(self.arquivo_pacientes, 'a+') as f:
            f.writelines(f'{id_paciente}, {nome_paciente}, {data_nascimento}, {sexo_paciente}')


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

        print('Paciente nao encontrado')
        return None, None, None, None  


    def editar_paciente(self, id_paciente, nome_paciente=None):
        '''Le arquivo de pacientes e substitui a linha correspondente
        ao codigo passado com os dados passados'''

        linhas = None

        with open(self.arquivo_pacientes, 'r') as f:
            linhas = f.readlines()

        for i in range(len(linhas)):
            codigo, nome = linhas[i][:-1].split(',')

            if codigo == id_paciente:
                linhas[i] = f'{id_paciente},{nome_paciente or nome}\n'

        # TODO: mostrar mensagem sobre codigo inexistente
        with open(self.arquivo_pacientes, 'w') as f:
            f.writelines(linhas)


    def remover_paciente(self, id_paciente):
        '''Le arquivo de pacientes e remove linha correspondente ao
        codigo passado'''

        linhas = None

        with open(self.arquivo_pacientes, 'r') as f:
            linhas = f.readlines()

        indice_paciente = None

        for i in range(len(linhas)):
            codigo, nome = linhas[i][:-1].split(',')

            if codigo == id_paciente:
                indice_paciente = i

        if indice_paciente == None:
            print('Paciente nao encontrado')
            return

        del linhas[indice_paciente]
        self.remover_consultas_do_paciente(id_paciente)

        with open(self.arquivo_pacientes, 'w') as f:
            f.writelines(linhas)


    def salvar_procedimento(self, codigo_procedimento, nome_procedimento): # etc
        '''Adiciona uma linha no arquivo de procedimentos'''

        with open(self.arquivo_procedimentos, 'a+') as f:
            f.append(f'{codigo_procedimento},{nome_procedimento}\n')


    def consultar_procedimento(self, codigo_procedimento):
        '''Percorre arquivo de procedimentos e retorna dados da linha
        correspondente ao codigo passado'''

        with open(self.arquivo_procedimentos, 'a+') as f:
            for linha in f.readlines():
                codigo, nome = linha[:-1].split(',')

                if codigo == codigo_procedimento:
                    return codigo, nome # TODO: retornar classe

        print('Procedimento nao encontrado')
        return None, None


    def editar_procedimento(self, codigo_procedimento, nome_procedimento=None):
        '''Le arquivo de procedimentos e substitui a linha
        correspondente ao codigo passado com os dados passados'''

        linhas = None

        with open(self.arquivo_procedimentos, 'r') as f:
            linhas = f.readlines()

        for i in range(len(linhas)):
            codigo, nome = linhas[i][:-1].split(',')

            if codigo == codigo_procedimento:
                linhas[i] = f'{codigo_procedimento},{nome_procedimento or nome}\n'

        # TODO: mostrar mensagem sobre codigo inexistente
        with open(self.arquivo_procedimentos, 'w') as f:
            f.writelines(linhas)


    def remover_procedimento(self, codigo_procedimento):
        '''Le arquivo de procedimentos e remove linha correspondente
        ao codigo passado'''

        linhas = None

        with open(self.arquivo_procedimentos, 'r') as f:
            linhas = f.readlines()

        indice_procedimento = None

        for i in range(len(linhas)):
            codigo, nome = linhas[i][:-1].split(',')

            if codigo == codigo_procedimento:
                indice_procedimento = i

        if indice_procedimento == None:
            print('Procedimento nao encontrado')
            return

        del linhas[indice_procedimento]
        self.remover_consultas_do_procedimento(codigo_procedimento)

        with open(self.arquivo_procedimentos, 'w') as f:
            f.writelines(linhas)


    def salvar_consulta(self, codigo_consulta, codigos_procedimentos, id_paciente): # etc
        '''Adiciona uma linha no arquivo de consultas'''

        with open(self.arquivo_consultas, 'a+') as f:
            f.append(f'{codigo_consulta},{";".join(codigo_procedimento)},{id_paciente}\n')


    def consultar_consulta(self, codigo_consulta):
        '''Percorre arquivo de consultas e retorna dados da linha
        correspondente ao codigo passado'''

        with open(self.arquivo_consultas, 'a+') as f:
            for linha in f.readlines():
                codigo, procedimentos, paciente = linha[:-1].split(',')

                if codigo == codigo_consulta:
                    return codigo, procedimentos.split(';'), paciente # TODO: retornar classe

        print('Consulta nao encontrado')
        return None, None


    def editar_consulta(self, codigo_consulta, codigos_procedimentos=None, id_paciente=None):
        '''Le arquivo de consultas e substitui a linha correspondente
        ao codigo passado com os dados passados'''

        linhas = None

        with open(self.arquivo_consultas, 'r') as f:
            linhas = f.readlines()

        for i in range(len(linhas)):
            codigo, procedimentos, paciente = linhas[i][:-1].split(',')

            if codigo == codigo_consulta:
                linhas[i] = f'{codigo_consulta},{";".join(codigos_procedimentos) or procedimentos},{id_paciente or paciente}\n'

        # TODO: mostrar mensagem sobre codigo inexistente
        with open(self.arquivo_consultas, 'w') as f:
            f.writelines(linhas)


    def remover_consulta(self, codigo_consulta):
        '''Le arquivo de consultas e remove linha correspondente ao
        codigo passado'''

        linhas = None

        with open(self.arquivo_consultas, 'r') as f:
            linhas = f.readlines()

        indice_consulta = None

        for i in range(len(linhas)):
            codigo, procedimentos, paciente = linhas[i][:-1].split(',')

            if codigo == codigo_consulta:
                indice_consulta = i

        if indice_consulta == None:
            print('Consulta nao encontrada')
            return

        del linhas[indice_consulta]

        with open(self.arquivo_consultas, 'w') as f:
            f.writelines(linhas)


    def remover_consulta_do_paciente(self, id_paciente):
        '''Le arquivo de consultas e remove linha que contem o
        paciente correspondente ao codigo passado'''

        linhas = None

        with open(self.arquivo_consultas, 'r') as f:
            linhas = f.readlines()

        indices_consultas = []

        for i in range(len(linhas)):
            codigo, procedimentos, paciente = linhas[i][:-1].split(',')

            if paciente == id_paciente:
                indice_consulta.append(i)

        for indice_consulta in indices_consultas:
            del linhas[indice_consulta]

        with open(self.arquivo_consultas, 'w') as f:
            f.writelines(linhas)


    def remover_consulta_do_procedimento(self, codigo_procedimento):
        '''Le arquivo de consultas e remove linha que contem o
        procedimento correspondente ao codigo passado'''

        linhas = None

        with open(self.arquivo_consultas, 'r') as f:
            linhas = f.readlines()

        indices_consultas = []

        for i in range(len(linhas)):
            codigo, procedimentos, paciente = linhas[i][:-1].split(',')

            if codigo_procedimento in procedimentos.split(';'):
                indice_consulta.append(i)

        for indice_consulta in indices_consultas:
            del linhas[indice_consulta]

        with open(self.arquivo_consultas, 'w') as f:
            f.writelines(linhas)
