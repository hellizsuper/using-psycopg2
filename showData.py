import psycopg2

DB_NAME = "checkdb"
DB_USER = "postgres"
DB_PASS = "123"
DB_HOST = "localhost"
DB_PORT = "5432"

conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

print("Database Connected Successfully")

cur = conn.cursor()
cur.execute("SELECT * from tblUsers")

data = cur.fetchall()

for x in data:
    print("ID: "+str(x[0]))
    print("NAME: " + str(x[1]))
    print("EMAIL: " + str(x[2]))

print("Data Fetched Successfully")
conn.close()