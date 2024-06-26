This is a simplified version that uses PostgreSQL, the user can search for universities depending on what he wants. 


I used 4521 as the password of the database. 
Create the database called college_finder on pgAdmin locally. 
Create a Virtual Environment to run it. 
Install the required packages
* pip install -r requirements.txt
* pip install psycopg2-binary (required to fix error in PostgreSQL)
populate the database using:
* python -m my_project.populate_db
run the project inside the environment: 
* python -m my_project.run
