limit=int(input("Enter the no of terms :"))
n1,n2=0,1
c=0
if limit<=0:
	print("Please enter a positive number :")
elif limit==1:
	print("Fibonacci : ")
	print(n1)
else:
	print("Fibonacci ")
	while c < limit:
		print(n1)
		nth=n1+n2
		n1=n2
		n2=nth
		c+=1
