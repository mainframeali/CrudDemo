Project description : Sample Crud project

Features : Lists, adds, updates and deletes from "listings" MySql table,
    which consists of 3 fields as listing_id, address & price.
    "listing_id" is an autoincrement field

Documents :
			FestApi Swagger http://127.0.0.1:8000/docs (after running project)
		    readme.txt (this file)
		    instructions.txt

Sql : sql/db_scripts.sql

Used Frameworks :
	fastapi : rest framework
	uvicorn : web server
	pymysql : my sql db connector
	SQLAlchemy : ORM tool

Used Libraries :
     pydantic : for data validation
     pytest & starlette.testclient : for test api testing


Project code structure :
    db
        database.py : main connection util for db connection
    endpoint
        crud.py : consists of endpoints for crud operations
        api.py : api routing
    model
        listing.py : base "Listing" class
        request.py : request objects for Listing
        response.py : common result object for all requests

