# ************************ HOMEWORK 1 QUESTION 1 **************************
def question_1(x, a):
    denuminator = x**(a%3)+3
    numerator = ((a**2)*x)+(2*x)-7
    y_answer = round(numerator/denuminator,2)
    print(y_answer)

question_1(3,3)


