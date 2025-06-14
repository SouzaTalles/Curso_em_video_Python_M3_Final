import moeda

n = float(input('Digite o preço: R$'))
print(f'A metade de {n} é {moeda.metade(n)}')
print(f'O dobro de {n} é {moeda.dobro(n)}')
print(f'Aumentando 10%, temos {moeda.aumentar(n, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(n, 13)}')
