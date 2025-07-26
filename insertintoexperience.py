import os
from dotenv import load_dotenv
import sqlitecloud

load_dotenv()

conn = sqlitecloud.connect(os.getenv("DATABASE_URL"))
cur = conn.cursor()

experiences = [
    ("高考三級資訊處理榜首", "2025", "行政院人事行政總處", "https://www.dgpa.gov.tw"),
    ("台北市長(候選人)", "2038", "台北市政府", "https://www.gov.taipei/"),
]

for exp in experiences:
    cur.execute("""
        INSERT OR IGNORE INTO experience (title, year, gov, site)
        VALUES (?, ?, ?, ?)
    """, exp)

conn.commit()
cur.close()
conn.close()
