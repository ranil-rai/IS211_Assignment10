
import sqlite3

def insert_data(connection, table, data):
    """
    Insert data into the given table.
    """
    cursor = connection.cursor()
    for row in data:
        placeholders = ', '.join(['?'] * len(row))
        query = f'INSERT INTO {table} VALUES ({placeholders})'
        cursor.execute(query, row)
    connection.commit()

def main():
    # Connect to the SQLite database
    conn = sqlite3.connect('pets.db')

    # Data to insert
    persons = [
        (1, 'James', 'Smith', 41),
        (2, 'Diana', 'Greene', 23),
        (3, 'Sara', 'White', 27),
        (4, 'William', 'Gibson', 23)
    ]

    pets = [
        (1, 'Rusty', 'Dalmation', 4, 1),
        (2, 'Bella', 'Alaskan Malamute', 3, 0),
        (3, 'Max', 'Cocker Spaniel', 1, 0),
        (4, 'Rocky', 'Beagle', 7, 0),
        (5, 'Rufus', 'Cocker Spaniel', 1, 0),
        (6, 'Spot', 'Bloodhound', 2, 1)
    ]

    person_pet = [
        (1, 1),
        (1, 2),
        (2, 3),
        (2, 4),
        (3, 5),
        (4, 6)
    ]

    # Insert data into tables
    insert_data(conn, 'person', persons)
    insert_data(conn, 'pet', pets)
    insert_data(conn, 'person_pet', person_pet)

    # Close the database connection
    conn.close()

if __name__ == '__main__':
    main()
