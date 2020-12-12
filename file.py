import discord
from discord.ext import commands
from discord import Webhook,AsyncWebhookAdapter
import re
from discord.ext.commands import MissingRequiredArgument
from discord.ext.commands import CommandInvokeError
from discord.ext.commands import MissingPermissions
from discord.ext.commands import has_permissions
from discord import Embed
import json
from datetime import datetime


client = commands.Bot(command_prefix = "!" case_insensitive=True,intents=default=True)

def global_check(ctx):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    return check

@client.command(help = "Starts the advertising prompt in your DMs")
@commands.cooldown(1, 14400, commands.BucketType.user)
async def advertise(ctx):
    try:
        author = ctx.message.author
        channel = client.get_channel(783714673425776701)
        checkdms = Embed(title = "Please check your DMs!",color=discord.Color.green())
        msgyes = await ctx.send(embed = checkdms)
        q1 = discord.Embed(title = "Company name?")
        msgyes = await author.send(embed = q1)
        waitmsg1 = await client.wait_for('message',check=global_dm_check(ctx.author,ctx.guild))
        name = waitmsg1.content
        q2 = discord.Embed(title = "Motto?",description = "Keep it nice and short. Ex. \"We sell quality products at quality prices\" instead of \"We are the best tech group on Roblox selling over twenty products with minimal prices.\"")
        msgyes = await author.send(embed = q2)
        waitmsg1 = await client.wait_for('message',check=global_dm_check(ctx.author,ctx.guild))
        motto = waitmsg1.content
        q3 = discord.Embed(title = "Invite or website?",description = "Choose **one**.\nNo Bit.ly/shortened links allowed please.")
        msgyes = await author.send(embed = q3)
        waitmsg1 = await client.wait_for('message',check=global_dm_check(ctx.author,ctx.guild))
        invite = waitmsg1.content
        q4 = discord.Embed(title = "Image LINK?",description = "Please send one **image link** for a product you've made. ***Don't send a file,*** send a Gyazo/Flyro link.")
        q4.set_footer(text = "Say skip to skip.")
        msgyes = await author.send(embed = q4)
        waitmsg1 = await client.wait_for('message',check=global_dm_check(ctx.author,ctx.guild))
        image = waitmsg1.content
        if image == "Skip" or image == "skip":
            image = None
        try:
            buildembed = discord.Embed(title = f"{name} **|| AD**",description=motto,timestamp=datetime.utcnow())
            buildembed.add_field(name = "Link:",value = invite)
            if image != None:
                buildembed.set_image(url = image)
            buildembed.set_footer(icon_url = ctx.author.avatar_url,text = f"Sent by {ctx.author}")
            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url('Webhook URL here', adapter=AsyncWebhookAdapter(session))
                await webhook.send(embed=buildembed, username=ctx.author.name,avatar_url=ctx.author.avatar_url)
            done = Embed(title = "All sent!",description = "Thanks for your patience throughout this process.",color=discord.Color.green())
            msgyes = await author.send(embed = done)
        except:
            error = Embed(title = "You sent a file, not an image URL.",description = "Please get a CDN link to a featured image. You're going to have to wait four hours before you try again.",color = discord.Color.red())
            msgyes = await author.send(embed = error)
    except discord.Forbidden:
        error = Embed(title = "I can't DM you!",color=discord.Color.red())
        msgyes = await ctx.send(Embed = error)
    
@advertise.error
async def advertise_error(ctx,error):
    if isinstance(error,commands.CommandOnCooldown):
        cooldown = Embed(title = "Slow down there friend",description = "Pilot, slow down there. You're still on cooldown! Please only use this command once every 4 hours.",color=discord.Color.orange())
        cooldown.set_thumbnail(url = "https://media.giphy.com/media/dJezVlwfVulTykjRQj/giphy.gif")
        msgyes = await ctx.send(embed = cooldown)
        
client.run("Token here")
