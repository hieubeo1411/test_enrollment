import json
import pandas as pd
from sqlalchemy import create_engine, Table, Column, Integer, String, Date, MetaData
from datetime import datetime

# Step 1: Define connection to the SQL database
# Example: Connection string for Microsoft SQL Server
# For SQLite (for testing), the connection string would be: sqlite:///employees.db
DATABASE_URI = 'mssql+pyodbc://sa:Passw0rd123@192.168.1.100/MyDatabase?driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(DATABASE_URI)

# Step 2: Define the table structure using SQLAlchemy's MetaData
metadata = MetaData()

employees_table = Table('employees', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('name', String),
                        Column('department', String),
                        Column('salary', Integer),
                        Column('join_date', Date)
                        )

# Step 3: Create the table if it does not exist
metadata.create_all(engine)

# Step 4: Extract data from the JSON file
with open('employees.json', 'r') as file:
    data = json.load(file)

# Step 5: Transform the data
# Convert the data into a pandas DataFrame for easy manipulation
df = pd.DataFrame(data)

# Convert 'join_date' from string to datetime object
df['join_date'] = pd.to_datetime(df['join_date'])

# Step 6: Load the data into the database
try:
    # Use the DataFrame's `to_sql` method to load data into the table
    df.to_sql('employees', con=engine, if_exists='append', index=False)
    print("Data loaded successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
