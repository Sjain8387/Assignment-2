import mysql.connector

def execute_sql():
    db_config = {
        'user': '${{ secrets.DB_USERNAME }}',
        'password': '${{ secrets.DB_PASSWORD }}',
        'host': '${{ secrets.DB_HOST }}',
        'database': '${{ secrets.DB_NAME }}',
    }

    try:
        # Connect to the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Read SQL file
        with open('update_companydb.sql', 'r') as file:
            sql_script = file.read()

        # Split and execute each SQL command
        commands = sql_script.split(';')
        for command in commands:
            if command.strip():
                cursor.execute(command)

        # Commit the transaction
        connection.commit()
        print("SQL script executed successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection.rollback()

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    execute_sql()
