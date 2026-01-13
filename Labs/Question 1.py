for i in range(1,21):
    print(i)

n=[1,2,3,4,5,6,7,8,9,10]
even=filter(lambda x:x%2==0,n)
for num in even:
    print(num)

a=filter(lambda x:x%2==0,n) #Even numbers
z=map(lambda x:x*x,a) #Square numbers
for num in z:
    print(num)

from functools import reduce
n=[1,2,3,4,5,6,7,8,9,10]
even=filter(lambda x:x%2==0,n)
a=filter(lambda x:x%2==0,n) #Even numbers
z=map(lambda x:x*x,a) #square numbers
result=reduce(lambda x,y:x+y,z) #sum of squared numbers
print(result)

d=[4,16,36,64,100]
for index, value in enumerate (d):
    print(index,value)



