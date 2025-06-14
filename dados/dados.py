import json
from dados import funcoes

def salvar(lista):
    with open('dados.json', 'w', encoding='utf-8') as arq:
        json.dump(lista, arq, indent=4)


def carregar():
    try:
        with open('dados.json', 'r', encoding='utf-8') as arq:
            return json.load(arq)
    except FileNotFoundError:
        return []


def dict():
    dados = {}
    dados['nome'] = str(input('nome: '))
    dados['idade'] = funcoes.leiaint('Idade: ')
    lis.append(dados.copy())
    print('\033[32mCadastro realizado com sucesso!\033[m')
    dados.clear


lis = carregar()
