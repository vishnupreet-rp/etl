# etl
This etl code connects with source database (mysql), pulls data and pushes into desination datawarehouse (mysql)

5 py files - main.py, db_credentials.py, sql_queries.py, variables.py, etl.py

* variables.py - contains datawarehouse name
* db_credentials.py - contains credentials for both source and destination databases
* sql_queries.py - contains extract and insert sql queries
* main.py - starts destination db connection, calls etl_process method and inserts error message into log table if any error occurs in etl_process method
* etl.py - initiates source connection, executes extract query on source db and inserts into target db and inserts data into log table
