import base64
import os
import time

Banner = """
███████╗ ██████╗  █████╗ 
╚════██║██╔═████╗██╔══██╗
    ██╔╝██║██╔██║╚█████╔╝
   ██╔╝ ████╔╝██║██╔══██╗
   ██║  ╚██████╔╝╚█████╔╝
   ╚═╝   ╚═════╝  ╚════╝ 
"""




terminal_width = os.get_terminal_size().columns

banner_lines = Banner.splitlines()

centered_banner = ""
for line in banner_lines:
    spaces_needed = (terminal_width - len(line)) // 2
    centered_banner += " " * spaces_needed + line + "\n"


os.system("cls")
print("\033[36m" + centered_banner)
id = input("\033[36m" + "Enter User Id $> ")
encoded_id = base64.b64encode(id.encode('utf-8'))
print("First Part Of User Token $> ", (encoded_id.decode('utf-8')))
time.sleep(5)
os.system("exit")