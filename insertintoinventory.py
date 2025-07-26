import os
from dotenv import load_dotenv
import sqlitecloud

load_dotenv()

conn = sqlitecloud.connect(os.getenv("DATABASE_URL"))
cur = conn.cursor()

items = [
    (
        "芋泥蒙布朗布丁",
        55,
        1,
        "全家",
        None,  # img1 NULL
        None,  # img2 NULL
        None,  # img3 NULL
    ),
    (
        "香蕉巧克力夾心酥",
        49,
        1,
        "全家",
        None,
        None,
        None,
    ),
]

for item in items:
    cur.execute("""
        INSERT OR IGNORE INTO inventory (name, price, amount, shop, img1, img2, img3)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, item)

conn.commit()
cur.close()
conn.close()
