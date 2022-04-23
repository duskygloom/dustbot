import discord
import configuration as conf

token = conf.token
bot   = discord.Client()


@bot.event
async def on_ready():
    '''bot ready'''
    print("bot is ready ^-^")

@bot.event
async def on_message(message):
    '''on recieving a message'''
    print(f"{message.author} > {message.channel}: {message.content}")

    if message.author == bot.user:
        pass

    elif message.author.id == conf.myid and message.content == "close bot":
        print("you closed bot")
        await message.channel.send("bybye ;-;")
        await bot.close()

    else:
        await message.channel.send(f"hewo {message.author.name} °^°")


bot.run(token)