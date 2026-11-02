import redis 
import json
r =redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

print("redis connected",r.ping())

brand ="bmw"
models =["bwm1","bmw2","bmw3"]
r.set(brand,json.dumps(models))
