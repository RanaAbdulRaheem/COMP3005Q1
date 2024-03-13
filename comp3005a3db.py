import psycopg2 as pg

#this funtion gte connected to the postgres in pgadmin and created the database
def connect():
    # establishing a connection to the database server
    db = pg.connect(
    database="postgres", 
    user='postgres', 
    password='postgres', 
    host='localhost', 
    port= 5432
    )
    # changing autocommit to be true to create the db
    db.autocommit = True
    #creating the cursor
    db_cur = db.cursor()
    #creating the database
    database = '''CREATE DATABASE comp3005a3'''
    #executing the database to create it
    db_cur.execute(database)

#calling the connect function to create the database
connect()

#connect to the created database
try:
    db = pg.connect(
    dbname="comp3005a3",
    user="postgres",
    password="postgres",
    host="localhost",
    port= 5432
    )
    
    db_cur = db.cursor()
    print("Connection has been established.")

except Exception as err:

    print("There is an error connecting to the database: ",err)

#creating the required studet table
table = '''
    CREATE TABLE students (
        student_id SERIAL PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        enrollment_date DATE
    )
'''
#insering that student table into the database
db_cur.execute(table)

# creating the initial data that is needed to be added
info_insert = '''
    INSERT INTO students (first_name, last_name, email, enrollment_date) 
    VALUES ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
'''
#insering that data into the student table 
db_cur.execute(info_insert)

#commiting all o fit to the database
db.commit()


#close the cursor and the connection
db_cur.close()
db.close()