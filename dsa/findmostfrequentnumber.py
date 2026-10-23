arr=[1,2,1,4,3,4,2,2,5,5,5,5,]
result ={}
for i , num in enumerate(arr):
  if num in result:
    result[num]=result.get(num,0)+1
  else:
    result[num]=1

highest = result[1]
for h in result:
  if result[h] > highest:
    highest =result[h]

print(highest)

highest =max(result,key=result.get)
print(highest)

print(result)
    