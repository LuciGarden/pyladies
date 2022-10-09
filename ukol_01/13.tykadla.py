tykadlo = int(input('Kolik mas tykadel? '))
if tykadlo == 0:
    print('Ahoj ze Zeme, neboj, pujcime ti par falesnych tykadel.')
elif tykadlo <= 2:
    print('Ahoj z Marsu!')
elif tykadlo <= 4:
    print('Ahoj z Jupiteru!')
elif tykadlo <= 8:
    print('Ahoj z Pluta!')
else:
    #nebola vybrana ani jedna zo situacii vyssie - cislo bolo zaporne alebo vyssie ako 8
    print('To neni mozne, propocitej si tykadla jeste jednou.')
