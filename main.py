import asyncio
from os import system
from colorama import Fore

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.headless = True
driver = webdriver.Chrome(options=chrome_options)

attempts=0
banner = '              zeeeeee-\n            z$$$$$$"\n           d$$$$$$"\n          d$$$$$P\n         d$$$$$P\n        $$$$$$"\n      .$$$$$$"\n     .$$$$$$"\n    4$$$$$$$$$$$$$"\n   z$$$$$$$$$$$$$"\n   """""""3$$$$$"\n         z$$$$P\n        d$$$$"\n      .$$$$$"\n     z$$$$$"\n    z$$$$P\n   d$$$$$$$$$$"\n  *******$$$"\n       .$$$"\n      .$$"\n     4$P"\n    z$"\n   zP\n  z"'

async def SentViews():
    global driver
    try: 
        driver.get("https://github.com/Ltooo4")
        system("title " + f"Attempts ~ {attempts}")
        print(f"{Fore.MAGENTA}[{Fore.BLUE}+{Fore.MAGENTA}] {Fore.GREEN}Sent{Fore.WHITE}")
    except Exception:
        system("title " + f"Attempts ~ {attempts}")
        #print(response.status)
        print(Fore.RED + 'Something Went Wrong!')


async def StartThreads(threads):
    tasks = []
    global attempts
    for _ in range(threads):
        attempts+= 1
        task = asyncio.ensure_future(SentViews())
        tasks.append(task)
    await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    print(f"\n\n{Fore.MAGENTA}{banner}{Fore.WHITE}\n\n\n\n")
    while True:
        asyncio.get_event_loop().run_until_complete(StartThreads(int(10)))
