# Сколько единиц содержится в двоичной записи значения выражения: 8^2020 + 4^2017 + 26 – 1?

result = bin(8**2020 + 4**2017 + 26 - 1)[2:]

print(result.count('1'))