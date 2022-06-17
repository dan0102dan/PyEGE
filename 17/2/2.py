# Файл содержит последовательность неотрицательных целых чисел, не превышающих 10 000. Назовём тройкой три идущих подряд элемента последовательности. Определите количество троек чисел таких, которые могут являться сторонами остроугольного треугольника. В ответе запишите два числа: сначала количество найденных троек, а затем — максимальную сумму элементов таких троек. Если таких троек не найдётся — следует вывести 0 0.

with open('17.txt') as f:
    data = list(map(int, f.readlines()))

res = []
for i in range(len(data) - 2):
    st = sorted([data[i], data[i + 1], data[i + 2]])
    if st[0]**2 + st[1]**2 > st[2]**2:
        res.append(sum(st))
print(len(res), max(res))