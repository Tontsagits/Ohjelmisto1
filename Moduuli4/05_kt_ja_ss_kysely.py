# Ohjelmisto 1 - Moduuli 4 - Tehtävä 5 - Käyttäjätunnus ja salasana kysely

k_tunnus = ''
s_sana = ''
kerrat = 1

while s_sana != 'rules' and k_tunnus != 'python' and kerrat <= 5:
    k_tunnus = input('Anna käyttäjätunnus: ')
    s_sana = input('Anna salasana: ')
    kerrat += 1
    if k_tunnus == 'python' and s_sana == 'rules':
        print('Tervetuloa!')
        break
    else:
        print('Pääsy evätty!')
