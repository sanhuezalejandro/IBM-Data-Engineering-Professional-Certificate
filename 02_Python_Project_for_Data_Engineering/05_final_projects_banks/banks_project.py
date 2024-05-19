from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlite3
from datetime import datetime


def log_progress(message):
    """This function logs the mentioned message at a given stage of the
    code execution to a log file. Function returns nothing."""

    timestamp_format = "%Y-%h-%d-%H:%M:%S"  # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now()  # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("./code_log.txt", "a") as f:
        f.write(timestamp + " : " + message + "\n")


def extract(url, table_attribs):
    """The purpose of this function is to extract the required
    information from the website and save it to a dataframe. The
    function returns the dataframe for further processing."""

    page = requests.get(url).text
    data = BeautifulSoup(page, "html.parser")
    df = pd.DataFrame(columns=table_attribs)
    tables = data.find_all("table")
    rows = tables[0].find_all("tr")
    for row in rows:
        col = row.find_all("td")
        if len(col) != 0:
            data_dict = {
                "Name": col[1].text.strip(),
                "MC_USD_Billion": col[2].text.strip(),
            }
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)
    return df


def transform(df):
    """This function converts the GDP information from Currency
    format to float value, transforms the information of GDP from
    USD (Millions) to USD (Billions) rounding to 2 decimal places.
    The function returns the transformed dataframe."""

    # Convert 'MC_USD_Billion' column to numeric if it's not already
    df["MC_USD_Billion"] = pd.to_numeric(df["MC_USD_Billion"], errors="coerce")
    # Add MC_GBP_Billion column
    df["MC_GBP_Billion"] = (df["MC_USD_Billion"] * exchange_rate_dict["GBP"]).round(2)
    # Add MC_EUR_Billion column
    df["MC_EUR_Billion"] = (df["MC_USD_Billion"] * exchange_rate_dict["EUR"]).round(2)
    # Add MC_INR_Billion column
    df["MC_INR_Billion"] = (df["MC_USD_Billion"] * exchange_rate_dict["INR"]).round(2)

    return df


def load_to_csv(df, csv_path):
    """This function saves the final dataframe as a `CSV` file
    in the provided path. Function returns nothing."""

    df.to_csv(csv_path)


def load_to_db(df, sql_connection, table_name):
    """This function saves the final dataframe to as a database table
    with the provided name. Function returns nothing."""

    df.to_sql(table_name, sql_connection, if_exists="replace", index=False)


def run_query(query_statement, sql_connection):
    """This function runs the stated query on the database table and
    prints the output on the terminal. Function returns nothing."""

    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)


""" Here, you define the required entities and call the relevant 
functions in the correct order to complete the project. Note that this
portion is not inside any function."""

url = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
table_attribs = ["Name", "MC_USD_Billion"]
db_name = "Banks.db"
table_name = "Largest_banks"
csv_path = "./Largest_banks_data.csv"

# Read the CSV file into a DataFrame
rates = pd.read_csv("exchange_rate.csv")
# Set the 'Currency' column as the index and convert to a dictionary
exchange_rate_dict = rates.set_index("Currency")["Rate"].to_dict()

log_progress("Preliminaries complete. Initiating ETL process")

df = extract(url, table_attribs)

log_progress("Data extraction complete. Initiating Transformation process")

df = transform(df)

log_progress("Data transformation complete. Initiating loading process")

load_to_csv(df, csv_path)

log_progress("Data saved to CSV file")

sql_connection = sqlite3.connect(db_name)

log_progress("SQL Connection initiated.")

load_to_db(df, sql_connection, table_name)

log_progress("Data loaded to Database as table. Executing queries")

query_statement = f"SELECT * from {table_name}"
run_query(query_statement, sql_connection)

query_statement = f"SELECT AVG(MC_GBP_Billion) from {table_name}"
run_query(query_statement, sql_connection)

query_statement = f"SELECT Name from {table_name} LIMIT 5"
run_query(query_statement, sql_connection)

log_progress("Process Complete.")

sql_connection.close()

log_progress("Server Connection closed")
