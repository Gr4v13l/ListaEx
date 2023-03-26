nomes = input("Digite uma lista de nomes separados por vírgulas: ")

nomes = [nome.strip() for nome in nomes.split(",")]

nome_verificar = input("Digite o nome a ser verificado: ")

if nome_verificar in nomes:
    print("O nome está na lista")
else:
    print("O nome não está na lista")
