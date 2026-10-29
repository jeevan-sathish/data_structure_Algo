

def interval_merge(interval):
    print(interval)
    sorted_interval = sorted(interval ,key=lambda x:x[0])
    print(sorted_interval)
    if not interval:
        return []
    
    merged =[interval[0]]
    print(merged)

    for ele in interval[1:]:
        current = ele[0]
        last = merged[-1][1]
        print(current ,last)

        if(last < current ):
            merged.append(ele)
        else:
            merged[-1][1]=max(last,ele[1])

    return merged


print(interval_merge([[1,4],[3,4],[5,7],[6,10],[12,20]]))