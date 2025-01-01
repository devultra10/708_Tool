import os 
import sys
sys.stdout.reconfigure(encoding='utf-8')

Banner = """
███████╗ ██████╗  █████╗ 
╚════██║██╔═████╗██╔══██╗
    ██╔╝██║██╔██║╚█████╔╝
   ██╔╝ ████╔╝██║██╔══██╗
   ██║  ╚██████╔╝╚█████╔╝
   ╚═╝   ╚═════╝  ╚════╝ 
"""

info = """
[INFO] Made By @d3v_nozz
[WARNING] Inspired Of Redtiger (i didn't stealed any function, i made all function, in the next update i will give credit cuz it will use redtiger function)
"""

terminal_width = os.get_terminal_size().columns

banner_lines = Banner.splitlines()
info_lines = info.splitlines()

centered_banner = ""

for line in banner_lines:
    spaces_needed = (terminal_width - len(line)) // 2
    centered_banner += " " * spaces_needed + line + "\n"

for line in info_lines:
    spaces_needed = (terminal_width - len(line)) // 2
    centered_banner += " " * spaces_needed + line + "\n"

os.system("cls" if os.name == "nt" else "clear")
print("\033[36m" + centered_banner + "\033[0m")
os.system("pause")