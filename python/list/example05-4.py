list_comprehension = [x for x in range(1,11)]
list_comprehensioned = [-x if x >= 3 and x <= 8 else x for x in list_comprehension]
print(list_comprehensioned)