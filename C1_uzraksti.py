import sys

if len(sys.argv) < 2:
   print("Lietošana: python C1_uzraksti.py ")
   print("Piemērs: python C1_uzraksti.py WARNING")
sys.exit()

līmeni = sys.argv[1].upper()
skaits = 0
atlasitās_rindas = []

with open("sistema.log", encoding="utf-8") as f:
    for rinda in f:
dalas = rinda.split()
      if len(dalas) > 2 and dalas[2] == līmeni:
skaits += 1
atlasitās_rindas.append(rinda)

print("Atrasts:", skaits)

with open(iznākuma_fails, "w", encoding="utf-8") as f:
f.writelines(atlasitās_rindas)
