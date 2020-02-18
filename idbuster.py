import requests
import argparse
import random
import time
import sys
import os
from bs4 import BeautifulSoup

ERASE_LINE = '\033[2K\033[1G'

black = lambda text: '\033[0;30m' + text + '\033[0m'
red = lambda text: '\033[0;31m' + text + '\033[0m'
green = lambda text: '\033[0;32m' + text + '\033[0m'
yellow = lambda text: '\033[0;33m' + text + '\033[0m'
blue = lambda text: '\033[0;34m' + text + '\033[0m'
magenta = lambda text: '\033[0;35m' + text + '\033[0m'
cyan = lambda text: '\033[0;36m' + text + '\033[0m'
white = lambda text: '\033[0;37m' + text + '\033[0m'

colors = [red,white,blue,cyan,yellow,magenta,green]

def banner():
    banner = '''
.__    .______.                   __
|__| __| _/\\_ |__  __ __  _______/  |_  ___________
|  |/ __ |  | __ \\|  |  \\/  ___/\\   __\\/ __ \\_  __ \\
|  / /_/ |  | \\_\\ \\  |  /\\___ \\  |  | \\  ___/|  | \\/
|__\\____ |  |___  /____//____  > |__|  \___  >__|
        \\/      \\/           \\/            \\/

                by Mr.Debugger
'''
    value = random.choice(colors)
    print (value(banner))
    print ("")

def error(error):
	global banner
	os.system("clear")
	errormsg = '''
Usage: python idbuster.py -u https://site.com?page_id= -n 1000

options:

  -u,  --url   Input a valid url with a parameter
  -n,  --number Input a number range [like:1000]
        [This will Test all page ids from 1-1000]
'''
	banner()
	print (errormsg)
	sys.exit(0)

parser = argparse.ArgumentParser()
parser.error = error
parser._optionals.title = "options"
parser.add_argument('-u','--url', type=str,required=True, help='Input a valid url with a parameter: ')
parser.add_argument('-n','--number', type=int,required=False, help='Input a number range[1,1000]: ')
args = parser.parse_args()

requests.packages.urllib3.disable_warnings()

def main(url,number):
    for x in range(1,number):
        sys.stdout.write(ERASE_LINE)
        try:
            r = requests.get(url + str(x),headers={'User-Agent':'Mozilla/5.0'},timeout=5,verify=False)
            if r.status_code == 200:
                sys.stdout.write(ERASE_LINE)
                print (green("[+] " + white("Found Page --> " + url + str(x))))
            elif r.status_code == 302:
                time.sleep(0.1)
            else:
                sys.stdout.write(cyan("[-] " + white("Testing: %s " % str(x))))
                sys.stdout.flush()
        except requests.exceptions.ReadTimeout:
            time.sleep(0.1)
        except requests.exceptions.ConnectionError:
            time.sleep(0.1)

    sys.stdout.write(ERASE_LINE)
    print ("")

os.system("clear")
banner()
main(args.url,args.number)
