# create a function called get_average() and calculate the average of the numbers below and return the average
# values = [61, 20, 45, 63, 96, 71, 6, 8, 72, 22, 97, 7, 46, 11, 15, 74, 81, 69, 70, 26]

def get_average():
    values = [61, 20, 45, 63, 96, 71, 6, 8, 72, 22, 97, 7, 46, 11, 15, 74, 81, 69, 70, 26]
    averege = sum(values)/ len(values)
    print('The averege is', averege)
    return averege

get_average()