#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    score = 0
    weight = 0
    for tupple in my_list:
        weight += tupple[0] * tupple[1]
        score += tupple[1]
        weighted_average = weight / score
    return weighted_average
