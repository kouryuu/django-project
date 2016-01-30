# -*- coding: utf-8 -*-
class Item:
    """ This object encapsulates an Item with a valuation made by a person.
    """
    def __init__(self,valuation,person,item_id):
        self.valuation = valuation
        self.person = person
        self.item_id = item_id

    def getValuation(self):
        return self.valuation
    def getPerson(self):
        return self.person
    def getItemID(self):
        return self.item_id
    def setValuation(self,valuation):
        self.valuation = valuation
    def setPerson(self,person):
        self.person = person
    """ Override default methods """
    def __eq__(self,other):
        return self.item_id == other.item_id or self.person == other.person # We want to discard items with the same person or the same id
    def __lt__(self,other):
        return self.valuation < other.valuation
    def __gt__(self,other):
        return self.valuation > other.valuation
    def __str__(self):
        return "< item"+ str(self.item_id) +"> P"+ str(self.person) +" = "+ str(self.valuation)

def defineMatrix(rows):
    """ Defines the square matrix where each person valuates an item
    """
    matrix =[]
    columns = rows #because its a square matrix
    for i in range(0,rows):
        for j in range(0,columns):
            item = Item(0,i,j) # The inital valuation will be defaulted to 0
            matrix.append(item)
    return matrix


def valuate(matrix,values):
    i = 0
    for item in matrix:
        item.setValuation(value[i])
        i += 1


def selectItems(matrix, n_items):
    """ Sorts by valuation (Ascending)
    Selects the last item and then it check if the item is already in selected_items list
    if it is not then it adds it to selected_items the algorithm terminates when all the items are selected.
    """
    selected_items = []
    sorted_matrix = sorted(matrix)
    while n_items > 0:
        already_placed = False
        maximum = sorted_matrix.pop()
        print "Maximo es" + str(maximum)
        for item in selected_items:
            if item == maximum:
                already_placed = True
        if not(already_placed):
            print "Insertando en maximos"
            selected_items.append(maximum)
            n_items = n_items - 1
    return selected_items
