# Import necessary packages
from sqlalchemy import create_engine
import pandas as pd

# Create an engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine connection using context manager: con
with engine.connect() as con:
    # Execute SQL query and store results in rs
    rs = con.execute('SELECT * FROM Album')

    # Convert the query results to a DataFrame: df
    df = pd.DataFrame(rs.fetchall())

# Print the first few rows of the DataFrame df
print(df.head())

# Open engine connection using context manager and fetch only a few rows
with engine.connect() as con:
    # Execute SQL query and store results in rs
    rs = con.execute('SELECT LastName, Title FROM Employee')

    # Fetch a limited number of rows and store in df
    df = pd.DataFrame(rs.fetchmany(3))

    # Set column names using the keys of the result set
    df.columns = rs.keys()

# Print the length and the first few rows of the DataFrame df
print(len(df))
print(df.head())

# Open engine connection using context manager and filter rows
with engine.connect() as con:
    # Execute SQL query and store results in rs
    rs = con.execute('SELECT * FROM Employee WHERE EmployeeId >= 6')

    # Fetch all rows and store in df
    df = pd.DataFrame(rs.fetchall())

    # Set column names using the keys of the result set
    df.columns = rs.keys()

# Print the first few rows of the DataFrame df
print(df.head())

# Open engine connection using context manager, order rows and fetch all
with engine.connect() as con:
    # Execute SQL query and store results in rs
    rs = con.execute('SELECT * FROM Employee ORDER BY BirthDate')

    # Fetch all rows and store in df
    df = pd.DataFrame(rs.fetchall())

    # Set column names using the keys of the result set
    df.columns = rs.keys()

# Print the first few rows of the DataFrame df
print(df.head())
