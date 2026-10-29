
def remove_duplicates(array):
    duplicate =[]
    for i in array:
        if i not in duplicate:
            duplicate.append(i)

    return duplicate
       
print(remove_duplicates([1,1,2,3,4,5,2,3,6]))