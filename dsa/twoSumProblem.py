def twoSum(numbers,target):
    first =0
    last =len(numbers)-1
    while(first <last):
        sum =numbers[first]+ numbers[last]
        if(sum == target):
            return [numbers[first],numbers[last]]
            
        elif(sum>target):
            last =last-1
        else:
            first+=1
            
  
    return []

print(twoSum([1,2,3,4,5,6,7],13))