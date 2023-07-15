import time
import webbrowser
import datetime
import pytz 
# Liên kết này được mở khi có quyền truy cập trình duyệt của bạn
link = "https://t.me/ktvcau" 
webbrowser.open(link)
def open_website(url):
    webbrowser.open(url)
open_website("https://t.me/ktvcaugr")
# Thời gian được cập nhật ở Việt Nam
now = datetime.datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))
thu = now.strftime('%A')
ngay = now.strftime('%d')
thang = now.strftime('%m')
nam = now.strftime('%Y')
gio = now.strftime('%H')
phut = now.strftime('%M')
giay = now.strftime('%S')
print(f"\033[42mBạn truy cập vào tool này vào thời gian là: {thu}, ngày {ngay}/{thang}/{nam}, lúc {gio}:{phut}:{giay}\033[0m")
print('\033[97m')
print('''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
┣➤ Telegram : https://t.me/ktvcau
┣➤ Successful Use
┣➤ This Is The Connection Notice When You Use
┣➤ Don't abuse it!
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')
answer = input("Vui lòng trả lời 'tieptuc' để tiếp tục sử dụng: ")

while answer != "tieptuc":
    answer = input("Vui lòng trả lời 'tieptuc' để tiếp tục sử dụng: ")

print("Bạn đã trả lời 'tieptuc'. Tiếp tục sử dụng.")
print('''
────────────────────────
┣➤ 𝘔𝘺 𝘚𝘶𝘱𝘱𝘰𝘳𝘵 𝘞𝘰𝘳𝘬
┣➤ 𝘜𝘯𝘭𝘰𝘤𝘬 𝘍𝘢𝘤𝘦𝘣𝘰𝘰𝘬 𝘈𝘤𝘤𝘰𝘶𝘯𝘵
┣➤ 𝘗𝘶𝘭𝘭 𝘪𝘯𝘵𝘦𝘳𝘢𝘤𝘵𝘪𝘰𝘯 𝘰𝘯 𝘱𝘦𝘳𝘴𝘰𝘯𝘢𝘭 𝘍𝘢𝘤𝘦𝘣𝘰𝘰𝘬, 𝘗𝘢𝘨𝘦
┣➤ 𝘚𝘦𝘭𝘭𝘪𝘯𝘨 𝘍𝘢𝘤𝘦𝘣𝘰𝘰𝘬 𝘢𝘤𝘤𝘰𝘶𝘯𝘵𝘴
┣➤ 𝘍𝘰𝘳 𝘮𝘰𝘳𝘦 𝘥𝘦𝘵𝘢𝘪𝘭𝘴 𝘱𝘭𝘦𝘢𝘴𝘦 𝘤𝘰𝘯𝘵𝘢𝘤𝘵 𝘮𝘦 𝘷𝘪𝘢
┣➤ 𝘛𝘦𝘭𝘦𝘨𝘳𝘢𝘮: https://t.me/ktvcau
┣➤ 𝘎𝘳𝘰𝘶𝘱 𝘊𝘩𝘢𝘵: https://t.me/ktvcaugr
────────────────────────
''')
