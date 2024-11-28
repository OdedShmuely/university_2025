from q1 import *

'''
the function will take the pile and will remove the pancakes in the indexes given 
and put them im another list
the function returns the pile of pancakes that were thrown aside
'''
def take_pancakes(pile,index_list):
    pile_to_return =[]
    lst_idx_to_remove = index_list
    pancake_sort(lst_idx_to_remove)
    flip(lst_idx_to_remove,len(lst_idx_to_remove)-1)
    for i in range (len(pile)-1,-1,-1):
        if len(lst_idx_to_remove)== 0:
            break
        if i == lst_idx_to_remove[0]:
            pile_to_return.append(pile[i])
            pile.pop(i)
            lst_idx_to_remove.pop(0)
        continue
    flip(pile_to_return,len(pile_to_return)-1)
    return pile_to_return

'''
the function will insert pancakes to the pile in the right order to keep it perfect
the function return none
'''
def insert_pancakes(pile,pancakes):
    for i in range (len(pancakes)):
        if len(pile) == 0:
            pile.append(pancakes[i])
        for j in range (len(pile)):
            if pancakes[i] < pile [j]:
                pile.insert(j,pancakes[i])
                break
            if pancakes[i] > pile [j] and j == len(pile)-1:
                pile.append(pancakes[i])
                break

'''
the function will return a canonic list built from pairs that sums up to the 
total size value given to the function 
'''
def divide_pancakes(pile, total_size):
    if total_size == 1:
        return 'Cant divide one pancake'
    lst_pairs = []
    pile_copy = pile[::]
    while len(pile_copy) > 0:
        for i in range (1, len(pile_copy)):
            if total_size - pile_copy[0] == pile_copy[i]:
                lst_pairs.append([pile_copy[i], pile_copy[0]])
                pile_copy.pop(i)
                break
        pile_copy.pop(0)
    if len(lst_pairs) == 0:
        return 'could not divide pancakes'
    return lst_pairs


