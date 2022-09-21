strana = int(input("Zadej stranu ctverce v cm: ")) # v cm
# strana - float(input("Zadej stranu ctverce v cm: ")) # v cm
cislo_je_spravne = strana > 0
if cislo_je_spravne:
    print ("Obvod čtverce se stranou" , strana , "cm je", strana * 4 , "cm")
    print ("Obsah čtverce se stranou" , strana , "cm je", strana * strana , "cm2")
else:
    print("Strana musí být kladná, jinak z toho nebude čtverec!")

print ("Děkujeme za použití geometrické kalkulačky.")

