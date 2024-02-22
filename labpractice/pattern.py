print('Triangle') #Alex Raduenz Nested Loops and Input Validation Practice
for a in range(5, 0, -1):
	for b in range(a):
		print('*', end=' ')
	print()
print('Pyramid')
for c in range(5):
	for d in range(5-c-1):
		print(' ', end='')
	for e in range(2*c+1):
		print('*', end='')
	print()

#Extra Credit
print('Diamond')
for f in range(5):
	for g in range(5-f-1):
		print(' ', end='')
	for h in range(2*f+1):
		print('*', end='')
	print()

for f in range(4, 0, -1):
	for g in range(5-f):
		print(' ', end='')
	for h in range(2*f-1):
		print('*', end='')
	print()
