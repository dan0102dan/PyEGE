# Световое табло состоит из цветных индикаторов. Каждый индикатор может окрашиваться в четыре цвета: белый, синий, желтый и красный. Какое наименьшее количество лампочек должно находиться на табло, чтобы с его помощью можно было передать 300 различных сигналов при условии, что гореть должны все лампочки?

N = 1
while 4 ** N < 300:
    N += 1
print(N)