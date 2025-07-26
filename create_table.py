import os
from dotenv import load_dotenv
import sqlitecloud

# 載入環境變數
load_dotenv()

# 建立連線
conn = sqlitecloud.connect(os.getenv("DATABASE_URL"))
cur = conn.cursor()

# 各資料表的建表 SQL（使用 AUTOINCREMENT 替代 serial）
tables = {
    "article": """
        CREATE TABLE IF NOT EXISTS article (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT UNIQUE,
            content TEXT,
            newDate TIMESTAMP,
            url1 TEXT,
            url2 TEXT,
            url3 TEXT,
            file1 BLOB,
            file1type TEXT,
            file2 BLOB,
            file2type TEXT,
            file3 BLOB,
            file3type TEXT
        );
    """,
    "mail": """
        CREATE TABLE IF NOT EXISTS mail (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            host TEXT,
            address TEXT,
            account TEXT,
            site TEXT
        );
    """,
    "inventory": """
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            price INTEGER,
            amount INTEGER,
            shop TEXT,
            img1 BLOB,
            img2 BLOB,
            img3 BLOB
        );
    """,
    "experience": """
        CREATE TABLE IF NOT EXISTS experience (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT UNIQUE,
            year INTEGER,
            gov TEXT,
            site TEXT
        );
    """,
    "member": """
        CREATE TABLE IF NOT EXISTS member (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            title TEXT,
            relation TEXT,
            gov TEXT,
            site TEXT,
            img TEXT
        );
    """,
    "bank": """
        CREATE TABLE IF NOT EXISTS bank (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            deposit INTEGER,
            site TEXT,
            address TEXT,
            withdrawals INTEGER,
            transfer INTEGER,
            activity TEXT,
            card TEXT,
            account TEXT
        );
    """,
    "cloud": """
        CREATE TABLE IF NOT EXISTS cloud (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            site TEXT,
            account TEXT,
            space INTEGER
        );
    """,
    "routine": """
        CREATE TABLE IF NOT EXISTS routine (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            date1 DATE,
            date2 DATE,
            date3 DATE,
            note TEXT,
            site TEXT
        );
    """,
    "host": """
        CREATE TABLE IF NOT EXISTS host (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            site TEXT,
            account TEXT
        );
    """,
    "subscription": """
        CREATE TABLE IF NOT EXISTS subscription (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            site TEXT,
            price INTEGER,
            nextdate DATE,
            note TEXT,
            account TEXT
        );
    """,
    "video": """
        CREATE TABLE IF NOT EXISTS video (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            url TEXT,
            img TEXT,
            type TEXT,
            date TEXT,
            song TEXT,
            site TEXT,
            watch TEXT,
            youtube TEXT,
            year INTEGER,
            season TEXT
        );
    """,
    "food": """
        CREATE TABLE IF NOT EXISTS food (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            amount INTEGER,
            price INTEGER,
            shop TEXT,
            todate TEXT,
            photo TEXT,
            photoHash TEXT
        );
    """
}

# 執行建表
for name, sql in tables.items():
    cur.execute(sql)

conn.commit()
conn.close()
