model = {
    "bmw": ["bmw1", "bmw2", "bmw3"],
    "odi": ["odi1", "odi2", "odi3", "odi4"],
    "swift": ["swift1", "swift2", "swift3"],
    "audi": ["audi1", "audi2", "audi3"],
    "honda": ["honda1", "honda2", "honda3"],
}

# result =[{"key":keys,"val":val} for keys in model for val in model[keys]]
# print(result)

# for k in model:
#     for i in model[k]:
#         print(k,i)

# inp = "bmw"
# cache = {}

# if inp in cache:
#     print("Cache hit:", cache[inp])

# else:
#     if inp in model:
#         cache[inp] = model[inp]
#         print("Fetched from model:", cache[inp])
#     else:
#         print("Model not found")

# print("Cache:", cache)