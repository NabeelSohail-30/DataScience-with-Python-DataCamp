# Import necessary packages
from sqlalchemy import create_engine
import pandas as pd

# Create an engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine connection using a context manager
with engine.connect() as con:
    # Define the SQL query
    query = '''
    SELECT Album.Title, Artist.Name
    FROM Album
    INNER JOIN Artist ON Album.ArtistID = Artist.ArtistID
    '''

    # Execute the query and store results in DataFrame df
    rs = con.execute(query)
    df = pd.DataFrame(rs.fetchall(), columns=['Title', 'Name'])

# Print the first few rows of DataFrame df
print("Head of DataFrame:")
print(df.head())

# Define another SQL query
query = '''
SELECT *
FROM PlaylistTrack
INNER JOIN Track ON PlaylistTrack.TrackId = Track.TrackId
WHERE Track.Milliseconds < 250000
'''

# Use read_sql_query() to execute the query and store results in DataFrame df
df = pd.read_sql_query(query, engine)

# Print the first few rows of DataFrame df
print("Head of DataFrame:")
print(df.head())
