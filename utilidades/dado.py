def leiadinheiro(msg=''):
    válido = False
    while True:
        entrada = str(input(msg)).replace(',', '.').strip()
        # Verifica se há apenas números e no máximo um ponto
        if entrada.isalpha() or entrada == '':
             print(f'\033[31mErro! "{entrada}" não é um valor monetário válido.\033[m')
        else:
            válido = True
            return float(entrada)


def leiaint(msg):
    while True:
        entrada = str(input(msg)).strip()
        if entrada == '':
            print('\033[31mO usuário não quis informar esse número.\033[m')
            return 0
        try:
            numero = int(entrada)
            return numero
        except ValueError:
            print('\033[31mErro! Digite um número inteiro válido.\033[m')


def leiafloat(msg=''):
    while True:
        entrada = str(input(msg)).strip()
        if entrada == '':
            print('\033[31mO usuário não quis informar esse número.\033[m')
            return 0
        try:
            numero = float(entrada)
            return numero
        except ValueError:
            print('\033[31mErro! Digite um número inteiro válido.\033[m')
