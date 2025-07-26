import os
from dotenv import load_dotenv
import sqlitecloud

# 載入環境變數
load_dotenv()

# 建立連線
conn = sqlitecloud.connect(os.getenv("DATABASE_URL"))
cur = conn.cursor()

banks = [
    (
        "台北富邦",
        624,
        "https://www.fubon.com/banking/personal/",
        """中平分行  
存款機
桃園市中壢區復興路76號1樓
中壢分行
存款機 
桃園市中壢區中北路二段119號
""",
        5,
        5,
        "https://www.fubon.com/banking/personal/credit_card/all_card/fubonbraves_debit/fubonbraves_debit.htm",
        "勇士簽帳金融卡 末四碼 9907",
        "營業部 末五碼 20819"
    ),
    (
        "兆豐/存摺",
        0,
        "https://www.megabank.com.tw/personal",
        """中壢分行  
臺幣存款機 
桃園市中壢區復興路46號 
""",
        0,
        0,
        "https://wwwfile.megabank.com.tw/event/megalite/index.html",
        "一般金融卡",
        "中壢分行 末五碼 52678"
    ),
    (
        "國泰世華",
        0,
        "https://www.cathay-cube.com.tw/cathaybk",
        """中壢分行
存款	
桃園市中壢區中央西路一段１１號 
全聯
""",
        0,
        0,
        "https://www.cathaybk.com.tw/cathaybk/personal/product/credit-card/cards/i-debit/",
        "CUBE 簽帳金融卡 末四碼 1588",
        "中壢分行 末五碼 30607"
    ),
    (
        "王道銀行",
        0,
        "https://www.o-bank.com/retail",
        "無中壢分行",
        10,
        0,
        "https://www.o-bank.com/retail/event/event-announce/CM_withdraw",
        "金山財神廟招財認同卡 末四碼 ????",
        "營業部 末五碼 75588"
    ),
    (
        "郵局/存摺",
        0,
        "https://www.post.gov.tw/post/internet/Group/default.jsp/",
        """中壢郵局 
存款機
桃園市中壢區中美路51號
中原大學郵局
存款機 
桃園市中壢區中北路200號
中壢普仁郵局
存款機 
桃園市中壢區中山東路2段24號
""",
        0,
        0,
        "https://epost.post.gov.tw/pstDigit/home.html",
        "一般金融卡",
        "中壢郵局 末五碼 45747"
    ),
    (
        "玉山",
        0,
        "https://www.esunbank.com/zh-tw/personal",
        """中壢分行
桃園市中壢區中山路126號
中原分行
桃園市中壢區中北路二段239號
""",
        3,
        3,
        "https://event.esunbank.com.tw/mkt/OpenAccount/marketing/index.html",
        "簽帳金融卡 末四碼 4836",
        "中壢分行 末五碼 76108"
    ),
    (
        "台新/Richart",
        3000,
        "https://richart.tw/TSDIB_RichartWeb/discount",
        """中壢分行
存款
桃園市中壢區延平路366號 
全家
""",
        5,
        5,
        "https://richart.tw/TSDIB_RichartWeb/card/debit-card",
        "綠狗卡 簽帳金融卡 末四碼 1902",
        "敦南分行 末五碼 57295"
    ),
    (
        "中國信託",
        1555,
        "https://www.ctbcbank.com/twrbo/zh_tw/index.html",
        """中壢分行
存款機
桃園市中壢區延平路500號1樓
中原分行
存款機 
桃園市中壢區中北路二段203號
統一超商
""",
        1,
        0,
        "https://www.ctbcbank.com/content/dam/minisite/long/atm/ATM/P2-1.html",
        "Line Pay 超萌熊大卡 簽帳金融卡 末四碼 6010",
        "營業部 末五碼 54064"
    ),
    (
        "聯邦銀行",
        -1,
        "https://www.ubot.com.tw/",
        """中壢分行 
存款機
桃園市中壢區中央西路一段62號 
北中壢分行
存款機 
桃園市中壢區元化路222號 
""",
        10,
        10,
        "https://newnewbank.com.tw/index.htm",
        "簽帳金融卡 末四碼 ????",
        "末五碼 ?????"
    ),
    (
        "華南",
        -1,
        "https://www.hncb.com.tw/wps/portal/HNCB/",
        """中壢分行 
存款
桃園市中壢區民族路35號
壢昌分行
存款
桃園市中壢區中正路175號
""",
        20,
        10,
        "https://www.hncb.com.tw/wps/portal/HNCB/msg/co-management/pb-best-offer/c1/t1/c4",
        "一般金融卡 末四碼",
        "末五碼 ?????"
    ),
    (
        "第一",
        -1,
        "https://www.firstbank.com.tw/sites/fcb/personalhome",
        """中壢分行
桃園市中壢區中正路146號1、2樓
西壢分行
桃園市中壢區中央西路2段30號
""",
        10,
        10,
        "https://card.firstbank.com.tw/sites/Satellite?c=CreditCard&cid=1565690699316&d=Touch&pagename=FirstBankCard%2FCreditCard%2Fzh%2FCreditCardDetailView#",
        "簽帳金融卡 末四碼 ????",
        "末五碼 ?????"
    ),
    (
        "合作金庫",
        -1,
        "https://www.tcb-bank.com.tw/personal-banking",
        """中壢分行
存款	
桃園市中壢區中山路180號
壢新分行
存款
桃園市中壢區中山路119號
中原分行
存款	
桃園市中壢區中北路二段392號
""",
        16,
        8,
        "https://actlink.tcb-bank.com.tw/digitalDeposit/index.html",
        "一般金融卡",
        "末五碼 ?????"
    ),
    (
        "台灣",
        -1,
        "https://www.bot.com.tw/tw/personal-banking",
        """中壢分行
桃園市中壢區延平路580號
建國分行
桃園市中壢區健行路169號
""",
        99,
        10,
        "https://event.bot.com.tw/digital-deposit/index",
        "一般金融卡",
        "末五碼 ?????"
    ),
]

for bank in banks:
    cur.execute("""
        INSERT OR IGNORE INTO bank
        (name, deposit, site, address, withdrawals, transfer, activity, card, account)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, bank)

conn.commit()
cur.close()
conn.close()
