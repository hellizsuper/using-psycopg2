import psycopg2

DB_NAME = "checkdb"
DB_USER = "postgres"
DB_PASS = "123"
DB_HOST = "localhost"
DB_PORT = "5432"

conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

print("Database Connected Successfully")

cur = conn.cursor()
# cur.execute("""
#     CREATE TABLE tblUsers
#     (
#     user_id INT PRIMARY KEY NOT NULL,
#     user_name TEXT NOT NULL,
#     user_email TEXT NOT NULL
#     );
# """)

cur.execute("INSERT INTO tblUsers (user_id, user_name, user_email) VALUES (2, 'Amin', 'aminhussaini@gmail.com')")

conn.commit()
# print("Table Users created Successfully")
print("Data inserted Successfully")
conn.close()