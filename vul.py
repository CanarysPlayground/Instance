# vul.py

import sqlite3

def get_user_data(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = " + user_id  # ⚠️ SQL Injection
    cursor.execute(query)
    return cursor.fetchall()
