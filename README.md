# Python
#### Comments
> тестовое задание на работу       


~~~
arr = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for i in range(len(arr)):
    if (i % 5 == 0 and i % 3 == 0):
        arr[i] = 'FrizzBuzz'
    elif i % 5 == 0:
        arr[i] = 'Frizz'
    elif i % 3 == 0:
        arr[i] = 'Buzz'

for i in arr:
    print(i) 
~~~
