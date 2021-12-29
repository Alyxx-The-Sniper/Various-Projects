#
#
#


def delete_starting_evens(lst): # remove even numbers stop loop condition until odd number
        while (len(lst) > 0 and lst[0] % 2 == 0):
            lst = lst[1:] # while the condition is TRUE lst indices will fallout short
        return lst

# print(delete_starting_evens([4, 8, 10, 11, 12, 15]))

#########################################################################
def odd_indices(lst):
    new_lst = []
    for i in range(1,  len(lst) , 2): #start at 1 to len(lst) skpped 2 indices
        new_lst.append(lst[i])

    return new_lst

# print(odd_indices([4, 3, 7, 10, 11, -2,5,6,7,88,99,44])) #3,10,-2

#########################################################################
def exponents(bases,powers):

    new_lst = []
    for base in bases:
        for power in powers:
            new_lst.append(base ** power)
    return new_lst

# print(exponents([2, 3, 4], [1, 2, 3]))

#########################################################################
def larger_sum(lst1,lst2):
    sum1 = 0
    sum2 = 0

    for i in lst1:
        sum1 = sum1 + i

    for ii in lst2:
        sum2 = sum2 + ii

    if sum1 > sum2:
        return lst1
    else:
        return lst2

# print(larger_sum([1, 9, 5], [2, 3, 7]))
# print(larger_sum([1, 9, 5], [2, 3, 10]))

#########################################################################
def over_nine_thousand(lst): # print value until it reach maximun required
    num = 0

    for i in lst:
        if num < 9000:
            num = num + i
    return num
# print(over_nine_thousand([8000, 900, 120, 5000, 6999]))

#########################################################################
def max_num(nums):
    maximum = nums[0]
    for number in nums:  # this will loop until the end of list and return the highest
        if number > maximum: #value it gathered
            maximum = number
    return maximum
print(max([50, -10, 0, 75, 20, 100, 55, 89, 77, 500, 40, 53]))

#########################################################################


