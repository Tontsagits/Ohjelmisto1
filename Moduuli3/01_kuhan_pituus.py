# Moduuli 3 - Tehtävä 1 - Kuhan pituus, ehtolause if


kuhan_pituus = float(input('Anna Kuhan pituus (cm): '))

if kuhan_pituus < 37:
    alamittaisuus = 37 - kuhan_pituus
    print(f"Kuha on {alamittaisuus:.1f} cm alamittainen, päästä se takaisin veteen.")
else:
    print("Kuha on riittävän iso. Voit pitää sen.")

