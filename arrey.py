from array import * # импорт класса array


# Создаем пустой список
arr = []
for i in range(1,18):
    if (i % 15 == 0):
        arr.append('FizzBuzz')
    elif i % 5 == 0:
        arr.append('Fizz')
    elif i % 3 == 0:
        arr.append('Buzz')
    else:
        arr.append(i)

for i in arr:
    print(i)

# range - генерирует числа от 1 до 17 для цикла
# arr.append - добавит элемент в конец списка


arr2 = array('i', []) # Создаем пустой массив натуральных чисел

for i in range(1,18):
    if (i % 15 == 0):
        arr2.append(0)
    elif i % 5 == 0:
        arr2.append(1)
    elif i % 3 == 0:
        arr2.append(2)
    else:
        arr2.append(i)

for i in arr2:
    print(i)

