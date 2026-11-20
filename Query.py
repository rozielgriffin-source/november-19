import sqlite3
import pandas as pd

database = 'cricket.db'

conn = sqlite3.connect(database)

query = """SELECT MIN(Season_Id), MAX(Season_Id) FROM Match;"""
seasons = pd.read_sql(query, conn)
print(seasons)