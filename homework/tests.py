import question_1
import question_2
import question_3
import wrong_4
from homework import question_4


def test_question_1():
    x = 1  # Change me!
    a = 3  # Change me!
    question_1.question_1(x, a)


def test_question_2():
    tier = 'Gold'           # Change me!
    yearly_purchases = 6    # Change me!
    payment = 1000.0        # Change me!

    question_2.question_2(tier, yearly_purchases, payment)


def test_question_3():
    input_num = 5  # Change me!
    question_3.question_3(input_num)


def test_question_4():
    board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]] # Change me!
    question_4.question_4(board)


if __name__ == '__main__':
    test_question_1()
    test_question_2()
    test_question_3()
    test_question_4()
