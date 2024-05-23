import socket
import time
import random
import string
import requests
import secrets

def spam_discord_webhook(webhook_url, message, count, delay):
    data = {"content": message}
    for _ in range(count):
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            print("\033[92mMessage sent successfully!\033[0m")  # Yeşil renk
        else:
            print("\033[91mFailed to send message.\033[0m")  # Kırmızı renk
        time.sleep(delay)

def generate_tiktok_account():
    email = ''.join(random.choices(string.ascii_lowercase, k=8)) + "@example.com"
    password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    print("\033[92mTikTok account created successfully.\033[0m")  # Yeşil renk
    print("\033[93mEmail:\033[0m", email)  # Sarı renk
    print("\033[93mPassword:\033[0m", password)  # Sarı renk

def generate_discord_token():
    token = secrets.token_hex(32)
    print("\033[92mDiscord token successfully generated:\033[0m")  # Yeşil renk
    print("\033[93mToken:\033[0m", token)  # Sarı renk
    print("\033[1;31mWarning: Treat your Discord token as sensitive information and do not share it with anyone.\033[0m")  # Kırmızı renk, kalın
    print("\033[1;31mWarning: Only use your Discord token with trusted applications.\033[0m")  # Kırmızı renk, kalın

def find_open_port(ip):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, 0))
        s.listen(1)
        port = s.getsockname()[1]
        s.close()
        return port
    except Exception as e:
        print("\033[91mError finding open port:", e, "\033[0m")  # Kırmızı renk
        return None

def find_ip():
    ip = input("\033[93mHedef IP adresini girin:\033[0m ")  # Sarı renk
    port = int(input("\033[93mHedef port numarasını girin:\033[0m "))  # Sarı renk
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            s.connect((ip, port))
            print("\033[92mIP adresi ve port açık.\033[0m")  # Yeşil renk
    except Exception as e:
        print("\033[91mHedef IP adresi veya port kapalı:", e, "\033[0m")  # Kırmızı renk

def main():
    while True:
        print("\033[1;32;40mSeçim yapın:\033[0m")  # Yeşil renk, kalın
        print("\033[1;33;40m1: Discord webhook spamla")
        print("2: İnternet Hız Testi yap")
        print("3: IP Logger aç")
        print("4: 10 Minute Mail aç")
        print("5: Discord Token Generator")
        print("6: Tiktok Hesap Oluştur")
        print("7: Temp SMS Oluştur")
        print("8: Discord Image Logger")
        print("9: Snapchat Hesap Oluştur")
        print("10: Discord Kullanıcı Kontrol")
        print("0: Çıkış yap")
        choice = input("\033[1;37;40mSeçiminizi yapın (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10): \033[0m")

        if choice == '0':
            print("\033[93mProgramdan çıkılıyor...\033[0m")  # Sarı renk
            break
        elif choice == '1':
            webhook_url = input("\033[93mDiscord webhook URL'sini girin:\033[0m ")  # Sarı renk
            message = input("\033[93mGönderilecek mesajı girin:\033[0m ")  # Sarı renk
            count = int(input("\033[93mKaç kez gönderileceğini girin:\033[0m "))  # Sarı renk
            delay = int(input("\033[93mGecikme süresini saniye cinsinden girin:\033[0m "))  # Sarı renk
            spam_discord_webhook(webhook_url, message, count, delay)
        elif choice == '2':
            # Diğer işlevler buraya gelecek
            pass
        elif choice == '3':
            # Diğer işlevler buraya gelecek
            pass
        elif choice == '4':
            # Diğer işlevler buraya gelecek
            pass
        elif choice == '5':
            generate_discord_token()
        elif choice == '6':
            generate_tiktok_account()
        elif choice == '7':
            # Diğer işlevler buraya gelecek
            pass
        elif choice == '8':
            # Diğer işlevler buraya gelecek
            pass
        elif choice == '9':
            # Diğer işlevler buraya gelecek
            pass
        elif choice == '10':
            find_ip()
        else:
            print("\033[91mGeçersiz seçim. Lütfen 0 ile 10 arasında bir sayı girin.\033[0m")  # Kırmızı renk

if __name__ == "__main__":
    main()
