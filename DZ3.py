a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
print("Кратно (7): ")
for i in range(a, b):
   if i % 7 == 0:
       print(i, end=' ')