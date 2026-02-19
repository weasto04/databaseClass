import sqlite3
import pandas as pd
import gradio as gr


conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
    WITH top_hitters AS (
            SELECT people.nameFirst, people.nameLast, batting.playerID
            FROM batting
            INNER JOIN people ON batting.playerID = people.playerID
            WHERE teamID = 'PHI'
            GROUP BY batting.playerID
            ORDER BY sum(batting.HR) DESC
            LIMIT 10
        )
        SELECT CONCAT(nameFirst, ' ', nameLast) as player, playerID
        FROM top_hitters
        ORDER BY nameLast ASC;
    """
cursor.execute(query)
records = cursor.fetchall()
conn.close()
#players = []
#for record in records:
#    players.append(record[0])

with gr.Blocks() as iface:
    playerID = gr.Dropdown(choices = records, interactive = True)

iface.launch()