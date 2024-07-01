note: This is a simplified version which uses PostgreSQL, the user can search for universities depending on what he wants. 


Be sure to remember the password in PostgreSQL for the database. 
Simplified version. 
Created the database called college_finder on pgAdmin locally. 
Create a Virtual Environment to run it. 
Installed the required packaged. 
* pip install -r requirements.txt
* pip install psycopg2-binary (required to fix error in PostgreSQL)
populate the database using:
* python -m my_project.populate_db
create the user database

CREATE TABLE "user" (
    uid SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    pass_hash VARCHAR(255) NOT NULL
);

run the project inside the environment: 
* python -m my_project.run
