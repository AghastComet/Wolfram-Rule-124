def part(p,q,r):
	p=int(p)
	q=int(q)
	r=int(r)
	s=(p+q+p*q+p*q*r)%2
	return s

def step(line):
	newL=[]
	for i in range(len(str(line))+1):
		p=list(str(line))[i-1]
		try:
			q=list(str(line))[i]
		except IndexError:
			q=0
		try:
			r=list(str(line))[i+1]
		except IndexError:
			r=0
		if i-1 == -1:
			p=0
		newL+=[str(part(p,q,r))]
	newL = "".join(newL)
	return newL

itr = int(input("Iterations: "))
start = input("Initial Sequance(must be 1's and 0's): ")
print()
for i in range(itr):
	start = step(start)
print('Actual Output:',start) #pure output
print('Base 10 Output:',int(str(start),2)) #convert ouput to base 10 first