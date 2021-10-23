# (М.В. Кузнецова) Определите, при каком наибольшем введённом значении переменной s программа выведет число 256.
# var s, n: integer;
# begin
#   readln (s);
#   n := 1;
#   while s <= 45 do begin
#     s := s + 4;
#     n := n * 2
#   end;
#   writeln(n)
# end.

def func(s):
	n = 1
	while s <= 45:
		s += 4
		n *= 2
	return n

s = 1
while True:
	if func(s) == 256:
		print(s)
	s += 1