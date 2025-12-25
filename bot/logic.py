import sqlite3
import os

bot_token = "8184400151:AAHJpwUSGgniNyOejr25UIn2BH61eAHO6Aw"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "professions.db")

def get_professions_by_answers(category, energy, goal):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, description
        FROM professions
        WHERE category=? AND energy=? AND goal=?
        LIMIT 3
    """, (category, energy, goal))

    result = cursor.fetchall()
    conn.close()
    return result
