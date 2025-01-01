from q1s2 import duplicate_list

'''
this function check the greater value between 2 values'''
def check_max (a,b):
    if a>b: return a
    else: return b


'''
this function return the max number of options possible to divide the pancakes between people in the division of total size
###sum_of_taken_p stands for sum of 2 pancakes
###delete_items is a list that collect the index of the numbers we want to throw because we used them
'''
def divide_pancakes_ex_rec(pancakes, total_size, idx, sum_of_taken_p, sum_of_leaf, delete_items):
    #stop
    if len(pancakes) == 0:
        return sum_of_leaf
    if sum_of_taken_p > total_size:
        sum_of_taken_p-=pancakes[idx - 1]
        delete_items.pop()
        return sum_of_leaf
    if idx == len(pancakes):
        return sum_of_leaf

    #before recursive call
    pancakes_copy = []
    duplicate_list(pancakes,pancakes_copy, len(pancakes)-1)
    if sum_of_taken_p == total_size:
        for i in range(len(delete_items)-1,-1,-1):
            pancakes_copy.pop(delete_items[i])
        sum_of_leaf += 1
        idx = 0
        sum_of_taken_p = 0
        delete_items = []
    delete_items.append(idx)

    #recursive call
    take = divide_pancakes_ex_rec(pancakes_copy, total_size, idx + 1, sum_of_taken_p + pancakes_copy[idx], sum_of_leaf, delete_items)
    no_take = divide_pancakes_ex_rec(pancakes, total_size, idx + 1, sum_of_taken_p, sum_of_leaf, delete_items)

    if idx-1 == delete_items[-1] and len(delete_items) > 1:
        delete_items.pop()
    return check_max(take,no_take)

def divide_pancakes_extended(pancakes, total_size):
    to_ret = divide_pancakes_ex_rec(pancakes,total_size, 0, 0,0, [])
    return to_ret

print(divide_pancakes_extended([1, 1, 4, 2, 3, 3, 2, 5], 6))