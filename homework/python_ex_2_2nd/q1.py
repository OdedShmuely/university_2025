"""
the function will take the index its given and will flip the pile of pancakes upside down
"""
def flip(pile, index):
    if index < 0 or index > len(pile)-1:
        print ('invalid index, wont change the pile')
        return pile
    flip_range = index // 2 if index % 2 == 0 else (index + 1) // 2
    for i in range(flip_range):
        temp_value = pile[i]
        pile[i] = pile[index - i]
        pile[index - i] = temp_value
    return pile


"""
the function will find the largest pancake and returns its index in the pile
"""
def find_largest_pancake(pile, index):  # finds the largest pancake
    to_index = index
    max_size = 0
    max_size_idx = 0
    for i in range(to_index+1):
        if pile[i] > max_size:
            max_size = pile[i]
            max_size_idx = i
    return max_size_idx

"""
the function will sort the pile and make if look like a pyramid from the largest pancake at the bottom to the smallest on top
"""
def pancake_sort(pile):
    for i in range(len(pile)-1,-1,-1):
        flip(pile,find_largest_pancake(pile,i))
        if i==0:
            return pile
        flip(pile,i)
    return pile

