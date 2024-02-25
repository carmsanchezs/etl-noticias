import pandas as pd
from sqlalchemy import create_engine, text

# read the data
df = pd.read_csv(r"data_files/data_100GreatestMovies.csv")
df.set_index('position', inplace=True)

# connect to the database
connection_string = "mysql+mysqlconnector://<user>:<password>@<host>:<port>/<database>"

try:
    # Connect to the database
    engine = create_engine(connection_string)

    # Test the connection by executing a simple query
    with engine.connect() as connection:
        # create the table with the structure that we need
        df.to_sql(name='movies', con=connection, if_exists='replace')

        print(pd.io.sql.get_schema(df, name='movies', con=connection))

except Exception as e:
    print("Connection failed:", e)
