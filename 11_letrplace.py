string=input("enter string")
f_c=string[0]
l_c=string[-1]
m_c=string[1:-1]
if len(string)<=1:
	print("new string is ",string)
n_s=l_c+m_c+f_c
print("new string is ",n_s)
