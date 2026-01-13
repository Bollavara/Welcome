#list comprehension
data=[1,2,3,4,5,6,2,4]
b=[x*x for x in data]
print(b)

#Set comprehension
c={x for x in data if x%2==0}
print(c)

#Dictionary Comprehension
d={x:x**3 for x in data}
print(d)

