import os
from dotenv import load_dotenv
import sqlitecloud

load_dotenv()

conn = sqlitecloud.connect(os.getenv("DATABASE_URL"))
cur = conn.cursor()

cur.execute("""
    INSERT OR IGNORE INTO subscription (name, site, price, nextdate, note, account)
    VALUES (?, ?, ?, ?, ?, ?)
""", (
    "linode",
    "https://cloud.linode.com/linodes",
    213,
    None,
    "Nanode 1 GB $5美元\nVirtual Private Server",
    "goldshoot0720@gmail.com"
))

conn.commit()
cur.close()
conn.close()
