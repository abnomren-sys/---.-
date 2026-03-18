x = int(input("Введите начало диапазона:"))
y = int(input("Введите конец диапазона:"))

fib = [0, 1]
while fib[-1] <= y:
    next_fib = fib[-1] + fib[-2]
    fib.append(next_fib)

result = []
for num in fib:
    if x <= num <= y:
        result.append(num)

if result:
    print("Числа Фибоначчи в диапазоне:", result)
else:
    print("В заданном диапазоне нет чисел Фибоначчи")

