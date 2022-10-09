print("Odpovedaj ano alebo nie.")

stastna = input("Si šťastná?")
bohata = input("Si bohatá?")

if stastna == "ano":
    if bohata == "ano":
        print("Super, to ti prajem!")
    if bohata == "nie":
        print("Viac šetri.")
else:
    if stastna == "nie":
        if bohata == "nie":
            print("To ma mrzí, teš sa z maličkostí.")
        if bohata == "ano":
            print ("Kúp si zmrzlinu, to ťa rozveselí.")
