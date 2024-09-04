# Ohjelmisto 1 - Moduuli 5 - Tehtävä 2 - Viisi suurinta lukua

luku = "0"
luvut = []

while luku != "" and luku != " ":
    luku = input("Anna kokonaisluku (tyhjä lopettaa): ")
    if luku != "" and luku != " " and luku.isnumeric():
        luvut.append(int(luku))
luvut.sort(reverse=True)
print(luvut[:5])
