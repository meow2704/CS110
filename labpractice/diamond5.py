n=6
p=6
for i in range(n):
	row=" "
	for j in range(n):
		if j>=p:
			row += "x"
		if j<p:
			row += "o"
	p -= 1
	print(row)