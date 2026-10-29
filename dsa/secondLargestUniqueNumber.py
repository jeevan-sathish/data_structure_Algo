
def remove_duplicates(array):
    duplicate =[]
    
    for i in array:
        if i not in duplicate:
            duplicate.append(i)

    if (len(duplicate)>2):
        largest =duplicate[0]
        smallest =float("-inf")
        for i in duplicate:
                
                if(i > largest):
                    smallest =largest
                    largest = i
                elif i <largest and i >smallest:
                    smallest=1

    

    
    return smallest

    
       
print(remove_duplicates([1,1,2,3,4,5,2,3,6]))