numero = list()
for cont in range(0,5):
    numero.append(int(input('Digite um valor: ')))
    
numero.sort()
print(numero)
print('O segundo menor número é',numero[1])