import os
from dotenv import load_dotenv
import sqlitecloud

load_dotenv()

conn = sqlitecloud.connect(os.getenv("DATABASE_URL"))
cur = conn.cursor()

cloud_accounts = [
    ("dropbox/goldshoot0720", "https://www.dropbox.com/", "goldshoot0720@gmail.com", 5),
    ("InfiniCLOUD", "https://infini-cloud.net", "goldshoot0720@gmail.com", 48),
]

for account in cloud_accounts:
    cur.execute("""
        INSERT OR IGNORE INTO cloud (name, site, account, space)
        VALUES (?, ?, ?, ?)
    """, account)

conn.commit()
cur.close()
conn.close()
