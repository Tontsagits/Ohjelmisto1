#  Funktioiden testausta

def tervehdi(kerrat):
    for i in range(kerrat):
        print ("Hyvää päivää " + str(i+1) + ". kerran")
    return

print ("Päivä alkaa tervehdyksillä.")
print("Tervehditään viisi kertaa")
tervehdi(5)
print ("Tervehditään vielä 2 kertaa lisää.")
tervehdi(2)

