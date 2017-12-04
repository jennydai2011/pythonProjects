answer = 45

for x in range(0,100):
    if x % 2 == 0 :
        print(x)
        if x == answer:
            print('found it')
            break
