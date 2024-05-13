import psycopg2

from dotenv import load_dotenv
import os
load_dotenv() 
pgpassword = os.getenv('POSTGRES_PASSWORD')

if pgpassword is None:
    print("Error: POSTGRES_PASSWORD variable is not set")
    exit(1)

conn = None
try:
    conn = psycopg2.connect(
        user="postgres",
        password=pgpassword,
        host="localhost",
        port="5432",
        database="postgres")
except Exception as e:
    print("Error connecting to data warehouse")
    print(e)
else:
    print("Successfully connected to warehouse")
finally:
    if conn:
        conn.close()
        print("Connection closed")