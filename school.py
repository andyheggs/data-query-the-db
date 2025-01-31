# pylint:disable=C0111,C0103

def students_from_city(db, city):
    """return a list of students from a specific city"""

    # Define query
    query = "SELECT * FROM students AS student WHERE birth_city = ?"

    # Execute query w specified city
    db.execute(query, (city,))

    # Fetch results
    results = db.fetchall()

    # Close con
    conn.close()

    return results


import sqlite3
conn = sqlite3.connect('data/school.sqlite')
db = conn.cursor()
print(students_from_city(db, 'Paris'))
