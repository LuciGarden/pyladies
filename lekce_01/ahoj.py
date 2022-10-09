print('Ahoj!')
strana = float(input('Zadaj stranu stvorca: ')) # v centimetroch
cislo_je_spravne = strana > 0

if cislo_je_spravne:
    print('Obvod stvorca so stranou', strana, 'je', 4 * strana)
    print('Obsah stvorca so stranou', strana, 'je', strana * strana)
else:
    print('Strana musi byt kladna, inak z toho nebude stvorec')

print('Dakujeme za pouzitie kalkulacky')
