#  Funktioiden testausta

# funktion parametrit
def tervehdi(kerrat):
    for i in range(kerrat):
        print ("Hyvää päivää " + str(i+1) + ". kerran")
    return

print ("Päivä alkaa tervehdyksillä.")
print("Tervehditään viisi kertaa")
tervehdi(5)
print ("Tervehditään vielä 2 kertaa lisää.")
tervehdi(2)

# funktion sisäiset, paikalliset muuttujat ja globaalit muuttujat
def vaihda():
    kaupunki = "Vantaa"
    print("Funktiossa lopuksi: " + kaupunki)
    return

kaupunki = "Helsinki"
print("Pääohjelmassa aluksi: " + kaupunki)
vaihda()
print("Pääohjelmassa lopuksi: " + kaupunki)
