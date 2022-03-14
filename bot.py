# bot.py
import os
import datetime
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
ROLE_ID = os.getenv('ROLE_ID')
date = []
timer = []
teams = []
time_now = datetime.datetime.now()
time_now = int(time_now.strftime("%d"))
bot = commands.Bot(command_prefix='!')
@bot.command(name='set_scrim', help='Setting up a scrim. Uses parameters date, time, team.')
async def setter(ctx, day: int, timers: int, team):
    date.append(day)
    timer.append(timers)
    teams.append(team)
    await ctx.send('Scrim has been added to the list.')
@bot.command(name='scrims')
async def nine_nine(ctx):
    scrims_for_the_day = f'{ROLE_ID}'
    for i in range(len(date)):
        if time_now > date[i]:
            date.remove(date[i])
            timer.remove(timer[i])
            teams.remove(teams[i])
        else:
            scrims_for_the_day = scrims_for_the_day + '\n ' + str(date[i]) + ' ' + str(timer[i]) + ' ' + teams[i]
    if scrims_for_the_day == f'{ROLE_ID}':
        response = 'There are no scrims set for today.'
    else:
        response = scrims_for_the_day
    await ctx.send(response)
@bot.command(name='clear_scrim')
async def clear(ctx):
    date.clear()
    teams.clear()
    timer.clear()
    await ctx.send('The schedule has been cleared!')
bot.run(TOKEN)