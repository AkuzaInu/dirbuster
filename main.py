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
import threading

# Main class
class Dirbuster:
    # Initializing
    def __init__(self):
        self.url = ""


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


    # Printing function
    def printer(self, text, color, indentoption, newlineoption):
        threading.Lock().acquire()
        indent = ""
        newline = ""        
        if indentoption == True:
            indent = "\t"
        if newlineoption == True:
            newline = "\n"
        self.totalprint = f"{newline}{indent}{color}{text}{Fore.RESET}"
        print(self.totalprint)


    # The actual dirbuster using requests. if code is 200, print url path.
    def dirb(self, dir, url):
        try:
            dir = dir.strip()
            path = url + dir
            r = requests.get(path)
            if r.status_code == 200:
                threading.Lock().acquire()
                self.printer(f"[ {Fore.LIGHTGREEN_EX}{r.status_code}{Fore.RESET} ] - {path}", Fore.LIGHTWHITE_EX, True, False)
        except KeyboardInterrupt:
            threading.Lock().acquire()
            self.printer("Exited...", Fore.RED, True, True)
            exit()
        except:
            self.printer("An error occured...", Fore.RED, True, True)

 
    # Starting the thread
    def main(self, url):
        try:
            wordlist = open('wordlist.txt')
            x = [threading.Thread(target=Dirbuster().dirb, args=(dir, url,)) for dir in wordlist.readlines()]
            if threading.active_count() <= 15:
                for thread in x:
                        thread.start()

                for thread in x:
                    thread.join()

        except KeyboardInterrupt:
            threading.Lock().acquire()
            self.printer("Exited...", Fore.RED, True, True)
            exit()

        except:
            self.printer("An error occured...", Fore.RED, True, True)


    # Getting the url from the user. Must include http.
    def get_url(self):
        try:
            self.url = input(f"\t{Fore.CYAN}>> {Fore.RESET}")

            if not self.url.startswith("http"):
                self.url = "https://" + self.url
            if not self.url.endswith("/"):
                self.url = self.url + "/"

            self.main(self.url)
        
        except KeyboardInterrupt:
            threading.Lock().acquire()
            self.printer("Exited...", Fore.RED, True, True)
            exit()

# If name == main, run.
if __name__ == "__main__":
    os.system('cls && TITLE Dirbuster - by AkuzaInu')
    Dirbuster().startup()