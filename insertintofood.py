import os
from dotenv import load_dotenv
import sqlitecloud

load_dotenv()

conn = sqlitecloud.connect(os.getenv("DATABASE_URL"))
cur = conn.cursor()

cur.execute("""
    INSERT OR IGNORE INTO food (name, amount, price, shop, todate, photo, photoHash)
    VALUES (?, ?, ?, ?, ?, ?, ?)
""", (
    "大甲芋泥布丁 獨享寶盒",
    2,
    70,
    "聖瑪莉",
    "2025-07-10",
    "https://fra.cloud.appwrite.io/v1/storage/buckets/6867c5280021205ba9c0/files/686ea805003903aa8c46/view?project=680c76af0037a7d23e44",
    "655fe96fb4cb74007001cd21b2e3d3599e041cbe97b74e912a6ae2493da4eb22"
))

conn.commit()
cur.close()
conn.close()
