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

