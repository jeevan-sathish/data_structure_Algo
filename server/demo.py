import redis 
import json
r =redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


r.hset(
    "user1",
    mapping={
        "name":"jeevan",
        "email":"jeevan@gmail.com"
    }
)

data = r.hgetall("user1")
for key,val in data.items():
    print(key,val)
