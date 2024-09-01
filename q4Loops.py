'''x = int(input("q4 part a input(integer): "))

print("Using for loop:\n")
for i in range(x, 0, -1):
	print(' ' * (x-i) + '*' * (i) + '\n', end = '')

print("\nUsing while loop:\n")
j = x
while j > 0:
	print(' ' * (x-j) + '*' * (j) + '\n', end = '')
	j = j - 1
'''

def LtrPttrn_for(y):
	print("Using for loop: \n")
	for i in range(1, y+1):
		for k in range(i):
			print(chr(k+65), end = '')
		print('\n', end = '')

LtrPttrn_for(int(input("q4 part b input(integer): ")))

def LtrPttrn_while(x):
	a = 1
	print("\nUsing while loop: \n")
	while a <= x:
		b = 0
		while b < a:
			print(chr(b + 65), end = '')
			b += 1
		print('\n', end = '')
		a += 1

LtrPttrn_while(int(input("q4 part b input(integer): ")))
