import sqlite3

conn = sqlite3.connect('database.db')

conn.execute('CREATE TABLE users (username TEXT, password TEXT)')

conn.close()

print("Database Ready")