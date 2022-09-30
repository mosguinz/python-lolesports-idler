import os
import time
import datetime

TARGET_TIME = "1400"
URL = "https://lolesports.com/live/lpl"

def now():
    return datetime.datetime.now().strftime("%H%M")

def open_link():
    os.system(f"open \"\" {URL}")


print(f"Waiting till {TARGET_TIME}. Refreshing every 10 seconds...")
print(f"Link: {URL}")

while now() <= TARGET_TIME:
    time.sleep(10)
        
open_link()
print(f"It is now {now()}. Opening {URL}")

input("Link didn't open? Press Enter to try again, or Ctrl+C to cancel.")
open_link()
