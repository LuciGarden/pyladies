retazec = input("Zadaj pôvodný reťazec: ") #V zivote som toho uz vela dokazala.
pozicia = int(input("Na akej pozícii spravíme výmenu? ")) #-4
znak = input("Aký znak tam dáme? ") #i

print("Po výmene to vyzerá takto: ") #ups :)))
print(retazec[:pozicia] + znak + retazec[pozicia + 1:])
