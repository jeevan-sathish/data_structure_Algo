# import json
# person = {
#     "name": "John Doe",
#     "age": 30,
#     "city": "New York"

# }
# json_data =json.dumps(person)
# print(json_data)


num = [20, 30, 32, 40, 50, 90]

largest = float('-inf')
secondlargest = float('-inf')

for i in num:
    if i > largest:
        secondlargest = largest
        largest = i
    elif i > secondlargest and i < largest:
        secondlargest = i

if secondlargest == float('-inf'):
    print(-1)
else:
    print(secondlargest)



