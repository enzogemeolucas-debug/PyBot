import discord, time, random, asyncio
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Bot iniciado!")

@bot.command()
async def oi(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(0.5)

    await ctx.send(f'Oi, {ctx.author.mention}!')

@bot.command()
async def tchau(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(0.5)

    await ctx.send('Tchau! \U0001f642')

@bot.command()
async def hora(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(1)

    await ctx.send(f'São {time.strftime("%H:%M")}')

@bot.command()
async def farme_aura(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(3)
    await ctx.send('676767676767676767676767676767 ATIVANDO MODO AURAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA 6767676767676767 (musica de farmar aura)')

@bot.command()
async def ping(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(0.5)
    await ctx.send('Pong\U0001F3D3')

@bot.command()
async def cara_ou_coroa(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(1)
    if random.randint(1, 2) == 1:
        await ctx.send("Cara! \U0001F642")
    else:
        await ctx.send("Coroa! \U0001F451")

@bot.command()
async def kaboom(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(0.5)
    for i in range(10, 0, -1):
        await ctx.send(f"**00:{i:02d}**\U0001F4A3")
        await asyncio.sleep(0.5)
    await ctx.send(f"KABOOM!\U0001F4A5")

@bot.command()
async def dance(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(2)
    gif_url = random.choice(
        ["https://klipy.com/gifs/pikuniku-dance-2", "https://klipy.com/gifs/hatsune-miku-kasane-teto-10",
         "https://klipy.com/gifs/dance-burnice", "https://klipy.com/gifs/griddy-miku",
         "https://klipy.com/gifs/hatsune-miku-mesmerizer-3",
         "https://klipy.com/gifs/default-dance-fortnite-4"])

    await ctx.send(gif_url)

@bot.command()
async def ajuda(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(4)

    await ctx.send(f"""
            :information_source: AJUDA DO BOT :information_source::\n
    !oi: Oi!
    !tchau: Tchau! \U0001f642
    !hora: São *hora atual*
    !farme_aura: (descubra kkkk)
    !ping: Pong!\U0001F3D3
    !cara_ou_coroa: lanca uma moeda e diz se da cara ou coroa
    !kaboom: conta de 10 a 0 e faz kaboom
    !dance: faz o PyBot dançar""")

bot.run("SEU_TOKEN_LEGAL")
