import sqlite3

conn = sqlite3.connect("alerts.db")
cursor = conn.cursor()

# count rows
cursor.execute("SELECT COUNT(*) FROM alerts")
count = cursor.fetchone()[0]
print(f"Total alerts in database: {count}")

# fetch all rows (optional)
cursor.execute("SELECT * FROM alerts")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
