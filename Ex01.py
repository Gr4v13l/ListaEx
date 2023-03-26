numeros = input("Digite uma lista de números, separados por vírgula: ")
lista = numeros.split(",")

for numero in lista:
    numero = int(numero)
    if numero % 2 == 0:
        print(numero)

    