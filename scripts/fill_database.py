from pymongo import MongoClient

conn = MongoClient()
db = conn.ClassGraphs
coll = db.CsClasses

coll.insert_one({
                 "designation": "CS141",
                 "dependents": "CS211, CS251, CS261",
                 "credit_hours": 3
                })

coll.insert_one({
                 "designation": "CS151",
                 "dependents": "CS251",
                 "credit_hours": 3
                })

coll.insert_one({
                 "designation": "CS211",
                 "dependents": "",
                 "credit_hours": 3
                })

coll.insert_one({
                 "designation": "CS251",
                 "dependents": "",
                 "credit_hours": 3
                })

coll.insert_one({
                 "designation": "CS261",
                 "dependents": "",
                 "credit_hours": 3
                })
