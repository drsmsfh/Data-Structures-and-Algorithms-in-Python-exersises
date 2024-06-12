"""
QUESTION 1: Alice has some cards with numbers written on them.
She arranges the cards in decreasing order, 
and lays them out face down in a sequence on a table. 
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
Write a function to help Bob locate the card.
"""
cards = []
wanted_number = 0


def checker(x,y):
    output = []
    for index, item in enumerate(x):
        if item != y:
            continue
        elif item == y :
            output.append(index)
    if len(output) == 0:
        output = [-1]
            
    return output
            

print(checker(cards,wanted_number))
