import sqlite3
import pandas as pd

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
    SELECT playerID, teams.yearID, batting.HR, name
    FROM batting inner join teams
    ON batting.yearID = teams.yearID AND batting.teamID = teams.teamID
    WHERE playerID = 'ruthba01';
"""
cursor.execute(query)
records = cursor.fetchall()
conn.close()

df = pd.DataFrame(records, columns = ['playerID', 'yearID', 'HR', 'TeamName'])

print(df)