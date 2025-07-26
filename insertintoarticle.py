import os
from dotenv import load_dotenv
import sqlitecloud

# 載入環境變數
load_dotenv()

# 建立連線
conn = sqlitecloud.connect(os.getenv("DATABASE_URL"))
cur = conn.cursor()

articles = [
    (
        "7月6日公務人員高考三級考試延期舉行",
        """引用來源:
https://wwwc.moex.gov.tw/main/news/wfrmNews.aspx?kind=3&menu_id=42&news_id=7518
引用內容:
114/07/05
114年公務人員高考三級考試設臺北、桃園、新竹、苗栗、臺中、彰化、雲林、嘉義、臺南、高雄、宜蘭、花蓮、臺東、澎湖、金門、馬祖16考區，原定7月6日至8日舉行，因受丹娜絲颱風影響，臺南市政府、高雄市政府等已宣布7月6日停止上班上課，依國家考試偶發事件處理辦法第12條第1項規定原則辦理，任一考區不能進行考試時，所有考區配合停止考試，爰經本考試典試委員長會同考選部決定，第1天考試（7月6日）延期舉行，延期後之考試日期，考選部將再發布公告。
考選部表示，後續考試相關事宜，考選部將會密切注意颱風動態，並視考區所在之行政區域是否停班停課，妥慎因應處理並發布訊息，請應考人密切注意考選部全球資訊網（https://www.moex.gov.tw）發布之最新消息。
考選部另說明，本次考試適逢颱風影響，請應考人關注天候動態及交通狀況，留意自身安全。應考人如因考試延期或交通因素致無法參加考試者，可依考選部各項考試規費退費作業要點規定，於考試後15日內申請退還報名費（申請窗口：高普考試司第一科連絡電話02-22369188分機3955、3958，試務信箱:moex3958@mail.moex.gov.tw）。
""",
        "2025-07-23 07:23:26",
        "https://fra.cloud.appwrite.io/v1/storage/buckets/6867c5280021205ba9c0/files/687fe17d00145748fcfc/view?project=680c76af0037a7d23e44&mode=admin",
        None, None,
        None, None,
        None, None,
        None, None
    ),
    (
        "受丹娜絲颱風持續影響 114年公務人員高考三級考試再度順延至7月8日至10日舉行",
        """引用來源:
https://wwwc.moex.gov.tw/main/news/wfrmNews.aspx?kind=3&menu_id=42&news_id=7520
引用內容:
114/07/06
考選部表示，依據中央氣象署最新颱風預報資料顯示，丹娜絲颱風暴風圈進入臺灣南部陸地，對臺灣各地及澎湖構成威脅，苗栗縣政府、臺中市政府、彰化縣政府、雲林縣政府等已宣布7月7日停止上班上課，依國家考試偶發事件處理辦法第12條第1項規定，任一考區不能進行考試時，所有考區配合停止考試，爰經本考試典試委員長會同考選部決定，114年公務人員高考三級考試再度順延至7月8日至10日舉行。
本考試設臺北、桃園、新竹、苗栗、臺中、彰化、雲林、嘉義、臺南、高雄、宜蘭、花蓮、臺東、澎湖、金門、馬祖16考區，原於7月6日至8日舉行，依序順延至7月8日至10日舉行。考選部提醒，除了高雄考區明誠中學應試地點調整為三民家商外，其餘試區應考人仍於原試場應試；考選部將持續留意天候動態並適時發布訊息公告，請應考人密切注意考選部全球資訊網（https://www.moex.gov.tw）最新消息，並關注交通動態，留意自身安全。
應考人如因考試延期或交通因素致全程無法參加考試者，可依考選部各項考試規費退費作業要點規定，於考試後15日內申請退還報名費（申請窗口：高普考試司第一科連絡電話02-22369188分機3955、3958，試務信箱: moex3958@mail.moex.gov.tw）。
""",
        "2025-07-24 07:24:26",
        "https://fra.cloud.appwrite.io/v1/storage/buckets/6867c5280021205ba9c0/files/686a5ee800352c80f246/view?project=680c76af0037a7d23e44&mode=admin",
        None, None,
        None, None,
        None, None,
        None, None
    ),
]

for article in articles:
    cur.execute("""
        INSERT OR IGNORE INTO article (
            title, content, newDate,
            url1, url2, url3,
            file1, file1type,
            file2, file2type,
            file3, file3type
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, article)

# 提交與關閉
conn.commit()
cur.close()
conn.close()
