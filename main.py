from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["mydatabase"]
collection = db["people"]

new_items = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 28},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 40},
    {"name": "Eve", "age": 27},
    {"name": "Frank", "age": 32},
    {"name": "Grace", "age": 29},
    {"name": "Helen", "age": 31},
    {"name": "Ivy", "age": 24},
    {"name": "Jack", "age": 26},
]

collection.insert_many(new_items)
collection.insert_one({"name": "Karl", "age": 25, "languages": ["python", "java", "c"]})

print("-----------------------------------")
print([p for p in collection.find({"age": {"$gt": 30}})])

collection.update_one(
    {"name": "Jack"}, {"$set": {"languages": ["python", "java", "c", "c++"]}}
)
print("-----------------------------------")
print([p for p in collection.find({"name": "Jack"})])

collection.delete_one({"name": "Karl"})

pipeline = [
    {
        "$group": {
            "_id": "$name",
            "count": {"$sum": 1},
        }
    },
    {"$sort": {"count": -1}},
]

print("-----------------------------------")
print([p for p in collection.aggregate(pipeline)])
