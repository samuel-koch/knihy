# pridani knihy
def pridat_knihu(knihy):
    nazev = input("Zadej název knihy: ")
    autor = input(f"Zadej název autora knihy {nazev}: ")
    rok = int(input(f"Zadej rok vydání knihy {nazev}: "))

    knihy[nazev] = {"autor": autor, "rok": rok}
    print(f"Kniha {nazev} byla přidána.")

# najdi knihu
def najdi_knihu(knihy):
    nazev = input("Zadej nazev hledane knihy: ")
    if nazev in knihy:
        print(f"Kniha {nazev} je v knihovně. Autor: {knihy[nazev]["autor"]}, Rok: {knihy[nazev]["rok"]}")
    else:
        print("Kniha není v knihovně.")





# hlavni program
def hlavni_program():
    knihy = {}
    pridat_knihu(knihy)

hlavni_program()