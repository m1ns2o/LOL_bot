import discord
import random
from discord.ext import commands

app = commands.Bot(command_prefix='!')


ls = ()

def roll(l):
    data = list(l)
    random.shuffle(data)
    # print(data[0:len(data) // 2])
    # print(data[len(data) // 2:])
    # await ctx.send(data)
    t1 = ' '.join(data[0:len(data) // 2])
    t2 = ' '.join(data[len(data) // 2:])
    embed = discord.Embed(title='Team', color=0xAAB9FF)
    embed.add_field(name='1팀', value=t1, inline=True)
    embed.add_field(name='2팀', value=t2, inline=True)
    return embed


@app.event
async def on_ready():
    print(app.user.name)
    await app.change_presence(status=discord.Status.online, activity=None)


@app.command()
async def h(ctx):
    await ctx.send('help')

@app.command()
async def team(ctx, *l):
    global ls
    ls = l
    await ctx.send(embed=roll(l))

@app.command()
async def reroll(ctx):
    await ctx.send(embed=roll(ls))

app.run('토큰')