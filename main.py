import discord
import os
import random
from discord.ext import commands, tasks
from keep_alive import keep_alive

version = discord.__version__
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
  print(
    f'Logged in as {bot.user.name} ({bot.user.id}), Discord version: {version}'
  )
  myFunction.start()


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  if message.content.startswith('hello'):
    await message.channel.send(
      f'Hello, {message.author.mention}! Care to roll some dice?')

  await bot.process_commands(message)


@bot.command(name='d20', description='Rolls a twenty-sided die')
async def d20(ctx):
  rolled_num = random.randint(1, 20)
  if rolled_num == 1:
    await ctx.send(f':game_die: You rolled a {rolled_num}... :cry:')
  else:
    await ctx.send(f':game_die: You rolled a {rolled_num}!')


@bot.command(name='d12', description='Rolls a twelve-sided die')
async def d12(ctx):
  rolled_num = random.randint(1, 12)
  if rolled_num == 1:
    await ctx.send(f':game_die: You rolled a {rolled_num}... :cry:')
  else:
    await ctx.send(f':game_die: You rolled a {rolled_num}!')


@bot.command(name='d10', description='Rolls a ten-sided die')
async def d10(ctx):
  rolled_num = random.randint(1, 10)
  if rolled_num == 1:
    await ctx.send(f':game_die: You rolled a {rolled_num}... :cry:')
  else:
    await ctx.send(f':game_die: You rolled a {rolled_num}!')


@bot.command(name='d8', description='Rolls an eight-sided die')
async def d8(ctx):
  rolled_num = random.randint(1, 8)
  if rolled_num == 1:
    await ctx.send(f':game_die: You rolled a {rolled_num}... :cry:')
  else:
    await ctx.send(f':game_die: You rolled a {rolled_num}!')


@bot.command(name='d6', description='Rolls a six-sided die')
async def d6(ctx):
  rolled_num = random.randint(1, 6)
  if rolled_num == 1:
    await ctx.send(f':game_die: You rolled a {rolled_num}... :cry:')
  else:
    await ctx.send(f':game_die: You rolled a {rolled_num}!')


@bot.command(name='d4', description='Rolls a four-sided die')
async def d4(ctx):
  rolled_num = random.randint(1, 4)
  if rolled_num == 1:
    await ctx.send(f':game_die: You rolled a {rolled_num}... :cry:')
  else:
    await ctx.send(f':game_die: You rolled a {rolled_num}!')


@bot.command(name='d100', description='Rolls a hundred-sided die')
async def d100(ctx):
  rolled_num = random.randint(1, 100)
  if rolled_num == 1:
    await ctx.send(f':game_die: You rolled a {rolled_num}... :cry:')
  else:
    await ctx.send(f':game_die: You rolled a {rolled_num}!')

@tasks.loop(minutes=1)
async def myFunction():
  print('Bot is still running...')

  
#run uptimerobot server
keep_alive()

#discord bot token obscured with replit tool "Secrets"
bot_token = os.environ['bot token']
bot.run(bot_token)
