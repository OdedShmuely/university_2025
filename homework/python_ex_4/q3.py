from q1s2 import duplicate_list
'''
a function to compare 2 int or none values and return the bigger or the non None
'''
def take_max_points(words,a,b):
    points_a = words.get(a)
    points_b = words.get(b)
    if points_a is None and points_b is None:
        return ''
    if points_b is None:
        return a
    if points_a is None:
        return b
    if points_a>points_b:
        return a
    return b

'''
this function receives words dict, the cards, index and the word composed and returns the composed word
with the highest value of points
'''
def create_words_rec(words,cards,idx,word_chosen):
    #stop:
    if idx == len(cards):
        return word_chosen

    #actions:
    cards_copy = []
    duplicate_list(cards,cards_copy,len(cards)-1)
    combined_letters_take = f'{word_chosen}{cards[idx]}'
    cards_copy.pop(idx)

    #recursive call
    word_with_taken_letter = create_words_rec(words,cards_copy,0,combined_letters_take)
    word_with_no_taken_letter = create_words_rec(words,cards,idx+1,word_chosen)

    #return:
    word_to_return = take_max_points(words,word_with_taken_letter,word_with_no_taken_letter)
    return word_to_return

'''this is a wrapped function that receives the words dict and the cards and returns the word that
will get the most points according to the dictionary words'''
def create_words(words, cards):
    winning_word = create_words_rec(words, cards, 0, '')
    return winning_word