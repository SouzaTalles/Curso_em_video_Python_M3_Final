from dados import dados

def listar(l):
    print('-' * 40)
    print(f'{"PESSOAS CADASTRADAS":^40}')
    print('-' * 40)
    for c in l:
        print(f'{c['nome']:<30}{c['idade']:>10}')
    
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
            print('\033[31mErro! Digite uma idade válida.\033[m')
