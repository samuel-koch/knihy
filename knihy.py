# pridani knihy
def pridat_knihu(knihy):
    nazev = input("Zadej název knihy: ")
    autor = input(f"Zadej název autora knihy {nazev}: ")
    rok = int(input(f"Zadej rok vydání knihy {nazev}: "))

    knihy[nazev] = {"autor": autor, "rok": rok}
    print(f"Kniha {nazev} byla přidána.")

# najdi knihu
def najdi_knihu(knihy):
    nazev = input("Zadej název hledané knihy: ")
    if nazev in knihy:
        print(f"Kniha {nazev} je v knihovně. Autor: {knihy[nazev]["autor"]}, Rok: {knihy[nazev]["rok"]}")
    else:
        print("Kniha není v knihovně.")





# hlavni program
def hlavni_program():
    knihy = {}
    while True:
        print("\nVyberte akci: ")
        print("1. Přidat knihu")
        print("2. Najít knihu")
        volba = input("Zadejte číslo akce: ")
        if volba == "1":
            pridat_knihu(knihy)
        elif volba == "2":
            najdi_knihu(knihy)
        else:
            print("Konec programu.")
            exit()

hlavni_program()