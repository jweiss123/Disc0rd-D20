import discord
import os
import random
from discord.ext import commands
from keep_alive import keep_alive

keep_alive()

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name} ({bot.user.id})')


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  if message.content.startswith('hello'):
    await message.channel.send(
      f'Hello, {message.author.mention}! Care to roll some dice?')

  await bot.process_commands(message)


@bot.slash_command(name='d20', description='Rolls a twenty-sided die')
async def d20(ctx):
  rolled_num = random.randint(1, 20)
  if rolled_num == 1:
    await ctx.send(f':game_die: You rolled a {rolled_num}... :cry:')
  else:
    await ctx.send(f':game_die: You rolled a {rolled_num}!')


@bot.slash_command(name='d6', description='Rolls a six-sided die')
async def d6(ctx):
  rolled_num = random.randint(1, 6)
  if rolled_num == 1:
    await ctx.send(f':game_die: You rolled a {rolled_num}... :cry:')
  else:
    await ctx.send(f':game_die: You rolled a {rolled_num}!')


#discord bot token obscured with replit tool "Secrets"
bot_token = os.environ['bot token']
bot.run(bot_token)
