import csv

skaits = {}

with open("sistema.log", encoding="utf-8") as f:
    for rinda in f:
        dalas = rinda.split()
        if dalas[2] == "ERROR":
            serviss = dalas[3].rstrip(":")
            if serviss in skaits:
                skaits[serviss] = skaits[serviss] + 1
            else:
                skaits[serviss] = 1
with open("servisi.csv", mode="w", encoding="utf-8-sig", newline="") as f:
rakstitajs = csv.writer(f)
rakstitajs.writerow(["Serviss", "Kļūdas"])
for serviss, kluudas in skaits.items():
rakstitajs.writerow([serviss, kluudas])
