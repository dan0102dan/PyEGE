# Исполнитель А16 преобразует число, записанное на экране.
# У исполнителя есть три команды, которым присвоены номера:
# 1. Прибавить 1
# 2. Прибавить 2
# 3. Умножить на 2
# Первая из них увеличивает число на экране на 1, вторая увеличивает его на 2, третья умножает его на 2.
# Программа для исполнителя А16 – это последовательность команд.
# Сколько существует таких программ, которые исходное число 3 преобразуют в число 12 и при этом траектория вычислений программы содержит число 10?
# Траектория вычислений программы — это последовательность результатов выполнения всех команд программы. Например, для программы 132 при исходном числе 7 траектория будет состоять из чисел 8, 16, 18.

def f(n, m):
	if n < m:
		return f(n + 1, m) + f(n + 2, m) + f(n * 2, m)
	elif n == m:
		return 1
	else:
		return 0

print(f(3, 10) * f(10, 12))