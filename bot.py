import os
import json
import random
import discord
from discord.ext import commands

DATA_FILE = "balances.json"

def load_balances():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_balances():
    with open(DATA_FILE, "w") as f:
        json.dump(balances, f, indent=2)

balances = load_balances()

def get_balance(user_id):
    user_id = str(user_id)

    if user_id not in balances:
        balances[user_id] = 1000

    return balances[user_id]

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
    amount = get_balance(interaction.user.id)
    save_balances()

    await interaction.response.send_message(
        f"🪙 **{interaction.user.display_name}**, you have **{amount:,} YVX Coins!**"
    )


@bot.tree.command(name="daily", description="Claim 500 YVX Coins")
async def daily(interaction: discord.Interaction):
    user_id = str(interaction.user.id)

    amount = get_balance(user_id)
    balances[user_id] = amount + 500
    save_balances()

    await interaction.response.send_message(
        f"🎁 **{interaction.user.display_name}** received **500 YVX Coins!**\n"
        f"💰 New balance: **{balances[user_id]:,} YVX Coins**"
    )


@bot.tree.command(name="work", description="Work to earn YVX Coins")
async def work(interaction: discord.Interaction):
    user_id = str(interaction.user.id)

    reward = random.randint(150, 350)
    amount = get_balance(user_id)

    balances[user_id] = amount + reward
    save_balances()

    await interaction.response.send_message(
        f"💼 **{interaction.user.display_name}** earned **{reward:,} YVX Coins!**\n"
        f"💰 New balance: **{balances[user_id]:,} YVX Coins**"
    )


@bot.tree.command(name="hunt", description="Go hunting for YVX Coins")
async def hunt(interaction: discord.Interaction):
    user_id = str(interaction.user.id)

    reward = random.randint(100, 500)
    amount = get_balance(user_id)

    balances[user_id] = amount + reward
    save_balances()

    await interaction.response.send_message(
        f"🏹 **{interaction.user.display_name}** went hunting and found "
        f"**{reward:,} YVX Coins!**\n"
        f"💰 New balance: **{balances[user_id]:,} YVX Coins**"
    )


bot.run(os.getenv("DISCORD_TOKEN"))
