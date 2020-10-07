from discord.ext import commands
import os
import traceback
import datetime
import pytz


bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def test(ctx):
    now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    await ctx.send('Niwa Bot は正常に稼働中！\nTime:['+now+']')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
