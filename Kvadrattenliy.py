
import math
a=float(input('a: ')) 
b=float(input('b: ')) 
c=float(input('c: ')) 
d=b**2-4*a*c
if d>0:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print('x1=',x1)
    print('x2=',x2)
elif d==0:
    x1=-b/(2*a)
    print('x1=x2=',x1)
else:
    print('həqiqi kökləri yoxdur')