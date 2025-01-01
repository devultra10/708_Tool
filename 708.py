import sys
import os
import time
import base64
from time import sleep
import asyncio
import discord
from discord.ext import commands
import subprocess
sys.stdout.reconfigure(encoding='utf-8')
os.system("title 708 Tool [v0.5]")
Banner = """
███████╗ ██████╗  █████╗ 
╚════██║██╔═████╗██╔══██╗
    ██╔╝██║██╔██║╚█████╔╝
   ██╔╝ ████╔╝██║██╔══██╗
   ██║  ╚██████╔╝╚█████╔╝
   ╚═╝   ╚═════╝  ╚════╝ 
"""

Interface = """
[1] Info | [2] Id to token | [3] Raid 
"""

username = os.getlogin()

prompt = f"\033[30m\033[34m@{username}\033[0m \033[30m\033[36m$> "

terminal_width = os.get_terminal_size().columns

banner_lines = Banner.splitlines()
interface_lines = Interface.splitlines()

centered_banner = ""
for line in banner_lines:
    spaces_needed = (terminal_width - len(line)) // 2
    centered_banner += " " * spaces_needed + line + "\n"

for line in interface_lines:
    spaces_needed = (terminal_width - len(line)) // 2
    centered_banner += " " * spaces_needed + line + "\n"

os.system("cls")
print("\033[36m" + centered_banner + "\033[0m")
inp = input(prompt)

if inp == "2":
    subprocess.run(["python", "Functions/idtotoken.py"]) 


if inp == "3":
    subprocess.run(["python", "Functions/raid.py"]) 


os.system("pause")
