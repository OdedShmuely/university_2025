from q1s2 import duplicate_list
'''
a function to compare 2 int or none values and return the bigger or the non None
'''
def take_max_points(a,b):
    if b is None: return a
    if a is None: return b
    if a > b:
        return a
    return b


def create_words_rec(words,cards,idx,word_chosen):
    #stop:
    if idx == len(cards):
        print (word_chosen)
        return words.get(word_chosen)

    #actions:
    cards_copy = []
    duplicate_list(cards,cards_copy,len(cards)-1)
    combined_letters_take = f'{word_chosen}{cards[idx]}'
    cards_copy.pop(idx)

    #recursive call
    word_with_taken_letter = create_words_rec(words,cards_copy,0,combined_letters_take)
    word_with_no_taken_letter = create_words_rec(words,cards,idx+1,word_chosen)

    #return:
    # points_from_take = words.get(word_with_taken_letter)
    # points_from_no_take = words.get(word_with_no_taken_letter)
    word_to_return = take_max_points(word_with_taken_letter,word_with_no_taken_letter)
    # print(points_from_take,points_from_no_take)
    return word_to_return

def create_words(words, cards):
    points = create_words_rec(words, cards, 0, '')
    if points is None:
        points = ''
    print(points)

# create_words({'ab':5, 'ca':2, 'abc':7, 'c':10}, ['a','b','c'])