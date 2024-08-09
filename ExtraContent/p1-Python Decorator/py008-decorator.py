import sqlite3
import time


def retry_on_failure(max_attempts, retry_delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(max_attempts):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as error:
                    print(f"Error occurred: {error}. Retrying...")
                    time.sleep(retry_delay)
            raise Exception("Maximum attempts exceeded. Function failed.")

        return wrapper

    return decorator


@retry_on_failure(max_attempts=3, retry_delay=2)
def establish_database_connection():
    connection = sqlite3.connect("example.db")
    db_cursor = connection.cursor()
    db_cursor.execute("SELECT * FROM users")
    query_result = db_cursor.fetchall()
    db_cursor.close()
    connection.close()
    return query_result


try:
    retrieved_data = establish_database_connection()
    print("Data retrieved successfully:", retrieved_data)
except Exception as error_message:
    print(f"Failed to establish database connection: {error_message}")
