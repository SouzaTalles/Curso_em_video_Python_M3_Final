def aumentar(n, q, mos=False):
    p = 1
    q = q / 100
    q = q + p
    n *= q
    if mos == True:
      n = (f'R${n}')
    return n  
    


def diminuir(n, q, mos=False):
    p = 1
    q = q / 100
    q = p - q
    n *= q
    if mos == True:
      n = (f'R${n}')
    return n


def dobro(n, mos=False):
    n *= 2
    if mos == True:
      n = (f'R${n}')
    return n


def metade(n, mos=False):
    n /= 2
    if mos == True:
      n = (f'R${n}')
    return n


def moeda(n):
    n = (f'R${n}')
    return n


def resumo(n, p1, p2):
    print("-" * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print("-" * 40)
    print(f'{"Preço analisado:":<20}{moeda(n):>20}')
    print(f'{"Dobro do preço:":<20}{dobro(n, True):>20}')
    print(f'{"Metade do preço:":<20}{metade(n, True):>20}')
    print(f'{f"{p1}% de aumento:":<20}{aumentar(n, p1, True):>20}')
    print(f'{f"{p2}% de redução:":<20}{diminuir(n, p2, True):>20}')
    print("-" * 40)
