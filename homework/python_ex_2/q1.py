#from tomlkit import value

def actual_flip (new_pile,index,i): #a function that helps flip the numbers in the list
        temp_value = new_pile[i]
        new_pile[i] = new_pile[index - i]
        new_pile[index - i] = temp_value

def flip(pile,index):
    new_pile = pile
    if index%2 ==0: #check how many times to repeat the loop for even and odd index
        for i in range (index//2):
            actual_flip(new_pile,index,i)
    else:
        for i in range (index//2+1):
            actual_flip(new_pile,index,i)
    return new_pile

def find_largest_pancake(pile,index):
    index_value = 0 # to store the data of the current size of pancake
    index_to_return = 0 #to save the index of the loop
    for i in range (index +1):
        if pile[i] > index_value:
            index_value = pile[i]
            index_to_return = i

    return index_to_return



def pancake_sort(pile):
    organized_pile = pile
    for i in range (len(organized_pile)-1,-1,-1):
        flip(organized_pile,find_largest_pancake(organized_pile,i))
        print(organized_pile)
    return organized_pile



