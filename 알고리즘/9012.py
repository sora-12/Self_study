import sys




def check(lists):
	stack=[]
	for j in lists:

		if j=='(':
			stack.append('(')
		else:
			if stack:
				stack.pop()
			else:
				return 'NO'
	if stack:
		return 'NO'
	else:
		return 'YES'



q = lambda : sys.stdin.readline().strip()
num_lines=int(q())
for i in range(num_lines):
	lists=q()
	print(check(lists))

