x = input("Введите словов на русском: ")
glas = ["у","е","ы","а","о","э","я","и","ю", "ё"]
soglas = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "р", "н", "п", "c", "т", "ф", "ч", "ц", "щ", "ш", "х", "ь"]
countsoglas = 0
countglas = 0

for j in x:
    if j in glas:
        countglas +=1
for k in x:
    if k in soglas:
        countsoglas +=1

print(len(x))
print(countsoglas)
print (countglas)
