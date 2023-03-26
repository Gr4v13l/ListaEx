lista = input("Digite uma sequência de números podendo ter repetição e separados por vírgula: ")
lista = lista.split(",")
lista_nova = []

while lista:
    elemento = lista.pop(0)
    if elemento not in lista_nova:
        lista_nova.append(elemento)

print("A lista nova é: ",lista_nova)