from fastapi import FastAPI
import db
from userModal import *



app = FastAPI()

@app.get("/")
async def hello():
    return {"msg": "Hello World"}


@app.post("/create")
async def create(data: Employees):
    id = db.add_employee(data)
    return {"Inserted": True, "Id": id}

@app.get("/all")
async def get_all():
    data = db.all()
    return {"data": data}

@app.post("/one")
def get_one(emp: Emp):
    res = db.get_one(emp.email)
    return {"Result": res}

@app.delete("/delete")
def delete(emp: Emp):
    res = db.delete(emp.email)
    return {"Delete Status": res}

@app.put("/update")
def update(data: Employees):
    res = db.update(data)
    return {"Update_Status": True,"Update_Count": res}
