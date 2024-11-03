x = input("Введите словов на русском: ")
glas = ["у","е","ы","а","о","э","я","и","ю", "ё"]
soglas = ["й","ц","к","н","г","ш","щ","з","х","ъ","ж","д","л","р","п","в","ф","ч","с","м","т","б","ь",]
countsoglas = 0
countglas = 0
for i in x:
    for j in glas:
        if i == j:
            countglas +=1
        else:
            countsoglas +=1
            
print(len(x))
print(countsoglas)
print (countglas)


