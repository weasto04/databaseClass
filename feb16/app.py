import sqlite3
import pandas as pd
import gradio as gr

def fetch_phillies():
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    query = """
        WITH top_hitters AS (
            SELECT people.nameFirst, people.nameLast
            FROM batting
            INNER JOIN people ON batting.playerID = people.playerID
            WHERE teamID = 'PHI'
            GROUP BY batting.playerID
            ORDER BY sum(batting.HR) DESC
            LIMIT 10
        )
        SELECT CONCAT(nameFirst, ' ', nameLast) as player
        FROM top_hitters
        ORDER BY nameLast ASC;
    """
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    players = []
    for record in records:
        players.append(record[0])
    return players

with gr.Blocks() as iface:
    playerID = gr.Dropdown(choices = fetch_phillies(), interactive = True)

iface.launch()