numeros = input("Digite uma série de números separados por vírgula: ")
numeros = [int(numero) for numero in numeros.split(",")]
nova_lista = []

for numero in numeros: 
    if numero %3 == 0:
        nova_lista.append(numero)

print(nova_lista)