# ************************ HOMEWORK 1 QUESTION 2 **************************
from python_ex_1.question_1 import question_1


def question_2(tier, yearly_purchases, payment):
    discount = 1
    if tier=='Gold':
        discount = 0.80
        if yearly_purchases>5:
            discount = 0.75
            if yearly_purchases>=10 and payment>1000:
                discount = 0.70
    elif tier == 'Silver':
        discount = 0.85
        if yearly_purchases >=15 and payment>800:
            discount = 0.80
    elif tier == 'Bronze':
        discount = 0.90
        if yearly_purchases >= 5 and payment > 1200:
            discount = 0.85
    elif payment>1200:
        discount = 0.95
    payment *= discount
    payment = int(payment)
    print(payment)



'''# ************************ HOMEWORK 1 QUESTION 2 **************************
def question_2_2nd(tier, yearly_purchases, payment):
    discount = 1
    if tier=='Gold':
        discount = 0.80
        if yearly_purchases<=5:
            return
        discount = 0.75
        if yearly_purchases<10 or payment<=1000:
            return 
        discount = 0.70
    elif tier == 'Silver':
        discount = 0.85
        if yearly_purchases >=15 and payment>800:
            discount = 0.80
    elif tier == 'Bronze':
        discount = 0.90
        if yearly_purchases >= 5 and payment > 1200:
            discount = 0.85
    elif payment>1200:
        discount = 0.95


def question_2(tier, yearly_purchases, payment):
    discount = 1
    question_2_2nd(tier, yearly_purchases, payment)
    payment *= discount
    payment = int(payment)
    print(payment)
'''