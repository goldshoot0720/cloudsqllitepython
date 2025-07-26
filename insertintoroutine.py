import os
from dotenv import load_dotenv
import sqlitecloud

load_dotenv()

conn = sqlitecloud.connect(os.getenv("DATABASE_URL"))
cur = conn.cursor()

cur.execute("""
    INSERT OR IGNORE INTO routine (name, date1, date2, date3, note, site)
    VALUES (?, ?, ?, ?, ?, ?)
""", (
    "天晟/身心科/譚詠康",
    "2025-07-31",
    None,
    None,
    "買潤餅",
    "https://www.tcmg.com.tw/index.php/main/schedule_time?id=14"
))

conn.commit()
cur.close()
conn.close()
