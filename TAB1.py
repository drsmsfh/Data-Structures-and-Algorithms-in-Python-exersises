"""
QUESTION 1: Alice has some cards with numbers written on them.
She arranges the cards in decreasing order, 
and lays them out face down in a sequence on a table. 
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
Write a function to help Bob locate the card.
"""
cards = [14,13,9,7,4,2,1]
wanted_number = 7
def checker(x,y):
    num_of_car_flepped = 0
    for i in x:
        if i != y:
            num_of_car_flepped += 1
        else :
            num_of_car_flepped += 1
            print (f'you flept {num_of_car_flepped} cards ')
            break

checker(cards,wanted_number)
