# ************************ HOMEWORK 1 QUESTION 3 **************************
def question_3(input_num):
    n = input_num
    if n % 2 == 0:
        print('not a diamond')
    else:
        counter = 1
        for i in range ((n//2)+1):
            space = n//2 * ' '
            asterisk = counter * '*'
            print (f'"{space}{asterisk}"')
            counter+=2
            n-=2
        n += 4
        counter -=4
        for i in range ((input_num//2)):
            space = n//2 * ' '
            asterisk = counter * '*'
            n+=2
            counter-=2
            print(f'"{space}{asterisk}"')
