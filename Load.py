import pandas as pd
from sqlalchemy import create_engine

conn_string = 'postgresql://postgres:system@localhost/MY_Database'
db = create_engine(conn_string)
conn = db.connect()
file_name = "tourism"
df = pd.read_csv(f'{file_name}.csv')
df.to_sql(file_name,con=conn,if_exists='replace',index=False)