numero = list()
for cont in range(0,5):
    numero.append(int(input('Digite um valor: ')))


numero.sort(reverse=True)
print('A ordem decrescente é: ',numero)