x = input("Введи строку: ")
glas = "аеёиоуыэюя"
soglas = "бвгджзйклмнпрстфхцчшщ"

glas_count = 0
soglas_count = 0

for i in x.lower():
  if i in glas:
    glas_count += 1
  elif i in soglas:
    soglas_count += 1

print("Длина строки ", len(x))
print("Гласных в строке ", glas_count)
print("Согласных в строке ",  soglas_count)
