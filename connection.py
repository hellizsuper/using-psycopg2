import psycopg2

DB_NAME = "checkdb"
DB_USER = "postgres"
DB_PASS = "123"
DB_HOST = "localhost"
DB_PORT = "5432"

try:
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

    print("Database Connected Successfully")

except:
    print("Database Not Connected")
