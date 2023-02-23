import requests
from colorama import init, Back, Style, Fore
import random
import threading
import os
import datetime
from timeit import default_timer as timer, time
now = datetime.datetime.now()
start = timer()

os.system('cls & title Bio Changer')
t = now.strftime("%H:%M:%S")
with open("tokens.txt", 'r') as fp:
    lines = len(fp.readlines())
print("starting with {} tokens".format(lines))
time.sleep(1)

try:
    tokens = []
    with open('tokens.txt', 'r') as f:
        for i in f:
            if i.count(":") == 2:
                i = i.split(":")[2]
            tokens.append(i.strip())
    tokens = list(set(tokens))
except:
    print([t],"No tokens.txt file found! Please create the file and try again.", Fore.RED)

def get_dcf_sdc(cookie):
    sep = cookie.split(";")
    sx = sep[0]
    sx2 = sx.split("=")
    dcf = sx2[1]

    split = sep[6]
    split2 = split.split(",")
    split3 = split2[1]
    split4 = split3.split("=")
    sdc = split4[1]

    return dcf, sdc

def headerpow(tokens):
    cookie = requests.get("https://discord.com/register").headers['set-cookie']
    dcf, sdc = get_dcf_sdc(cookie)
    return {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.263 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
        "Referer": "https://discord.com/register",
        "Authorization": tokens,
        "X-Super-Properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkZpcmVmb3giLCJkZXZpY2UiOiIiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMC4xNDsgcnY6ODguMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC84OC4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiODguMCIsIm9zX3ZlcnNpb24iOiIxMC4xNCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5MTczNCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
        "X-Fingerprint": '873691818078920745.AdL-Gi4qePqVs4lEO8acceJAgxc',
        "Cookie": f"__dcfduid={dcf}; __sdcfduid={sdc}; OptanonConsent=isIABGlobal=false&datestamp=Mon+Aug+09+2021+04%3A31%3A04+GMT%2B0300+(Arabian+Standard+Time)&version=6.17.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2Floggin&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; _gcl_au=1.1.62729347.1628472664; _ga=GA1.2.1942394829.1628472665; _gid=GA1.2.2001024037.1628472665",
        "DNT": "1",
        "Connection": "keep-alive"
    }

def change(tokens):
    
    for token in tokens:
        Bio = open('Bio.txt', 'r').readlines()
        Bio = random.choice(Bio)


        header = headerpow(token)

        json_data = {
        'bio': Bio,
        }
        response = requests.patch('https://discord.com/api/v9/users/@me/profile', headers=header, json=json_data)
        if response.status_code == 200:
            print(f"{Fore.BLUE}Changed bio to >  " +  json_data['bio'])
            print(f"{Fore.BLUE}Token > " + token)
        if response.status_code == 401:
            print(f"{Fore.RED}Failed to change bio due to invalid token >  " + token)
change(tokens)
print("pow helped :) me still learning")
end = timer()
while True:
    if threading.active_count() < 13: #number off threads
        threading.Thread(
            target = headerpow,
            args = [
                tokens
            ]
        ).start()
    print(f"{Fore.LIGHTCYAN_EX}finished in", end - start)
    exit()