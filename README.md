# FastAPI-MongoDB
CRUD app with FastAPI and MongoDB

## Setup FastAPI application
  Create a new directory named Fastapi-Mongo and inside that create a new file named main.py
  Install fast API and uvicorn using the command:
  
    $ pip install fastapi
    $ pip install uvicorn
    
  Create a simple route in main.py to check the setup:
  
    from fastapi import FastAPI
    
    app = FastAPI()
    
    @app.get("/")
    async def hello():
      return {"msg": "Hello World"}
  
  Now run the command:
  
    $ uvicorn main:app --reload
    
  Navigate to http://127.0.0.1:8000 in your browser here you should see the output:
	{
    "msg": "Hello World"
  }
  You can also check the interactive API documentation at:http://127.0.0.1:8000/docs


## Setup MongoDB
  Install the MongoDB community edition. Follow https://www.mongodb.com/docs/manual/administration/install-community/  for the installation process.
  To check whether the MongoDB has been installed successfully run the command:
    
    $ mongo --version
    
  Now install MongoDB compass, the free GUI for MongoDB, or set up your account on MongoDB Atlas, which manages MongoDB in the cloud.
  Here we will use MongoDB Atlas set up your account https://www.mongodb.com/cloud/atlas/register and create a cluster.
  
  
## Install PyMongo
  PyMongo is the official MongoDB driver for synchronous python applications.
  Here is the installation process: https://pymongo.readthedocs.io/en/stable/installation.html
  
  
## Connect to MongoDB Atlas
  To connect the MongoDB cluster use the atlas collection string for your cluster.
  Create a file named db.py
  
    import pymongo
    
    conn_str = “Your_Connection_String”
    client = pymongo.MongoClient(conn_str)
    
    
## Start setting up your database
  We will create a database that will store the employee information in an organization.
  Create a database and a collection named Organisation and employees respectively.
  
    import pymongo
    
    conn_str = “Your_Connection_String”
	  client = pymongo.MongoClient(conn_str)

	  db = client["Organisation"]
    employeeCollection = db["employees"]
    
  
## Setup the CRUD database operations
  Add each of the functions in the db.py file.
     
   > Add a new employee to the collection
   
        def add_employee(data):
          data = dict(data)
          response = employeeCollection.insert_one(data)
          return str(response.inserted_id)

   > Retreive all employees present in the collection
   
        def all( ):
          response = employeeCollection.find({})
          data = [ ]
          for emp in response:
            emp["_id"] = str(emp["_id"])
            data.append(emp)
          return data
          
   > Retreive a employee with a matching email Id
   
        def get_one(email):
          response = employeeCollection.find_one({'email':email})
          response["_id"] = str(response["_id"])
          return response

   > Update a employee with matching email Id
   
        def update(data):
          data = dict(data)
          response = employeeCollection.update_one({"email": data["email"]}, 
          {"$set": data})
          return response.modified_count
          
   > Delete a employee with matching email Id
   
        def delete(email):
          response = employeeCollection.delete_one({"email":email})
          return response.deleted_count


## Setup the Modal
  Create a file named modals.py and create the Employee modal.
  
    from pydantic import BaseModel

    class Employees(BaseModel):
	    email: str
	    name: str
	    mobile: str
	    experienceYear: int
      
    class Emp(BaseModel):
	    email: str


## Setup the CRUD Routes
  Add each of the routes in the main.py file
  
    from fastapi import FastAPI
    import db
    from userModal import *

   > add the following handler for creating new employee
   
      @app.post("/create")
      async def create(data: Employees):
        id = db.add_employee(data)
        return {"Inserted": True, "Id": id}
        
   Fire up the uvicorn server and test the route with dummy data and check whether the data is entering into the database or not
   
   > this route will retrieve all the employee's details

      @app.get("/all")
      async def get_all():
        data = db.all()
        return {"data": data}

   > this route will return the employee details with a matching email
   
      @app.post("/one")
      def get_one(emp: Emp):
        res = db.get_one(emp.email)
        return {"Result": res}
   > this route will update the employee with matching email id
   
      @app.put("/update")
      def update(data: Employees):
        res = db.update(data)
        return {"Update_Status": True,"Update_Count": res}
        
   > this route will delete the employee with a matching email

      @app.delete("/delete")
      def delete(emp: Emp):
        res = db.delete(emp.email)
        return {"Delete Status": res}


  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
