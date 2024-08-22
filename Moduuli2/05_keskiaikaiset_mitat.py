# Moduuli 2 - 5 Keskiaikaiset mitat

'''
Yksi leiviskä on 20 naulaa.
Yksi naula on 32 luotia.
Yksi luoti on 13,3 grammaa.
'''

leiviska = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))
print("Massa nykymittojen mukaan:")
massa = leiviska*20*32*13.3 + naulat*32*13.3 + luodit*13.3
print(massa) # massan tarkastus
print(f"{massa/1000:.0f} kilogrammaa ja {((massa/1000) - int(massa/1000)) * 1000:.2f} grammaa.")
