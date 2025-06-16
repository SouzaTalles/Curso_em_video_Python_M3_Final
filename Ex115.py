from time import sleep
from dados import funcoes, dados

while True:
    print('-' * 40)
    print(f'{"MENU PRINTCIPAL":^40}')
    print('-' * 40)
    print('1 _ Ver pessoas cadastradas \n2 _ Cadastrar nova pessoa \n3 - Sair do sistema')
    print('-' * 40)

    op = funcoes.leiaint('Sua Opção: ')
    
    if op == 1:
        funcoes.listar(dados.lis)
        sleep(2)
    elif op == 2:

        dados.dict()
        dados.salvar(dados.lis)  # <- salvando os dados
        sleep(2)
    elif op == 3:
        break
    else:
        print('\033[31mERRO! Digite uma opção valida!\033[m')
print('-' * 40)
print(f'{"Saindo do sistema... Até logo!":^40}')
print('-' * 40)
