Project description : Sample Crud project

Features : Lists, adds, updates and deletes from "listings" MySql table,
    which consists of 3 fields as listing_id (autoincrement), address & price.

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
        crud.py : consists of endpoints for crud operations for listing table, 
		 (if new tables wanted to added, new files for each table is suggested)
        api.py : api routing
    model
        listing.py : base "Listing" class
        request.py : request objects for Listing
        response.py : common result object for all requests
	(PS : for each table to be added, one object and one request class should be added)
	
Sample test output:
python manuel_test.py
{'data': {'price': 124001, 'listing_id': 1, 'address': 'test address 124'}, 'code': 200, 'message': 'Listing retrieved successfully', 'error': False}
{'data': {'listing_id': 21}, 'code': 200, 'message': 'Listing added successfully.', 'error': False}
{'data': {'price': 124001, 'listing_id': 1, 'address': 'test address 124'}, 'code': 200, 'message': 'Listing updated successfully', 'error': False}
{'data': {'listing_id': 7}, 'code': 200, 'message': 'Listing deleted successfully', 'error': False}
