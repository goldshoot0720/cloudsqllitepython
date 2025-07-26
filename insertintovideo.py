import os
from dotenv import load_dotenv
import sqlitecloud

load_dotenv()

conn = sqlitecloud.connect(os.getenv("DATABASE_URL"))
cur = conn.cursor()

cur.execute("""
    INSERT OR IGNORE INTO video
    (name, url, img, type, date, song, site, watch, youtube, year, season)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    "名探偵コナン",
    "https://fra.cloud.appwrite.io/v1/storage/buckets/6867c5280021205ba9c0/files/686ea1e900041219af1e/view?project=680c76af0037a7d23e44",
    "https://fra.cloud.appwrite.io/v1/storage/buckets/6867c5280021205ba9c0/files/686ea1e80016ba6dd7d9/view?project=680c76af0037a7d23e44",
    "OP",
    "2025-07-10 07:10:25",
    "「But ノーラヴ」",
    "https://www.ytv.co.jp/conan/",
    "https://ani.gamer.com.tw/animeVideo.php?sn=30234",
    "https://www.youtube.com/watch?v=agYpVLKBDSE",
    "2025",
    "winter",
))

conn.commit()
cur.close()
conn.close()
