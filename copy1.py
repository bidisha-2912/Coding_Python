a=[2,5,4,1]
b=a
c=a.copy()#shallow copy
b.append(3)
c.append(12)
print(a)
print(b)
print(c)
