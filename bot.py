import discord
from discord.ext import commands
import random
import math

client = commands.Bot(command_prefix=".")



@client.event
async def on_ready():
    print('Ready')
    await client.change_presence(activity = discord.Game("use .gen to begin!"))



@client.command(name="gen")
async def VoiceChannel(ctx):
    VoiceChannel = ctx.author.voice.channel
    members = VoiceChannel.members

    mems = [ ]
    for member in members:
        mems.append(member.name)
          
    team1_size = 0
    team2_size = 0
    if len(mems) % 2 == 0:
      # even number of members in the channel
      team1_size = len(mems)/2
      team2_size = len(mems)/2
    else:
      # odd number of members
      x = random.choice([1,2])
      if x == 0:
        team1_size = math.ceil(len(mems)/2)
        team2_size = math.floor(len(mems)/2)
      else:
        team2_size = math.ceil(len(mems)/2)
        team1_size = math.floor(len(mems)/2)

    random.shuffle(mems)

    i = 0
    team1 = [ ]
    while team1_size > 0:
      team1.append(mems[i])
      mems.remove(mems[i])
      team1_size -= 1
      i += 1

    sep = " \n"
    team1f = sep.join(team1)
    memsf = sep.join(mems)
      
    await ctx.send (f">>> **Team 1:**\n{team1f}\n\n**Team 2:**\n{memsf}")
  
    
    
        
client.run('NzAzODMxMDE3MDQ3MzI2NzIw.XqgHxA.UbFajkj6Ib82oHyDlkrAUwy4TjE')
