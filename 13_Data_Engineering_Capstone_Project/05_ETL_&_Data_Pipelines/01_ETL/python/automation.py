# Import libraries required for connecting to mysql
import mysql.connector

# Import libraries required for connecting to DB2 or PostgreSql
import psycopg2

# Connect to MySQL
mysql_conn = mysql.connector.connect(
    user="root", password="1234", host="localhost", database="sales"
)
mysql_cursor = mysql_conn.cursor()

# Connect to DB2 or PostgreSql
postgres_conn = psycopg2.connect(
    database="postgres", user="postgres", password="1234", host="127.0.0.1", port="5432"
)
postgres_cursor = postgres_conn.cursor()

# Find out the last rowid from DB2 data warehouse or PostgreSql data warehouse
# The function get_last_rowid must return the last rowid of the table sales_data on the IBM DB2 database or PostgreSql.


def get_last_rowid():
    query = "SELECT MAX(rowid) FROM sales_data"
    postgres_cursor.execute(query)
    result = postgres_cursor.fetchone()
    return result[0] if result[0] is not None else 0


last_row_id = get_last_rowid()
print("Last row id on production datawarehouse = ", last_row_id)

# List out all records in MySQL database with rowid greater than the one on the Data warehouse
# The function get_latest_records must return a list of all records that have a rowid greater than the last_row_id in the sales_data table in the sales database on the MySQL staging data warehouse.


def get_latest_records(rowid):
    query = "SELECT * FROM sales_data WHERE rowid > %s"
    mysql_cursor.execute(query, (rowid,))
    return mysql_cursor.fetchall()


new_records = get_latest_records(last_row_id)
print("New rows on staging datawarehouse = ", len(new_records))

# Insert the additional records from MySQL into DB2 or PostgreSql data warehouse.
# The function insert_records must insert all the records passed to it into the sales_data table in IBM DB2 database or PostgreSql.


def insert_records(records):
    insert_query = """
    INSERT INTO sales_data (rowid, product_id, customer_id, quantity, timestamp)
    VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP)
    """
    for record in records:
        postgres_cursor.execute(insert_query, record)
    postgres_conn.commit()


insert_records(new_records)
print("New rows inserted into production datawarehouse = ", len(new_records))

# disconnect from mysql warehouse
mysql_cursor.close()
mysql_conn.close()
# disconnect from DB2 or PostgreSql data warehouse
postgres_cursor.close()
postgres_conn.close()
# End of program
