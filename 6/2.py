# При каком наибольшем введенном числе d после выполнения программы будет напечатано 55?
# var n, s, d: integer;
# begin
#   readln(d);
#   n := 0;
#   s := 0;
#   while s <= 365 do begin
#     s := s + d;
#     n := n + 5
#   end;
#   write(n)
# end.

def func(d):
	n = 0
	s = 0
	while s <= 365:
		s += d
		n += 5
	return n

d = 1
while True: 
	if func(d) == 55:
		print(d)
	d += 1