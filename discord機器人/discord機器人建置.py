import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='{')
@bot.event
async def on_ready():
    print(">> BOT is online <<")

bot.run("OTQxNjY5ODM5OTI2MzQ1NzQ4.YgZUYQ.0g6Kt6ZwLy6S9qQSTdwwkf13bkU")

