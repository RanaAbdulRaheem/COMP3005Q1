import psycopg2 as pg

# conneting to the database
try:
    #establish the connection
    db = pg.connect(
    dbname="comp3005a3",
    user="postgres",
    password="postgres",
    host="localhost",
    port= 5432
    )
    #create the cursor
    db_cur = db.cursor()
    #if the connection is establoshed
    print("Connection has been established.")

# catch error
except Exception as err:
    #catch the exception
    print("There is an error connecting to the database: ",err)

# Retrieves and displays all records from the students table.
def getAllStudents():
    #execute the command to get all students in the database
    db_cur.execute('''SELECT * FROM students''')
    # Get all students in the database and store them in the data
    data = db_cur.fetchall()
    # return the data
    return data

# Inserts a new student record into the students table.
def addStudent(first_name, last_name, email, enrollment_date):

    try:
        # insert the values into the database
        db_cur.execute(
            '''INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)''',
            (first_name, last_name, email, enrollment_date)
        )
        # commit the changes
        db.commit()
        print("\nStudent Added Successfully")

    except Exception as error:

        print("Error Adding Student: ",error)

# Updates the email address for a student with the specified student_id    
def updateStudentEmail(student_id, new_email):
    try:
        #update the specific row of the database using the student id
        db_cur.execute('''UPDATE students SET email = %s WHERE student_id = %s''', (new_email, student_id))
        # commit the changes 
        db.commit()
        print("\nEmail updated successfully")

    except Exception as error:

        print("Error Updating Email: ",error)
    
# Deletes the record of the student with the specified student_id
def deleteStudent(student_id):
    try:
        # delete the specific row of the database using the student id
        db_cur.execute('''DELETE FROM students WHERE student_id = %s ''', (student_id,))
        # commit the changes
        db.commit()
        print("\nStudent Delete Successfully")

    except Exception as error:

        print("Error Deleting Student: ",error)


check =False
#running the while to get the users input and make changes to the database how the user wants.
while check is False:
    
    try:
        #giving the user options to pick from
        action=int(input("\nEnter an option:\n1.Add Student\n2.Update Email Using Student ID\n3.Delete Student Using Student ID \n4.View All Students\n5.Exit\n -->"))

        if action == 1:
            firstName = input("Enter Student's First Name: ")
            lastName = input("Enter Student's Last Name: ")
            email = input("Enter Email Address: ")
            enDate = input("Enter Enrollment Date (YYYY/MM/DD): ")

            addStudent(firstName, lastName, email, enDate)
        
        #if the action is 2 then update the student emiail using the student ID
        elif action == 2:
            student_id = int(input("Enter Student's ID: "))

            studentsIDs = []
            for rows in getAllStudents():
                studentsIDs.append(rows[0])

            if student_id not in studentsIDs:
                print("\nThis ID does not exist! Please try again.")
            else:            
                email = input("Enter New Email Address: ")
                updateStudentEmail(student_id, email)
        
        #if the acion is 3 then delete the student using the student ID
        elif action == 3: 
            student_id = int(input("Enter Student's ID to Delete: "))

            studentsIDs = []
            for rows in getAllStudents():
                studentsIDs.append(rows[0])

            if student_id not in studentsIDs:
                print("\nThis ID does not exist! Please try again.")
            else:
                deleteStudent(student_id)

        # if the action picked is 4 then print all the students
        elif action == 4:
            print("{:<5} {:<15} {:<15} {:<30} {:<15}".format("ID", "First Name", "Last Name", "Email", "Enrollment Date"))
            #loop through the students table and display each record
            for rows in getAllStudents():
                #printing the tuples
                print("{:<5} {:<15} {:<15} {:<30} {:<15}".format(rows[0], rows[1], rows[2], rows[3], rows[-1].strftime('%Y-%m-%d')))

                
        #exit the loop and the program
        elif action == 5:
            db.close()
            db_cur.close()
            check = True
        
        else:
            print("Please enter a valid input!")

    except Exception as error:

        print("Error! Please enter an Integer.",error)
