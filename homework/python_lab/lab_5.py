def even_sum (num_lst):
    if len(num_lst) == 0:
        return 0
    returned_num =  even_sum(num_lst[1:])
    if num_lst[0] %2 == 0:
        return returned_num + num_lst[0]
    return returned_num
print(even_sum([1,2,3,4,5,6,7,8]))


def max_finder (lst):
    return max_finder_wrapper(lst, 0)

def max_finder_wrapper(lst, first_idx):
    if len(lst)== 0:
        return first_idx
    biggest_num_idx = max_finder_wrapper(lst[:-1], first_idx)
    if lst[biggest_num_idx] > lst[len(lst)-1]:
        return biggest_num_idx
    return len(lst)-1
print(max_finder([]))



