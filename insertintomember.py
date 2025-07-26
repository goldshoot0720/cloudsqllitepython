import os
from dotenv import load_dotenv
import sqlitecloud

load_dotenv()

conn = sqlitecloud.connect(os.getenv("DATABASE_URL"))
cur = conn.cursor()

cur.execute("""
    INSERT OR IGNORE INTO member (name, title, relation, gov, site, img)
    VALUES (?, ?, ?, ?, ?, ?)
""", (
    "塗○傑",
    "董事",
    "國中同班同學",
    "臺北農產運銷股份有限公司",
    "https://www.tapmc.com.tw",
    None
))

conn.commit()
cur.close()
conn.close()
