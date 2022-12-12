import pymongo

conn_str = "Your Connection String"
client = pymongo.MongoClient(conn_str)

db = client["Organisation"]
employeeCollection = db["employees"]


def add_employee(data):
    data = dict(data)
    response = employeeCollection.insert_one(data)
    return str(response.inserted_id)

def all( ):
    response = employeeCollection.find({})
    data = [ ]
    for emp in response:
        emp["_id"] = str(emp["_id"])
        data.append(emp)
    return data

def get_one(email):
    response = employeeCollection.find_one({'email':email})
    response["_id"] = str(response["_id"])
    return response

def update(data):
    data = dict(data)
    response = employeeCollection.update_one({"email": data["email"]}, 
    {"$set": data})
    return response.modified_count

def delete(email):
    response = employeeCollection.delete_one({"email":email})
    return response.deleted_count
