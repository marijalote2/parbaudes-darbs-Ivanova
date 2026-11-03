skaits = 0

with open("sistema.log", encoding="utf-8") as f:
for rinda in f:
dalas = rinda.split()
if len(dalas) > 2 and dalas[2] == "WARNING":
skaits = skaits + 1

print(skaits)
