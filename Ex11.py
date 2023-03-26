numeros = input("Digite uma lista de números separados por vírgula: ")
numeros = numeros.split(",") 
soma = 0 

for numero in numeros:
    if int(numero) % 2 != 0:
        soma += int(numero)

print("A soma de todos os números ímpares na lista é: ", soma)
