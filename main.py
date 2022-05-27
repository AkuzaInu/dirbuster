# This is a python directory buster
# Enter a url and it will start searching for all (including hidden) directories

# THIS IS CREATED FOR EDUCATIONAL PURPOSES ONLY, USE THIS IN YOUR OWN ENVIRONMENT
# I AM NOT RESPONSIBLE FOR ANY KIND OF MIS-USE OF THIS PRODUCT
# MIS-USING THIS PRODUCT FOR UNLAWFUL ACTIVITIES IS ILLEGAL

# Imports
import time
import os
import requests
from colorama import Fore

# Main class
class Dirbuster:
    # Initializing
    def __init__(self):
        self.url = ''

    # Startup function, contains just plain text and a logo
    def startup(self):
        def logo():
            print(f"""{Fore.CYAN}\n\n
        ████│  █████│  ████│   ████│   █   █│  █████│  █████│  █████│  ████│
        █│  █│   █│    █│  █│  █│  █│  █   █│  █│        █│    █│      █│  █│
        █│  █│   █│    ████│   ████│   █   █│  █████│    █│    █████│  ████│
        █│  █│   █│    █│  █│  █│  █│  █   █│      █│    █│    █│      █│  █│
        ████│  █████│  █│  █│  ████│   █████│  █████│    █│    █████│  █│  █│            
            {Fore.RESET}""")

            slowtype(f"{Fore.BLUE}\tCreated by AkuzaInu{Fore.RESET}\n\n")

        def slowtype(txt):
            for x in txt:
                print(x,end="",flush=True)
                time.sleep(0.05)
    
        logo()
        self.get_url()

    # The actual dirbuster using requests. if code is 200, print url path.
    def dirb(self, url):
        try:
            wordlist = open('wordlist.txt', 'r')
            for dir in wordlist.readlines():
                dir = dir.strip()
                path = url + "/" + dir
                r = requests.get(path)
                if r.status_code == 200:
                    print(f"\t[ {Fore.LIGHTGREEN_EX}{r.status_code}{Fore.RESET} ] - {path}")
        except KeyboardInterrupt:
            print(f"\n\t{Fore.RED} Exited...{Fore.RESET}\n")
            exit()
        except:
            print(f"\n\t{Fore.RED}An error occured...{Fore.RESET}")    
    
    # Getting the url from the user. Must include http.
    def get_url(self):
        url = input(f"\t{Fore.CYAN}>> {Fore.RESET}")

        if "http" not in url:
            print(f"\n\t{Fore.RED}Please enter a valid url. \n\t{Fore.LIGHTRED_EX}(e.g.) https://example.com\n")
            self.get_url()
        
        self.dirb(url)

# If name == main, run.
if __name__ == "__main__":
    os.system('cls && TITLE Dirbuster - by AkuzaInu')
    Dirbuster().startup()