from datetime import date

arquivo_log = 'log.csv'

class Log:
    @staticmethod
    def registrar_log(mensagem):
        with open(arquivo_log, 'a') as f:
            f.write(f"[{date.today()}] {mensagem}\n")