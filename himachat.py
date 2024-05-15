import requests
import random 
import time 
message = input("メッセージ:")
session = input("セッション:")
roomid = input("部屋id:")
uid = input("useid:")
cookie = input("cookie:")
delay = input("送信間隔:")
url = "https://himachat.jp/gomitame.php?mode=monku"

def set_information_and_send():
    headers = {
      "Accept": "*/*",
      "Accept-Encoding": "gzip, deflate, br, zstd",
      "Accept-Language": "ja,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
      "Content-Type": "application/x-www-form-urlencoded",
      "Cookie": cookie,
      "Origin": "https://himachat.jp",
      "Referer": "bing.com",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
      "X-Requested-With": "XMLHttpRequest"
    }
    payload = {
        "roomid":roomid,
        "marumie":uid,
        "mysession":session,
        "waruguti":message
    }
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
          print("サーバーには送信できました。反映できてるかはわかりません。")
while True:
    set_information_and_send()
    time.sleep(float(delay))

    
    
