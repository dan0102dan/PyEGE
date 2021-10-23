# Определите, при каком наименьшем введённом значении переменной s программа выведет число 64.
# var s, n: integer;
# begin
#   readln (s);
#   n := 1;
#   while s < 51 do begin
#     s := s + 5;
#     n := n * 2
#   end;
#   writeln(n)
# end.

def func(s):
	n = 1

	while s < 51:
		s += 5
		n *= 2
	return n

s = 1
while True:
	if (func(s) == 64):
		print(s)
	s += 1