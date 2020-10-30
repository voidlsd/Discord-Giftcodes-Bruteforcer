# Project Name: Discord Giftcodes Bruteforcer
# Project Author: VoidLSD
# Project Reason: Since no one made one already, I've decided to create one.

import requests
import random
import os

os.system("clear")

chars = "abcdefghijklmnopq_rstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678"

intro = """
    ██████╗  ██████╗ ██████╗ 
    ██╔══██╗██╔════╝ ██╔══██╗
    ██║  ██║██║  ███╗██████╔╝
    ██║  ██║██║   ██║██╔══██╗
    ██████╔╝╚██████╔╝██████╔╝
    ╚═════╝  ╚═════╝ ╚═════╝ 
  Discord Giftcode Bruteforcer
       Created by VoidLSD
"""
print(intro)
threads = input("How many threads: ")
threads = threads*5
threads = int(threads)

for i in range(threads):
    code = ""

    for c in range(16):
        code += random.choice(chars)

    code = str(code)

    url = f"https://discord.com/api/v8/entitlements/gift-codes/{code}"
    rqt = requests.get(url)
    try:
        if rqt.status_code == 200:
            print("Bruted: "+code)
        if rqt.status_code == 404:
            print("Invalid: "+code)
        if rqt.status_code == 429:
            print("Rate limited.")
    except Exception:
        print("Cannot connect to Discord's API.")
