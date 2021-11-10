import os
import time
import webbrowser
import sys
import pyfiglet
import colorama
from colorama import Fore , Back , Style
colorama.init(autoreset = True)

def logo(self):
	print(f'''{Fore.GREEN}
          ▄▀█ █▀▀ █▀▀ █▀▀ █▀█ █░█ █▄░█ ▀█▀
          █▀█ █▄▄ █▄▄ █▄▄ █▄█ █▄█ █░▀█ ░█░

             █▀▄ █▀▀ █░░ █▀▀ ▀█▀ █▀▀ █▀█
             █▄▀ ██▄ █▄▄ ██▄ ░█░ ██▄ █▀▄''')
	
def first(self):
	os.system('clear')
	logo('y')
	print(" ")
	print(f"           {Fore.GREEN} ::~:: {Fore.WHITE} CREATED BY HACODE  {Fore.GREEN}::~::")
	print(f"         {Fore.GREEN}::~:: {Fore.WHITE}github.com/united-hackers {Fore.GREEN}::~::")
	print(f''' {Fore.GREEN}
		      [{Fore.RED}1{Fore.GREEN}]---START
		      [{Fore.RED}2{Fore.GREEN}]---UPDATE
		      [{Fore.RED}3{Fore.GREEN}]---ABOUT
		      [{Fore.RED}4{Fore.GREEN}]---MORE
		      [{Fore.RED}5{Fore.GREEN}]---FOLLOW
		      [{Fore.RED}6{Fore.GREEN}]---VIDEO
		      [{Fore.RED}7{Fore.GREEN}]---CHAT NOW
		      [{Fore.RED}8{Fore.GREEN}]---RESTART
		      [{Fore.RED}9{Fore.GREEN}]---EXIT ''')
						
						
	c = " "
	while(c != 9):
		print("")
		c = int(input(f'{Fore.GREEN}SELECT OPTION: {Fore.RED}'))
		if c == 1:
			second('t')
		elif c == 2:
			print("")
			print(f"{Fore.YELLOW}This Tool Updating Very Soon")
			print(f"{Fore.YELLOW}keep wait")
			print("")
		elif c == 3:
			os.system('clear')
			print('''
							
							
░█████╗░██████╗░░█████╗░██╗░░░██╗████████╗
██╔══██╗██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝
███████║██████╦╝██║░░██║██║░░░██║░░░██║░░░
██╔══██║██╔══██╗██║░░██║██║░░░██║░░░██║░░░
██║░░██║██████╦╝╚█████╔╝╚██████╔╝░░░██║░░░
╚═╝░░╚═╝╚═════╝░░╚════╝░░╚═════╝░░░░╚═╝░░░          
                     
THIS TOOLS IS ONLY FOR EDUCATIONAL PURPOSE SO'
IM NOT RESPONSIBLE IF YOU DO ANY ILLEGAL THINGS'
THANKS FOR READING SUBSCRIBE {HACODE}'
HAVE A GOOD DAY BUDDIE :)
''')
			
		elif c == 4:
			print(f"{Fore.YELLOW}Comming More Surprices for you")
		elif c == 5:
			webbrowser.open("https://www.instagram.com/hacode_88/")
		elif c == 6:
			webbrowser.open("https://youtube.com/channel/UCi00gqBm4n98-dg7ND7gsrg")
		elif c == 7:
			webbrowser.open("https://chat.whatsapp.com/JnrKsQW55tFAvq3iTgO2Ut")
		elif c == 8:
			first("kriss")
		elif c  == 9:
			exit()
	


def second(self):
	os.system('clear')
	logo('y')
	print(f'''


{Fore.YELLOW}[{Fore.RED}1{Fore.YELLOW}]---Google    {Fore.YELLOW}[{Fore.RED}6{Fore.YELLOW}]---Amazon
{Fore.YELLOW}[{Fore.RED}2{Fore.YELLOW}]---Gmail     {Fore.YELLOW}[{Fore.RED}7{Fore.YELLOW}]---Twitter
{Fore.YELLOW}[{Fore.RED}3{Fore.YELLOW}]---Facebook  {Fore.YELLOW}[{Fore.RED}8{Fore.YELLOW}]---Instagram
{Fore.YELLOW}[{Fore.RED}4{Fore.YELLOW}]---Telegram  {Fore.YELLOW}[{Fore.RED}9{Fore.YELLOW}]---Mesenger
{Fore.YELLOW}[{Fore.RED}5{Fore.YELLOW}]---Whatsapp  {Fore.YELLOW}[{Fore.RED}10{Fore.YELLOW}]---YouTube
''')
	d = " "
	while True:
		d = int(input(f'{Fore.GREEN}SELECT OPTION: {Fore.RED}'))
		if d == 1:
			webbrowser.open("https://youtu.be/P-SLC6-2RRI")
		elif d == 2:
			webbrowser.open("https://youtu.be/P4aZo90kxJM")
		elif d == 3:
			webbrowser.open("https://youtu.be/fcZJGwfvCVs")
		elif d == 4:
			webbrowser.open("https://youtu.be/MHAtxUB1a-8")
		elif d == 5:
			webbrowser.open("https://youtu.be/CH0dERa4NSA")
		elif d == 6:
			webbrowser.open("https://youtu.be/GuM49m7ko34")
		elif d == 7:
			webbrowser.open("https://youtu.be/mltwxdmcntY")
		elif d == 8:
			webbrowser.open("https://youtu.be/RLXDJ_wXlLo")
		elif d == 9:
			webbrowser.open("https://youtu.be/DTh3b8j4OXI")
		elif d == 10:
			webbrowser.open("https://youtu.be/6S_P3ulvqEY")
			
		

if __name__ == '__main__':
	first('y')
	