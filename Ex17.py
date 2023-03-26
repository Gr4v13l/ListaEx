nomes = input("Digite uma lista de nomes separados por vírgulas: ")

nomes = [nome.strip() for nome in nomes.split(",")]

nomes_com_e = [nome for nome in nomes if "e" in nome.lower()]

print("Nomes com a letra 'e':", nomes_com_e)
