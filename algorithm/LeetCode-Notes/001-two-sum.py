a = [2, 7, 11, 15]
d = {str(i) : a[i] for i in range(len(a))}

print(d)

target = 9

i1="0"
i2="0"

found=False
for k, v in d.items():
    print("k is "+ str(k) + ", v is "+ str(v))
    i1=k
    f = target - d[k]
    for fk2 in d.keys():
        if d[fk2] == f:
            print("found 2nd item:" + str(f) + ", index is "+ fk2)
            i2=fk2
            found=True
            break
    if found:
        break

print("found matching index: "+ str(i1) +" and "+ str(i2))
        


