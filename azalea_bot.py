import os
import discord
import random
import datetime

client = discord.Client(intents = discord.Intents().all())


@client.event
async def on_ready():
    cliccGeneral = await client.fetch_channel(915361057185357881)
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.author.id == 607020747650629633:
        await message.add_reaction("🌸")

    if message.author.id == 726150411475484713: 
        await message.add_reaction("🐉")

    if message.author.id == 538515351592370176:
        await message.add_reaction("🐐")

    if message.author.id == 610951370744266780:
        match random.randint(0,2):
            case 0:
                reaction = "<:bingchinglingly:1085044806683725865>"
            case 1:
                reaction = "<:bingchingchinglinglingly:1095712297567145985>"
            case 2:
                reaction = "<:bingchillingchinglingly:1102693790000623676>"
        await message.add_reaction(reaction)

    if "Azalea" in message.content:
         await message.channel.send("Bot")

    if "💀" in message.content:
        if random.randint(1, 3) == 1:
            await message.channel.send("Skull emoji.")

    if message.content.startswith("a."):

        if "sendFlower" in message.content:
            await message.channel.send(file=discord.File(r'C:\Users\idtec\OneDrive\Documents\coding\Pie Thon\Azalea Bot\azalea.jpeg'))

        elif "memberStats" in message.content:
            guild = await client.fetch_guild(message.guild.id, with_counts=True)
            await message.channel.send("Number of members: " + str(guild.approximate_member_count) + "\nNumber of active members: " + str(guild.approximate_presence_count))

        elif "messagesSent" in message.content:
            yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
            num = 0
            async for message in message.channel.history(limit=None, after=yesterday):
                num += 1
            await message.channel.send("Number of messages sent since yesterday in this channel: " + str(num))
        else:
            await message.channel.send("Sorry, I don't recognize that command.")

client.run("TOKEN")