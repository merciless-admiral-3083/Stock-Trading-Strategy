import pandas as pd
from sqlalchemy import create_engine

# Load the Excel file
file_path = '../data/HINDALCO_1D.xlsx'
df = pd.read_excel(file_path)

# Connect to the database
engine = create_engine('postgresql://username:password@localhost:5432/your_db_name')

# Insert data into the 'stock_data' table
df.to_sql('stock_data', engine, if_exists='append', index=False)
