x = -1.5
y = 1.1
r = 1

if ((x+r)**2 + (y-r)**2<=r**2 and y>=r and y<-x) or \
    ((x+r)**2 + (y-r)**2>=r**2 and x<0 and y>=-x):
    print("yes")

else:
    print("no")
