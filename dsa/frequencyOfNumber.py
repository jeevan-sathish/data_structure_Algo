def frequency(array):
    freq ={}
    for i in array:
        if i in freq:
            freq[i]=freq[i]+1
        else:
            freq[i]=1

    return freq




print(frequency([5,5,1,2,1,1,3,2,3,4,2,2,2,4,4,4,4,5]))