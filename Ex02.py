lista_palavra = input("Digite uma lista de palavra: ")
lista_palavra = lista_palavra.split(", ")

for palavra in lista_palavra:
    if palavra.startswith("a") or palavra.startswith("A"):
        print(palavra)