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


from typing import Optional, Sequence, Any, List, Dict
import mysql.connector
import time

def query_db(query: str, params: Optional[Sequence[Any]] = None) -> List[Dict]:
    """
    Execute a (possibly parameterized) query and return a list of dict rows.

    Usage:
      query_db("SELECT * FROM my_table WHERE id = %s", (some_id,))
      query_db("SELECT * FROM my_table")  # no params
    """
    connection_attempts = 0

    while connection_attempts < 10:
        connection_attempts += 1
        connection = None
        cursor = None
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor(dictionary=True)

            # execute with or without params
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            results = cursor.fetchall()
            return results

        except mysql.connector.Error as e:
            print({"error": str(e)})
            time.sleep(5)
            continue

        finally:
            # Close cursor and connection if they were created
            try:
                if cursor is not None:
                    cursor.close()
            except Exception:
                pass

            try:
                if connection is not None and connection.is_connected():
                    connection.close()
            except Exception:
                pass

    # After retries failed, return empty list (or raise)
    return []
