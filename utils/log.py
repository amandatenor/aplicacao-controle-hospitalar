from datetime import datetime

arquivo_log = './out/log.csv'

class Log:

    @staticmethod
    def registrar_log(mensagem):
        with open(arquivo_log, 'a') as f:
            data_hora_atual = datetime.today().strftime('%d/%m/%Y %H:%M:%S')
            f.write(f"[{data_hora_atual}] {mensagem}\n")


