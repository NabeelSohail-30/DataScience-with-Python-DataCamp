# Import necessary packages
from sqlalchemy import create_engine
import pandas as pd

# Create an engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in a DataFrame: df
df = pd.read_sql_query('SELECT * FROM Album', engine)

# Print the first few rows of the DataFrame
print("Head of DataFrame:")
print(df.head())

# Open engine connection using a context manager and store query result in df1
with engine.connect() as con:
    # Execute SQL query and store results in rs
    rs = con.execute("SELECT * FROM Album")

    # Fetch all rows and store in df1
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

# Confirm that both methods yield the same result
print("Results are equal:", df.equals(df1))

# Import necessary packages
from sqlalchemy import create_engine
import pandas as pd

# Create an engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in a DataFrame: df
df = pd.read_sql_query(
    "SELECT * FROM Employee WHERE EmployeeId >= 6 ORDER BY BirthDate",
    engine
)

# Print the first few rows of the DataFrame
print("Head of DataFrame:")
print(df.head())
