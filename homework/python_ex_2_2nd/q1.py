def flip(pile, index):  # flips the pile using a temporary value to help switch the numbers
    flip_range = index // 2 if index % 2 == 0 else (index + 1) // 2
    for i in range(flip_range):
        temp_value = pile[i]
        pile[i] = pile[index - i]
        pile[index - i] = temp_value
    return pile


def find_largest_pancake(pile, index):  # finds the largest pancake
    to_index = index
    max_size = 0
    max_size_idx = 0
    for i in range(to_index+1):
        if pile[i] > max_size:
            max_size = pile[i]
            max_size_idx = i
    return max_size_idx


def pancake_sort(pile):
    for i in range(len(pile)-1,-1,-1):
        flip(pile,find_largest_pancake(pile,i))
        if i==0:
            return pile
        flip(pile,i)
    return pile

pile1 = [3,1,6,12,17,2,4,9,22]  # Change me!
pile2 = [5, 2, 11, 15, 8, 1, 13, 20, 10]  # Change me!
pile3 = flip(pile1, 2)
print(pile3)
print(flip(pile2, 3))
print(find_largest_pancake(pile3, 8))
print(find_largest_pancake(pile2, 8))
print(pancake_sort(pile1))
print(pancake_sort(pile2))
'''
def pancake_sort(pile): #a function to sort the pancakes like a pyramid
    for i in range (len(pile)):
        flip(pile,find_largest_pancake(pile,len(pile)-i))
        flip(pile,len(pile))
        print(pile)
    return pile
    idx = len(pile)
    while idx > 2:
        flip(pile, find_largest_pancake(pile, idx))
        flip(pile, idx)
    return pile

'''
