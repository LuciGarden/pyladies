from random import randrange

tah_pc = randrange(3)
tah_cloveka = input("Vyber si kameň, nožnice alebo papier: ")

if tah_pc == 0:
    tah_pc = "kameň"
    print("Počítač zahral kameň")
elif tah_pc == 1:
    tah_pc = "nožnice"
    print("Počítač zahral nožnice")
else:
    tah_pc = "papier"
    print("Počítač zahral papier")

if tah_cloveka == tah_pc:
    print("Remíza")
elif ((tah_cloveka == "kameň") and (tah_pc == "nožnice")) or ((tah_cloveka == "nožnice") and (tah_pc == "papier")) or ((tah_cloveka == "papier") and (tah_pc == "kameň")):
    print("Vyhral/a si!")
else:
    print("Prehral/a si!")
