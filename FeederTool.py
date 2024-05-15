print('\033[34m'+"""
╔════════════════════════════════════════════════════════════════════════════╗
║╔══════════════════════════════════════════════════════════════════════════╗║
║║                              KotetsuFeeder                               ║║
║╚══════════════════════════════════════════════════════════════════════════╝║
║╔══════════════════════════════════════════════════════════════════════════╗║
║║                                                                          ║║
║║  GitHub: https://github.com/kotetsu499                                   ║║
║║                                                                          ║║
║║  Features:                                                               ║║
║║      1. spammer                                                          ║║
║║      2. change_status                                                    ║║
║║      3. create_room                                                      ║║
║║      4. N/A                                                              ║║
║║                                                                          ║║
║║                          Discord: kotetsu152                             ║║
║║                                                                          ║║
║╚══════════════════════════════════════════════════════════════════════════╝║
╚════════════════════════════════════════════════════════════════════════════╝

"""+'\033[0m')
import random
import requests
import time
session = requests.session()
response = session.get("https://www1.x-feeder.info/")
cookies = response.cookies
print("短い間に何回もリクエスト送信すると、一時的な制限がかけられます。")

select = input("select:")


if select == "1":
  print("このプログラムは荒らしのために作られたわけではありません。～分おきにアナウンスをするなどの目的で使用してください。")
  url = input("URL:")
  cookies = input("cookie:")
  url = url + "post_feed.php"
  name = input("名前: ")
  comment = input("コメント: ")
  is_special = 0
  category_id = 0
  spam = input("連投対策を有効にするか(y か n):")
  delay = input("何秒おきに送信するか:")

  
  headers = {
      "Accept": "text/plain, */*; q=0.01",
      "Accept-Encoding": "gzip, deflate, br, zstd",
      "Accept-Language": "ja,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
      "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
      "Cookie": cookies,
      "Origin": "https://www2.x-feeder.info",
      "Referer": url,
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
      "X-Requested-With": "XMLHttpRequest"
  }


  def send_request():
      payload = {
          "name": name,
          "comment": comment,
          "is_special": is_special,
          "category_id": category_id
      }
      if spam == "y":
          payload = {
              "name": name,
              "comment": comment + str(random.randint(1,1000000)),
              "is_special": is_special,
              "category_id": category_id
          }
      
      response = requests.post(url, headers=headers, data=payload)
      if response.status_code == 200:
          print("サーバーには送信できました。反映できてるかはわかりません。")

  while True:
      send_request()
      time.sleep(float(delay))  
      
      
      
      
  
if select == "2":
    print("ステータスをランダムで生成する場合はkotetsu152と入力")
    status = input("ステータス:")
    url = input("URL:")
    cookies = input("cookie:")
    url = url + "update_status.php"
    count = input("何秒おきに変更するか:")
    def change_status():  
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "ja,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": cookies,
            "Origin": "https://www2.x-feeder.info",
            "Referer": url,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",#ユーザーエージェント(端末情報)です。おそらく私のpcのです。
            "X-Requested-With": "XMLHttpRequest"
        }
        payload = {
            "is_mobile": 0,
            "status": 0,
            "status_text": status,
            "now_broadcasting": 0
        }
        if status == "kotetsu152":
          payload = {
            "is_mobile": 1,
            "status": 1,
            "status_text": str(random.randint(1,1000000)),
            "now_broadcasting": 1
          }
      
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200:
          print("サーバーには送信できました。反映できてるかはわかりません。")
    while True:
        change_status()
        time.sleep(float(count))
  
if select == "3":
    print("(部屋の複数作成はなかなか厳しく規制されているので、間隔を長くすることをお勧めします。)")
    print("idは、「kotetsu152」と入力して自動入力")
    url = "https://www.x-feeder.info/create_room.php"
    cookies = input("cookie:")
    template_id = input("テンプレートid(分からなければ0):")
    room_pass = input("管理用パスワード:")
    email = input("email:")
    rooms = input("何個作るか:")
    id = input("部屋のid:")
    delay = input("部屋を作成する間隔(秒)")
    idlol = 0
    def create_room():
        global id
        global i
        global idlol
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "ja,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": cookies,
            "Origin": "https://www2.x-feeder.info",
            "Referer": url,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",#ユーザーエージェント(端末情報)です。おそらく私のpcのです。
            "X-Requested-With": "XMLHttpRequest"
        }
        payload = {
            "public_or_private": "public",
            "template_id": template_id,
            "password_for_settings": room_pass,
            "password_for_settings_re": room_pass,
            "email": email,
            "numbering_policy": "auto",
            "feeder_id": id
        }
        if id == "kotetsu152":
            idlol = str(random.randint(1,1000000))
            print(idlol)
            payload = {
            "public_or_private": "public",
            "template_id": template_id,
            "password_for_settings": room_pass,
            "password_for_settings_re": room_pass,
            "email": email,
            "numbering_policy": "custom",
            "feeder_id": idlol
            }

            
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200:
            print("サーバーには送信できました。反映できてるかはわかりません。")
            
    for i in range(int(rooms)):
        print(idlol)
        print(id)
        create_room()
        time.sleep(float(delay))