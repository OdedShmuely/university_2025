'''
this function check the greater value between 2 values
'''
def check_max (a,b):
    if a>b: return a
    else: return b


'''
this function return the max number of options possible to divide the pancakes between people in the division of total size
### sum_of_taken_p stands for sum of all the pancakes i used in this branch
### pancakes_skipped is a list that takes the numbers i didn't take to check them later
### sum of leaf represents the total of people that can get a plate that contain the sum of total pancakes
'''
def divide_pancakes_ex_rec(pancakes, pancakes_skipped, total_size, sum_of_leaf, sum_of_taken_p):
    #stop
    if sum_of_taken_p == total_size:
        sum_of_leaf += 1
        sum_of_taken_p = 0
        pancakes += pancakes_skipped
        pancakes_skipped = []
    if len(pancakes) == 0:
        return sum_of_leaf
    if sum_of_taken_p > total_size:
        return sum_of_leaf
    curr_pancake = pancakes[0]

    #recursive call
    new_sum_of_leaf_take = divide_pancakes_ex_rec(pancakes[1:], pancakes_skipped, total_size, sum_of_leaf, sum_of_taken_p + curr_pancake)
    new_sum_of_leaf_no_take = divide_pancakes_ex_rec(pancakes[1:],pancakes_skipped + [curr_pancake], total_size, sum_of_leaf, sum_of_taken_p)

    new_sum_of_leaf = check_max(new_sum_of_leaf_take,new_sum_of_leaf_no_take)
    return new_sum_of_leaf

def divide_pancakes_extended(pancakes, total_size):
    to_ret = divide_pancakes_ex_rec(pancakes, [],total_size, 0, 0)
    return to_ret