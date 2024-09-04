# Ohjelmisto 1 - Moduuli 6 - Tehtävä 4 - Lukujen summa

def k_summa(lista):
    return sum(lista)

lista_numeroita = []

while True:
    luku = input("Anna positiivisia kokonaislukuja: ")
    if luku == "" or luku == " ":
        break
    numero = int(luku)
    if numero < 0:
        break
    lista_numeroita.append(numero)

print(f"Summa {k_summa(lista_numeroita)}")
