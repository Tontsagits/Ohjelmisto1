# Ohjelmisto 1 - Moduuli 5 - Tehtävä 3 - Onko luku alkuluku

luku = "0"
testattava = 0

while luku != "" and luku != " ":
    luku = input("Anna positiivinen kokonaisluku (tyhjä lopettaa): ")
    if luku != "" and luku != " " and luku.isnumeric():
        testattava = int(luku)
        if testattava == 1:
            print(f"Luku {testattava} ei ole alkuluku.")
        elif testattava < 1:
            print("Anna positiivinen kokonaisluku.")
        elif testattava > 1:
            onko_alkuluku = True
            for i in range(2,testattava):
                # print(f"{testattava} / {i} = {testattava/i}")
                if testattava % i != 0:
                    onko_alkuluku = False
            if onko_alkuluku:
                print(f"Luku {testattava} on alkuluku.")
            else:
                print(f"Luku {testattava} ei ole alkuluku.")
