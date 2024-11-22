from itertools import count


def flip(pile,index): #flips the pile using a temporary value to help switch the numbers
    temp_value = 0
    if index%2==0:
        for i in range (index//2):
            temp_value=pile[i]
            pile[i]=pile[index-i]
            pile[index-i]=temp_value
    else:
        for i in range ((index+1)//2):
            temp_value=pile[i]
            pile[i]=pile[index-i]
            pile[index-i]=temp_value
    return pile


def find_largest_pancake(pile,index): # finds the largest pancake
    check_for_greater = 0
    store_index = 0
    if index == len(pile)-1: #I check a private case for when the index is equal to the length of the pile
        check_for_greater = pile[index]
        store_index = index
    for i in range(index): #check all the items in the pile to find the largest and store it and its index to return
        if pile[i]>check_for_greater:
            check_for_greater = pile[i]
            store_index = i
    return store_index

def pancake_sort (pile):
    counter=len(pile)
    while counter>2:
        counter-=1
        flip(pile,find_largest_pancake(pile,counter))
        flip (pile,counter)
    return pile



pile1 = [3,1,6,12,4,9]  # Change me!
pile2 = [5,2,11,15,8,10]  # Change me!
pile3 = flip(pile1,2)
print(pile3)
print(flip(pile2,3))
print(find_largest_pancake(pile3,4))
print(find_largest_pancake(pile2,1))
print(pancake_sort(pile1))
print(pancake_sort(pile2))
'''
def pancake_sort(pile): #a function to sort the pancakes like a pyramid
    for i in range (len(pile)):
        flip(pile,find_largest_pancake(pile,len(pile)-i))
        flip(pile,len(pile))
        print(pile)
    return pile
'''