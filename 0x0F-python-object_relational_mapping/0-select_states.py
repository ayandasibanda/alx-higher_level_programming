#!/usr/bin/python3
"""
This script connects to a MySQL server running on localhost at port 3306
and lists all states from the database hbtn_0e_0_usa sorted by states.id.
"""

import MySQLdb
import sys

def get_states(username, password, db_name):
    """
    Retrieves and prints all states from the database hbtn_0e_0_usa.
    """
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query
    cursor.execute("SELECT * FROM states ORDER BY id")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL credentials from command line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to get and print states
    get_states(username, password, db_name)

