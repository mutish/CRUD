import sqlite3
# connection to the db
# execute the schema script : executes multiple sql statements at once
connection = sqlite3.connect('database.db')
with open('schema.sql') as f:
    connection.executescript(f.read())
#setting up cursor for navigation ability
# cursor object allows one to process rows in a db
cursor = connection.cursor()
# dummy content
cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ('First post', 'content first post'))
cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ('Second post', 'content second post'))

# committing....
connection.commit()

# ...then close the connection.
connection.close()