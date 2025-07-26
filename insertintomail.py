import os
from dotenv import load_dotenv
import sqlitecloud

load_dotenv()

conn = sqlitecloud.connect(os.getenv("DATABASE_URL"))
cur = conn.cursor()

mails = [
    ("goldshoot0720/hotmail", "outlook", "goldshoot0720@hotmail.com", None, None),
    ("abuhg17myyahoo", "gmail", "abuhg17myyahoo@gmail.com", None, None),
    ("goldshoot0720/outlook", "outlook", "goldshoot0720@outlook.com", None, None),
    ("miabubu20xx", "gmail", "miabubu20xx@gmail.com", None, None),
    ("abuhg2016", "gmail", "abuhg2016@gmail.com", None, None),
    ("goldshoot0721", "gmail", "goldshoot0721@gmail.com", None, None),
    ("soilshoot0720", "gmail", "soilshoot0720@gmail.com", None, None),
    ("fireshoot0720", "gmail", "fireshoot0720@gmail.com", None, None),
    ("watershoot0720", "gmail", "watershoot0720@gmail.com", None, None),
    ("woodshoot0720", "gmail", "woodshoot0720@gmail.com", None, None),
    ("ironshoot0720", "gmail", "ironshoot0720@gmail.com", None, None),
    ("coppershoot0720", "gmail", "coppershoot0720@gmail.com", None, None),
    ("silvershoot0720", "gmail", "silvershoot0720@gmail.com", None, None),
    ("tsaopaofenghsiungistaipeimayor", "gmail", "tsaopaofenghsiungistaipeimayor@gmail.com", None, None),
    ("tsaopaofenghsiung202507050418", "gmail", "tsaopaofenghsiung202507050418@gmail.com", None, None),
    ("tsaopaofenghsiung2025", "gmail", "tsaopaofenghsiung2025@gmail.com", None, None),
    ("chbondg2", "gmail", "chbondg2@gmail.com", None, None),
    ("feng33feng35feng3", "gmail", "feng33feng35feng3@gmail.com", None, None),
    ("chbondg2025", "gmail", "chbondg2025@gmail.com", None, None),
    ("goldshoot2025", "gmail", "goldshoot2025@gmail.com", None, None),
    ("tsaopaofenghsiung", "gmail", "tsaopaofenghsiung@gmail.com", None, None),
    ("peoper31206", "gmail", "peoper31206@gmail.com", None, None),
    ("peoper11206", "gmail", "peoper11206@gmail.com", None, None),
    ("fengwithlai1103", "gmail", "fengwithlai1103@gmail.com", None, None),
    ("fengwithtu1127", "gmail", "fengwithtu1127@gmail.com", None, None),
    ("fengwithting0831", "gmail", "fengwithting0831@gmail.com", None, None),
    ("tu0403withyu0723", "gmail", "tu0403withyu0723@gmail.com", None, None),
    ("fengwithfeng1127", "gmail", "fengwithfeng1127@gmail.com", None, None),
    ("abuhg17", "gmail", "abuhg17@gmail.com", None, None),
    ("goldshoot0720/gmail", "gmail", "goldshoot0720@gmail.com", None, None),
    ("goldshoot0720/aol", "aol", "goldshoot0720@aol.com", None, None),
    ("goldshoot0720/zohomail", "zohomail", "goldshoot0720@zohomail.com", None, None),
    ("goldshoot0720/yandex", "yandex", "goldshoot0720@yandex.com", None, None),
    ("goldshoot0720/vk", "vk", "goldshoot0720@vk.com", None, None),
    ("goldshoot0720/naver", "naver", "goldshoot0720@naver.com", None, None),
    ("goldshoot0720/daum", "daum", "goldshoot0720@daum.net", None, None),
]

for mail in mails:
    cur.execute("""
        INSERT OR IGNORE INTO mail (name, host, address, account, site)
        VALUES (?, ?, ?, ?, ?)
    """, mail)

conn.commit()
cur.close()
conn.close()
