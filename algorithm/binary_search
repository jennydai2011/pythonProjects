#binary search



#1 - linear search

def linear_search(arr, target):
    count = 0
    for i in range(len(arr)):
        count = count + 1
        if arr[i] == target:
            print("found target at index:" + str(i))
            print(" counting the times of linear_search:" + str(count))
            break


#2 - iterative binary search
def iterative_binary_search(arr, target):
    low = 0
    high = len(arr) -1
    count = 0
    while low <= high:
        count = count + 1
        mid = (low + high) // 2
        if target == arr[mid]:
            print("found target at index:" + str(mid))
            print(" counting the times of iterative_binary_search:" + str(count))
            break
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1


#3 - recursive_binary_search
def recursive_binary_search(arr, target, low, high, count):
    count = count + 1

    if low > high:
        return

    mid = (low + high) // 2
    if target == arr[mid]:
        print("found target at index:" + str(mid))
        print(" counting the times of recursive_binary_search:" + str(count))
        return
    elif target < arr[mid]:
        high = mid - 1
        recursive_binary_search(arr, target, low, high, count)
    else:
        low = mid + 1
        recursive_binary_search(arr, target, low, high, count)


#run
arr = [2, 4, 5, 6, 8, 9, 22, 189]
target = 189

#run - #1 - linear search
linear_search(arr, target)

#run - #2 - iterative_binary_search
iterative_binary_search(arr, target)

#run - #3 - iterative_binary_search
recursive_binary_search(arr, target, 0, len(arr), 0)