import discord
from discord.ext import commands

client = commands.Bot(command_prefix="-")

@client.event
async def on_ready():
    print("Bot is ready!")


@client.command
async def Hello(ctx):
    await ctx.send("Hi")


client.run("BOT TOKEN")


