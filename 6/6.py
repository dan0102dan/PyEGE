# (М.В. Кузнецова) Определите, при каком наименьшем введённом значении переменной s программа выведет число 96.
# var s, n: integer;
# begin
#   readln (s);
#   n := 3;
#   while s <= 51 do begin
#     s := s + 7;
#     n := n * 2
#   end;
#   writeln(n)
# end.

def func(s):
	n = 3
	while s <= 51:
		s += 7
		n *= 2
	return n

s = 0
while True:
	if func(s) == 96:
		print(s)
	s += 1