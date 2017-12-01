#opt#1- define a list, set list and return list
#con: hold all items of list in memory
# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return result

#opt#2 - use generator
#pro- hold one item in list at a time, performance better
# def square_numbers(nums):
#     for i in nums:
#         yield i*i
#
# my_nums = square_numbers([1,3,5,7,9])

#opt#3- short way of loop through list
#my_nums = [x*x for x in [1,3,5,7,9]]

#opt#4 - short way of loop through generator
my_nums=(x*x for x in [1,3,5,7,9])
#will print generator object
print(my_nums)

#will print the result of generator
#print(next(my_nums))

#convert the generator to list
#after converted to list, it will lose the benefit of performance
print(list(my_nums))

#print each result of generator
for x in my_nums:
    print(x)