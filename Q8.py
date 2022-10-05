l1=[eval(e) for e in input("enter the keys seprate by comma").split(",")]
l2=[ eval(d) for d in input("enter the data seprate by comma").split(",")]
m={}
for e in l1:
    for d in l2:
        m[e]=d
print(m)
