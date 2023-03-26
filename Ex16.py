numeros = input("Digite uma lista de números separados por vírgulas: ")

numeros = [int(numero) for numero in numeros.split(",")]

frequencia = {}
for numero in numeros:
    if numero not in frequencia:
        frequencia[numero] = 1
    else:
        frequencia[numero] += 1

numeros_repetidos = [numero for numero in frequencia if frequencia[numero] > 1]

print("Números repetidos:", numeros_repetidos)
