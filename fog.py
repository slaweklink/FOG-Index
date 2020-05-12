print("Wpisz lub wklej tekst do sprawdzenia: ")
tekst = input()

slowa = tekst.split()
ilosc_slow = len(slowa)

zdania = 0
kropki = tekst.count(".")
wykrzykniki = tekst.count("!")
znakizapytania = tekst.count("?")

zdania = kropki + wykrzykniki + znakizapytania

dlugie_slowa = 0
for i in slowa:
    if len(i) >= 8:
        dlugie_slowa += 1

print(ilosc_slow)
print(zdania)
print(dlugie_slowa)
Fog = 0.4 * (int(ilosc_slow/zdania) + 100*int(dlugie_slowa/ilosc_slow))
print(int(Fog))
