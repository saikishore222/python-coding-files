n=int(input())
for i in range(n):
	p=int(input())
	k=0
	m=p
	for i in range(p):
			k+=1
			if(m==0):
				break
			if(k%2==0):
				m-=1
			else:
				m-=2
	if(k%2==0):
		print("CAPTIAN AMERICA")
	else:
		print("IRON MAN")
