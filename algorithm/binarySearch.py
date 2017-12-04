

def binarySearch(min_number, max_number, answer):
    found = False
    while min_number <= max_number and not found:
        avg = (min_number + max_number) // 2
        print(avg)
        if answer == avg:
            print('found answer')
            found = True
            break
        if answer > avg:
            min_number = avg + 1
        else:
            max_number = avg - 1


binarySearch(0,100, 45)
