
import sqlite3

def query_data(connection, person_id):
    """
    Query and print data for a given person ID.
    """
    cursor = connection.cursor()

    # Query person data
    cursor.execute('SELECT * FROM person WHERE id=?', (person_id,))
    person = cursor.fetchone()
    if person:
        print(f'{person[1]} {person[2]}, {person[3]} years old')

        # Query pets data
        cursor.execute('SELECT pet.* FROM pet JOIN person_pet ON pet.id = person_pet.pet_id WHERE person_pet.person_id=?', (person_id,))
        for pet in cursor.fetchall():
            status = 'dead' if pet[4] else 'alive'
            print(f'Owned {pet[1]}, a {pet[2]}, {pet[3]} years old, {status}')
    else:
        print("Error: No person found with that ID.")

def main():
    # Connect to the SQLite database
    conn = sqlite3.connect('pets.db')

    while True:
        try:
            person_id = int(input("Enter a person's ID number (or -1 to exit): "))
            if person_id == -1:
                break
            query_data(conn, person_id)
        except ValueError:
            print("Please enter a valid integer.")

    # Close the database connection
    conn.close()

if __name__ == '__main__':
    main()
