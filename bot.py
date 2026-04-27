import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

WELCOME_CHANNEL_ID = 1490662368420692091

@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Game(name="unknown's fixed mods froyo https://discord.gg/mXYkrMHVxP")
    )

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel is None:
        channel = await bot.fetch_channel(WELCOME_CHANNEL_ID)
    member_count = member.guild.member_count
    await channel.send(f"welcome to UFM broyo {member.mention} you are member number {member_count}")

bot.run(os.environ["DISCORD_TOKEN"])
