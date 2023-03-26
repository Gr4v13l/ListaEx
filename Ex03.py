
numeros = input("Digite uma lista de números separados por vírgulas: ")

lista_numeros = [int(num) for num in numeros.split(",")]

numero_maximo = max(lista_numeros)
numero_minimo = min(lista_numeros)

print("O número máximo é:", numero_maximo)
print("O número mínimo é:", numero_minimo)

