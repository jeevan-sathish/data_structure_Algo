num =[2,3,4,5,7,9]
oddsum=0
evensum=0
for i  in range(len(num)):
    if not i%2==0:
        oddsum +=num[i]
    else:
        evensum +=num[i]


print(oddsum,evensum)
if(oddsum == evensum):
    print("true")
print("false")