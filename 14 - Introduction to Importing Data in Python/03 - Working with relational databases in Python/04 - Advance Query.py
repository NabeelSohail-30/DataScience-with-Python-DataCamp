engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    # Perform query and save results to DataFrame: df
    query = '''
    SELECT Album.Title, Artist.Name
    FROM Album
    INNER JOIN Artist ON Album.ArtistID = Artist.ArtistID
    '''
    rs = con.execute(query)
    df = pd.DataFrame(rs.fetchall(), columns=['Title', 'Name'])

# Print head of DataFrame df
print(df.head())

# Execute query and store records in DataFrame: df
# Define the SQL query
query = '''
SELECT *
FROM PlaylistTrack
INNER JOIN Track ON PlaylistTrack.TrackId = Track.TrackId
WHERE Track.Milliseconds < 250000
'''

# Use read_sql_query() to execute the query and store results in DataFrame df
df = pd.read_sql_query(query, engine)

# Print head of DataFrame
print(df.head())

