l=int(input("Enter the limit for the first list"))
l2=int(input("Enter the limit for the second list"))
a = []
b = []
c = []
d = []
for i in range(l):
	inp=int(input("Enter the value for first list"))
	a.append(inp)
for i in range(l2):
	inp=int(input("Enter the value for second list"))
	b.append(inp)

a.sort()
b.sort()
c.sort()
d.sort()
if(len(a)==len(b)):
	print("a is equal to b in length")
else:
	print("a is not equal to b in length")

if(sum(a)==sum(b)):
	print("Sum of a is equal to b ")
else:
	print("Sum of a is not equal to b")

com=set(a).intersection(b)
if com:
	print("Common elements present and they are ",com)
else:
	print("No Common elements ")
