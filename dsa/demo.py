# import json
# person = {
#     "name": "John Doe",
#     "age": 30,
#     "city": "New York"

# }
# json_data =json.dumps(person)
# print(json_data)


# num = [20, 30, 32, 40, 50, 90]

# largest = float('-inf')
# secondlargest = float('-inf')

# for i in num:
#     if i > largest:
#         secondlargest = largest
#         largest = i
#     elif i > secondlargest and i < largest:
#         secondlargest = i

# if secondlargest == float('-inf'):
#     print(-1)
# else:
#     print(secondlargest)




# import asyncio
# import time


# async def get_user_profile():
#     print("Fetching user profile...")
#     await asyncio.sleep(2)
#     print("User profile received")
#     return {"name": "Jeevan"}


# async def get_transactions():
#     print("Fetching transactions...")
#     await asyncio.sleep(3)
#     print("Transactions received")
#     return ["Deposit", "Withdrawal"]


# async def get_notifications():
#     print("Fetching notifications...")
#     await asyncio.sleep(1)
#     print("Notifications received")
#     return ["Welcome back"]


# async def dashboard():
#     start = time.perf_counter()

#     profile, transactions, notifications = await asyncio.gather(
#         get_user_profile(),
#         get_transactions(),
#         get_notifications()
#     )

#     result = {
#         "profile": profile,
#         "transactions": transactions,
#         "notifications": notifications
#     }

#     print(result)
#     print(f"Total time: {time.perf_counter() - start:.2f} seconds")


# asyncio.run(dashboard())

# import asyncio

# async def fun1():
#     print("running fun1")
#     await asyncio.sleep(2)
#     print("fun1 completed")
#     return ["fun1","completed"]

# async def fun2():
#     print("running fun2")
#     await asyncio.sleep(3)
#     print("fun2 completed")
#     return ["fun2","completed"]

# async def fun3():
#     print("running fun3")
#     await asyncio.sleep(5)
#     print("fun3 completed")
#     return ["fun3","completed"]

# async def main():
#     result = await asyncio.gather(
#         fun1(),
#         fun2(),
#         fun3()    )

#     print(result)

# asyncio.run(main())

# i=0
# j=0

# while



def demo(**kargs):
  for key,value in kargs.items():
    print(f"{key}:{value}")
  

print(demo(name="jeevabn" ,age=20))
    



