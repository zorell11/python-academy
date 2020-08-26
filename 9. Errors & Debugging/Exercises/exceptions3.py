try:
    #Místo kde vznikne chyba.
    produkt = 123 / (23*0)

#Urči typ chyby a vytvoř alias.
except ZeroDivisionError as nula:
    typ = type(nula).__name__
    print(typ)
    zprava = nula.args[0]
    print(zprava)
    radek = typ + ': ' + zprava
    print(radek)
    print(nula.__class__)
    print(nula.args)
