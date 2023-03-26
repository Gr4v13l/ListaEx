palavras = input("Digite uma lista de palavras separadas por vírgulas: ")

palavras = [palavra.strip() for palavra in palavras.split(",")]

impares = [palavra for palavra in palavras if len(palavra) % 2 == 1]

print("Palavras com número ímpar de letras:", impares)
