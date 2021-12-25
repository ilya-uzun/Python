
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
