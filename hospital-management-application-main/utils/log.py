from datetime import datetime

arquivo_log = '\out\log.csv'

class Log:
    @staticmethod
    def registrar_log(mensagem):
        with open(arquivo_log, 'a') as f:
            f.write(f"[{datetime.today()}] {mensagem}\n")