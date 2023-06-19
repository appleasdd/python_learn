import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='{',intents = intents)
@bot.event
async def on_ready():
    print(">> BOT is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(941670949764345869)
    await channel.send(f"{member}join!")
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(941670949764345869)
    await channel.send(f"{member}leave!")


bot.run("OTQxNjY5ODM5OTI2MzQ1NzQ4.YgZUYQ.0g6Kt6ZwLy6S9qQSTdwwkf13bkU")

