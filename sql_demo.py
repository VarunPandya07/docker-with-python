import mysql.connector
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector.abstracts import MySQLConnectionAbstract


def create_connection() -> PooledMySQLConnection | MySQLConnectionAbstract:
    try:
        return mysql.connector.connect(
            host="mysqldb",  
            user="root",
            password="root",
            database="mydata"
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        exit(1)

def create_table(connection: PooledMySQLConnection | MySQLConnectionAbstract):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS names (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255)
        )
    """)
    connection.commit()
    cursor.close()

def insert_name(connection: PooledMySQLConnection | MySQLConnectionAbstract, name: str):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO names (name) VALUES (%s)", (name,))
    connection.commit()
    cursor.close()

    with open("server.txt", 'a') as file:
        file.write(name+"\n")

def fetch_all_names(connection: PooledMySQLConnection | MySQLConnectionAbstract):
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM names")
    names = [row[0] for row in cursor.fetchall()]
    cursor.close()
    return names

def main():
    connection = create_connection()
    create_table(connection)

    while True:
        print("\n1. Add a name")
        print("2. Show all names")
        print("3. Quit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            insert_name(connection, name)
            print(f"Name '{name}' added to the database.")
        elif choice == "2":
            names = fetch_all_names(connection)
            if names:
                print("Names in the database:")
                for name in names:
                    print(name)
            else:
                print("No names found in the database.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    connection.close()

if __name__ == "__main__":
    main()
