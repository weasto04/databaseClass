import pandas as pd

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
	SELECT yearID, teamID, sum(HR) as totalHR
    FROM batting
    WHERE teamID = 'PHI'
    GROUP BY yearID
    ORDER BY yearID DESC;
"""
cursor.execute(query)
records = cursor.fetchall()
conn.close()
df = pd.DataFrame(records, columns=['yearID', 'teamID', 'totalHR'])

print(df)