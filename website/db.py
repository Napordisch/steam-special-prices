import mysql.connector
import os
import time

# db_config = {
#     'host': os.environ.get("DB_HOST"),
#     'user': os.environ.get("DB_LOGIN"),
#     'password': os.environ.get("DB_PASSWORD"),
#     'database': os.environ.get("DB_NAME")
# }
db_config = {
    'host': "localhost",
    'user': "user",
    'password': "user_password",
    'database': "game_info"
}


def query_db(query: str):
    connection_attempts = 0
    while connection_attempts < 10:
        connection_attempts += 1
        try:
            # Connect to the database
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor(dictionary=True)

            # Execute a query
            cursor.execute(query)
            results = cursor.fetchall()
            return (results)

        except mysql.connector.Error as e:
            print(({"error": str(e)}))
            time.sleep(5)

            continue

        finally:
            # Close connections
            if connection.is_connected():
                cursor.close()
                connection.close()
