import psycopg2
import dotenv
import os

def main():
    connection = connect("ASX")
    crsr = connection.cursor()
    init_db(crsr)

    print("Hello User, welcome to the Investment System!")
    print("What would you like to do today?")
    print("1. View companies")
    print("2. Add a new company")
    print("3. Update an existing company")
    print("4. Delete a company")
    choice = input("Please enter the number of your choice: ")

    crsr.close()
    close_connection(connection, "ASX")

def init_db(crsr):
    crsr.execute("""
        CREATE TABLE IF NOT EXISTS company (
            id SERIAL PRIMARY KEY,
            ticker VARCHAR(10) UNIQUE NOT NULL,
            name VARCHAR(100) NOT NULL,
            sector VARCHAR(50),
            industry VARCHAR(50)
        );
    """)
    crsr.connection.commit()

def connect(dbname):
    dotenv.load_dotenv()
    USER = os.getenv("SQLUSER")
    PASSWORD = os.getenv("SQLPASSWORD")
    connection = None
    try: 
        print(f"Connecting to database {dbname}...")
        connection = psycopg2.connect(
            host="localhost",
            database=dbname,
            user=USER,
            password=PASSWORD
            )
        return connection
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def close_connection(connection, dbname):
    print(f"Closing connection to database {dbname}...")
    try: 
        connection.close()
        print("Connection closed successfully")
    except(Exception, psycopg2.DatabaseError) as DBError:
        print(DBError)

if __name__ == '__main__':
    main()