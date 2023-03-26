numeros = input("Digite uma lista de números, separados por vírgula: ")
lista = numeros.split(",")

for numero in lista:
    numero = int(numero)
    if numero < 5:
        print(numero)