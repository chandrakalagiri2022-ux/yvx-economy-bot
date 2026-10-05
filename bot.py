import os
import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"YVX Economy is online as {bot.user}")


@bot.tree.command(name="balance", description="Check your YVX Coins balance")
async def balance(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"🪙 **{interaction.user.display_name}**, you have **1,000 YVX Coins**!"
    )


@bot.tree.command(name="daily", description="Claim your daily YVX Coins")
async def daily(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"🎁 **{interaction.user.display_name}** received **500 YVX Coins**!"
    )


@bot.tree.command(name="work", description="Work to earn YVX Coins")
async def work(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"💼 **{interaction.user.display_name}** earned **250 YVX Coins**!"
    )


@bot.tree.command(name="hunt", description="Go hunting for rewards")
async def hunt(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"🐾 **{interaction.user.display_name}** went hunting and found **300 YVX Coins**!"
    )


bot.run(os.getenv("DISCORD_TOKEN"))
