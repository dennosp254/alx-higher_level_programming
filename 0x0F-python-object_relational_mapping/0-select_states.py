#!/usr/bin/python3  
import MySQLdb  
import sys  

def main():  
    # Get arguments from command line  
    mysql_user = sys.argv[1]  
    mysql_password = sys.argv[2]  
    database_name = sys.argv[3]  

    # Connect to the MySQL server  
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_user, passwd=mysql_password, db=database_name)  

    # Create a cursor to execute SQL queries  
    cursor = db.cursor()  

    # Execute the query to select all states, sorted by id  
    cursor.execute("SELECT * FROM states ORDER BY id ASC")  

    # Fetch all results  
    results = cursor.fetchall()  

    # Display results  
    for row in results:  
        print(row)  

    # Close the cursor and database connection  
    cursor.close()  
    db.close()  

if __name__ == "__main__":  
    main()
