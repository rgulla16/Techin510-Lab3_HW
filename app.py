import sqlite3
import psycopg2
import os
from datetime import datetime

import streamlit as st
from pydantic import BaseModel
import streamlit_pydantic as sp

# Connect to our database
DB_CONFIG = os.getenv("DB_TYPE")
if DB_CONFIG == 'PG':
    PG_USER = os.getenv("PG_USER")
    PG_PASSWORD = os.getenv("PG_PASSWORD")
    PG_HOST = os.getenv("PG_HOST")
    PG_PORT = os.getenv("PG_PORT")
    con = psycopg2.connect(f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/todoapp?connect_timeout=10&application_name=todoapp")
else:
    con = sqlite3.connect("todoapp.sqlite", isolation_level=None)
cur = con.cursor()

# Create the table
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT,
        state TEXT,
        created_at TIMESTAMP,
        created_by TEXT,
        category TEXT
    )
    """
)

# Define our Form
class Task(BaseModel):
    name: str
    description: str
    state: str
    created_at: datetime
    created_by: str
    category: str

# This function will be called when the check mark is toggled, this is called a callback function
def toggle_state(state, row):
    cur.execute(
        """
        UPDATE tasks SET state = ? WHERE id = ?
        """,
        (state, row[0]),
    )

def main():
    st.title("Ravinder's Winter Quarter Assignments Reminder")

    # Create a Form using the streamlit-pydantic package, just pass it the Task Class
    data = sp.pydantic_form(key="task_form", model=Task)
    if data:
        cur.execute(
            """
            INSERT INTO tasks (name, description, state, created_at, created_by, category)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (data.name, data.description, data.state, data.created_at, data.created_by, data.category),
        )

    data = cur.execute(
        """
        SELECT * FROM tasks
        """
    ).fetchall()

    # HINT: how to implement an Edit button?
    # if st.query_params.get('id') == "123":
    #     st.write("Hello 123")
    #     st.markdown(
    #         f'<a target="_self" href="/" style="display: inline-block; padding: 6px 10px; background-color: #4CAF50; color: white; text-align: center; text-decoration: none; font-size: 12px; border-radius: 4px;">Back</a>',
    #         unsafe_allow_html=True,
    #     )
    #     return

    cols = st.columns(6)
    cols[0].write("Done?")
    cols[1].write("Name")
    cols[2].write("Description")
    cols[3].write("State")
    cols[4].write("Created At")
    cols[5].write("Created By")
    
    for row in data:
        cols = st.columns(6)
        cols[0].checkbox('state', row[3], label_visibility='hidden', key=row[0], on_change=toggle_state, args=(not row[3], row))
        cols[1].write(row[1])
        cols[2].write(row[2])
        cols[3].write(row[3])
    
main()