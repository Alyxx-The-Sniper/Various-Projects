#
#
#
def large_power(base, exponent):
  if base ** exponent > 5000:
    return True
  else:
    return False

# x = large_power(800,3)
# print(x)

##############################################
def over_budget(budget, food_bill, electric_bill, internet_bill, rent):
    all_expense = food_bill + electric_bill + internet_bill + rent
    if all_expense > budget:
        return True
    else:
        return False

january = over_budget(10000,2000,3000,2000,3000)
# print(january)

##############################################
def twice_as_large(num1, num2):
    twice = num1 * 2
    if twice >= num2:
        return True
    else:
        return False

sample1 = twice_as_large(100,150)
# print(sample1)

##############################################
def divisible_by_ten(num):
    result = num % 10
    if result == 0:
        return True
    else:
        return False

number1 = divisible_by_ten(100)
number2 = divisible_by_ten(99)

# print(number1)
# print(number2)

##############################################
def not_sum_to_ten(num1, num2):
    if num1 + num2 != 10:
        return  True
    else:
        return False
##############################################
def int_range(num,lower,upper): #search for a number in a numbers bracket
    if num >= lower and num <= upper:
        return True
    else:
        return False

# print(int_range(1,10,20))
##############################################
def movie_review(rating):
    if rating <= 5:
        return 'Avoid at all cost!'
    elif rating <= 9:
        return  'This one was fun'
    else:
        return 'Outstanding'


# print(movie_review(11))
##############################################
def append_size(lst):
    lst.append(len(lst))
    return lst

# print(append_size([23, 42, 108]))
##############################################
def append_sum(lst):
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])

    return lst

# print(append_sum([1, 1, 2]))


##############################################
def larger_list(lst1, lst2): # check for list len of two list
    if len(lst1) >= len(lst2):
        return lst1[-1]
    else:
        return lst2[-1]

# print(larger_list(['aa','bb','cc'], ['zz','yy','dd','p','q','t']))

###############################################
def more_than_n (lst, item, n): # more than  a certain number(n)
    x = list(lst).count(item)
    if x >= n :
        return True
    else:
        return False
# print(more_than_n(['potato', 'cinamon', 'chili', 'chili','garlic'], 'chili', 2))


###############################################
def combine_sort(lst1, lst2):
    new_list = lst1 + lst2
    x = sorted(new_list)
    return x

# print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))


###############################################
#every three number
def every_three_nums(n):
    return list(range(n,101,3))

# print(every_three_nums(0))

###############################################

def remove_middle(lst, start_index, end_index):
    s = lst[0 : start_index]
    e = lst[end_index + 1  :  ]
    x = s + e
    return x

# print(remove_middle([4, 8 , 15, 16, 23, 42], 1, 3))

###############################################

def more_frequent_item(lst,item1,item2):
    a = list(lst).count(item1)
    b = list(lst).count(item2)
    if a >= b:
        return item1
    else:
        return item2

# print(more_frequent_item(['potato', 'potato', 'chili', 'chili','chili'], 'potato', 'chili'))


###############################################

def double_index(lst, index):
        if index >= len(list(lst)):
            return lst
        else:
            new_list = lst[0:index] # slice for preparation to append
            new_list.append(lst[index] * 2) #append edit the last element in a list
            new_list = new_list + lst[ index+1 : ] # concatenate new-list and lst (sliced lst)
            return new_list

# print(double_index([3, 8, -10, 12, ], 1))

###############################################

def middle_element(lst):
    if len(lst) % 2 != 0:
        a = int((len(lst) - 1 ) / 2)  #len in a list = count normally
        return lst[a]                 #index in a list start count at 0
    else:
        if len(lst) % 2 == 0:
            b = int(len(lst)) / 2
            c = lst[int(b)]
            d = lst[int(b-1)]
            output = (c + d) / 2
            return output

print(middle_element([5, 2, -10, 10, 21, 5, 32, 99,]))
# x = [5, 2, -10, 10, 21, 5, 32, 99,55 ]
# print(len(x))

###############################################
def divisible_by_ten(lst):
    counter = 0
    for i in list(lst):
        if i % 10 == 0:
            counter += 1
    return counter
# print(divisible_by_ten([20, 25, 30, 35, 40,40,5,100,90]))

###############################################
def add_greetings(lst_names):
    greetings = []
    for name in lst_names:
        greetings.append('Hello ' + name)
    return greetings

# print(add_greetings(["Owen", "Max", "Sophie", 'toto']))

###############################################







