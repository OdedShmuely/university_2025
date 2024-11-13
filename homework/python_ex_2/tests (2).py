import q1
import q2


def test_q1():
    pile1 = [3,1,6,12,4,9]  # Change me!
    pile2 = [5,2,11,15,8,10]  # Change me!

    #test flip
    pile3 = q1.flip(pile1,2)
    print(pile3)
    print(q1.flip(pile2,3))

    #test find_largest_pancake
    print(q1.find_largest_pancake(pile3,4))
    print(q1.find_largest_pancake(pile2,1))

    #test pancake_sort
    print(q1.pancake_sort(pile1))
    print(q1.pancake_sort(pile2))
    
    
def test_q2():
    pile1 = [3,1,12,4,9]  # Change me!
    pile2 = [5,2,11,15,8,10]  # Change me!
    pile3 = [2,3,4,7,12]  # Change me!

    pile4 = [2,3,4,4,5,5,6,7,8,9,12]

    #test take_pancakes
    print(q2.take_pancakes(pile1,[0,2,3]))
    print(pile1)

    print(q2.take_pancakes(pile2,[1,4]))
    print(pile2)

    #test insert_pancakes
    q2.insert_pancakes(pile3,[6,9])
    print(pile3)

    #test divide_pancakes
    print(q2.divide_pancales(pile4,10))
    print(q2.divide_pancales(pile4,12))
    

    


if __name__ == '__main__':
    test_q1()
    test_q2()
    