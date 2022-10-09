from random import randrange

sucet = 0
while sucet < 21:
    print("Dohromady to je", sucet, "bodov")
    odpoved = input("Chceš kartu? ")
    if odpoved == "áno":
        karta = randrange(2, 11)
        print("Karta má", karta, "bodov")
        sucet = sucet + karta
    elif odpoved == "nie":
        print("Koniec hry. Prehral si.")
        break
    else:
        print('Odpovedaj pomocou "áno" alebo "nie".')

if sucet == 21:
    print("Vyhral si. Dohromady to je", sucet, "bodov.")
elif sucet > 21:
    print("Prehral si, počet bodov je vyšší než 21.")
