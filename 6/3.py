# (М.В. Кузнецова) Определите, при каком наибольшем введённом значении переменной s программа выведет число 128.
# var s, n: integer;
# begin
#   readln (s);
#   n := 1;
#   while s < 94 do begin
#     s := s + 8;
#     n := n * 2
#   end;
#   writeln(n)
# end.

def func(s):
	n = 1
	while s < 94:
		s += 8
		n *= 2
	return n

s = 1
while True:
	if func(s) == 128:
		print(s)
	s += 1