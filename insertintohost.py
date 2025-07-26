import os
from dotenv import load_dotenv
import sqlitecloud

load_dotenv()

conn = sqlitecloud.connect(os.getenv("DATABASE_URL"))
cur = conn.cursor()

cur.execute("""
    INSERT OR IGNORE INTO host (name, site, account)
    VALUES (?, ?, ?)
""", (
    "wordpress/miabubu20xx",
    "https://wordpress.com/",
    "miabubu20xx@gmail.com",
))

conn.commit()
cur.close()
conn.close()
