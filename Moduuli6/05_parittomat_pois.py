# Ohjelmisto 1 - Moduuli 6 - Tehtävä 5 - Parittomat pois

def p_parittomat(lista):
    parilliset = []
    for alkio in lista:
        if alkio % 2 == 0:
            parilliset.append(alkio)
    return parilliset

lista_numeroita = []

while True:
    luku = input("Anna positiivisia kokonaislukuja: ")
    if luku == "" or luku == " ":
        break
    numero = int(luku)
    if numero < 0:
        break
    lista_numeroita.append(numero)

print(f"Alkuperäinen lista: {lista_numeroita}")
print(f"Parilliset ilman parittomia: {p_parittomat(lista_numeroita)}")
