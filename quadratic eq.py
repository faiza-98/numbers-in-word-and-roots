import math
def quadratic(a,b,c):
    d=(b*b)-(4*a*c)
    if d>0:
        r1=(-b+math.sqrt(d))/(2*a)
        r2=(-b-math.sqrt(d))/(2*a)
        print("Roots are real and distinct", r1 ,"and" , r2)
    elif d==0:
        r1=-b/(2*a)
        print("Roots are real and same", r1 ,"and" , r1)
        return d
    else:
        print("no real roots are present")
    return d
   
x=float(input("enter the value of a"))
y=float(input("enter the value of b"))
z=float(input("enter the value of c"))
quadratic(x,y,z)        
