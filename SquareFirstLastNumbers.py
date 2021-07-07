n=input("enter :")
m=str(n)
x,y=int(m[0]),int(m[-1])
a,b=x*x,y*y
c=(a,m[1:-1],b)
print(str(c).replace(",","").replace("(","").replace(")","").replace(" ","").replace("'",""))
