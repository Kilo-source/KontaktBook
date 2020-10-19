
kontakti = open('kontakti.txt', '+a')

#adadakontakti.write("IME - PEZIME - EMAIL - TELEFON - MESTO STANOVANJA\n")
odgovor = input("Da li zelite da unesete Kontakt? (da/Ne): ")

if odgovor.upper().strip() == 'DA':
    ime = input("Unesite Ime Kontakta: ")
    ime = str(ime)
    prezime = input("Unesite Prezime Kontakta: ")
    prezime = str(prezime)
    telefon = input("Unesite broj telefona: ")
    telefon = str(telefon)
    email = input("Unesite e mail kontakta: ")
    email = str(email)
    ulica = input("Unesite ulicu i broj kontakta: ")
    ulica = str(ulica)
else:
    print("Hvala vam sto ste bar usli :D")
    quit()

unos = (ime + " - " + prezime + ' - ' + telefon + ' - ' + email + ' - ' + ulica + "\n")
kontakti.write(unos)
print("Kontakt je uspesno unet!!!")
kontakti.close()