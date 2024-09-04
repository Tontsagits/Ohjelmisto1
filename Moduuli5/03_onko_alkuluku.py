# Ohjelmisto 1 - Moduuli 5 - Tehtävä 3 - Onko alkuluku

luku = "0"
testaus = 0

while luku != "" and luku != " ":
    luku = input("Anna positiivinen kokonaisluku (tyhjä lopettaa): ")
    if luku != "" and luku != " " and luku.isnumeric():
        testaus = int(luku)
        if testaus == 1:
            print("Luku 1 ei ole alkuluku.")
        elif testaus < 1:
            print("Anna positiivinen kokonaisluku.")
        elif testaus > 1:
            for i in range(2,testaus):
                # testataan onko annettu luku alkuluku
                # saa olla jaollinen vain itsellään (ja tietysti luvulla 1)
                # muuten ei ole alkuluku
                if testaus % i == 0:
                    print(f"Luku {testaus} on alkuluku.")
                else:
                    print(f"Luku {testaus} ei ole alkuluku.")
