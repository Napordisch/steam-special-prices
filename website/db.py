from flask import Flask, jsonify
import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'user',
    'password': 'user_password',
    'database': 'game_info'
}

def query_db(query:str):
    try:
        # Connect to the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)

        # Execute a query
        cursor.execute(query)
        results = cursor.fetchall()
        print (f"querying db: \"{query}\" ")
        return (results)

    except mysql.connector.Error as e:
        print(({"error": str(e)}))

    finally:
        # Close connections
        if connection.is_connected():
            cursor.close()
            connection.close()
#
# if __name__ == "__main__":
#     try:
#         # Connect to the database
#         connection = mysql.connector.connect(**db_config)
#         cursor = connection.cursor(dictionary=True)
#
#         # Execute a query
#         query = "SELECT * FROM game_prices"
#         cursor.execute(query)
#         results = cursor.fetchall()
#         for i in results:
#             print(i)
#
#         print((results))
#
#     except mysql.connector.Error as e:
#         print(({"error": str(e)}))
#
#     finally:
#         # Close connections
#         if connection.is_connected():
#             cursor.close()
#             connection.close()