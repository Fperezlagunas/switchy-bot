import discord
from discord.ext import commands
import os

my_secret = os.environ['Token']

client = commands.Bot(command_prefix = '$' )

@client.event
async def on_ready():
  print('bot listo')

@client.command(pass_context=True)
async def clear(ctx, amount=100):
  channel = ctx.message.channel
  messages = []
  async for message in client.logs_from(channel, limit=int(amount)):
   messages.append(message)
  await client.delete_messages(messages)

@client.command()
async def a(ctx):
  embed = discord.Embed(
    title = 'Title',
    description = 'bla',
    colour = discord.Colour.blue()
  )
  embed.add_field(name='field name',value='field Value', inline=False)

  await ctx.send(embed=embed)
  embed.set_footer
client.run(my_secret)