import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True  # Required to detect new members joining

bot = commands.Bot(command_prefix="!", intents=intents)

WELCOME_CHANNEL_ID = 1490662368420692091

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} and ready!")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        await channel.send(f"hello {member.mention} welcome to unknown's fixed mods")

bot.run(os.environ["DISCORD_TOKEN"])
