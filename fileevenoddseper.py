import os
f=open('nums.txt','r')    
file1=open('nums1.txt','w')
file2=open('nums2.txt','w')
num=f.readline().split(',')
nums=[int(i) for i in num]
for i in nums:
    if i%2==0:
        file1.write(str(i))
for i in nums:
    if i%2!=0:
        file2.write(str(i))
f.close()
file1.close()
file2.close()
