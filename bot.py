import discord, time, random, asyncio
from discord.ext import commands

intents = discord.Intents.all()

intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

python_logo = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢠⢠⢢⢢⢲⢱⢱⢱⢕⢵⢱⢕⢕⢖⢴⢰⡠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢜⢜⢜⢜⢜⢼⢸⢜⡪⡣⡣⡳⡱⡣⣫⢺⡸⡱⣕⢵⡱⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡪⡪⡪⠊⠀⠀⠀⢣⢣⡣⡳⡹⣸⢱⢝⢜⢎⢮⡣⣳⢱⢵⡱⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢎⢎⢮⠀⠀⠀⠀⡸⡸⡸⡪⣣⢣⡳⡕⣝⢕⡇⣗⢵⡹⡜⡮⣪⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡕⡵⡱⡹⡰⡔⣕⢵⢹⢜⢕⡕⣇⢧⢫⡪⣣⢳⢕⢧⢳⡹⡪⡮⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠎⠎⠮⠪⠣⠣⠣⠇⠗⠕⠧⠳⡱⡕⡧⡫⣎⢧⢳⢝⢮⡪⣏⢞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡀⡀⡄⡠⡀⡄⡠⣀⢄⢄⢄⢄⢄⢄⢄⢄⢄⢄⢄⢇⢯⡪⣳⢱⢳⡹⡪⣇⢗⡵⣫⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡠⡪⡪⡪⡣⡣⣣⢳⢹⢸⡸⡜⡜⡎⡞⣜⢕⢇⢯⡪⣣⡳⡝⣎⢞⢼⡱⣳⢹⡺⣜⢵⢝⢮⠀⠀⠂⠁⡈⠠⠈⠠⠐⠀⠀⠀⠀
⠀⢀⢎⢎⢎⢮⢪⢎⢮⢪⢪⡪⡎⣎⢮⢪⢳⢹⡸⡪⡳⡱⡝⡼⣸⢪⢎⡗⡧⡫⣎⢧⡳⡵⡝⡮⡳⠀⠀⠂⠁⡀⠐⠈⡀⠐⢈⠠⠀⠀
⠀⡪⡪⡪⡪⣪⢪⡪⡪⡪⡣⣣⢣⢇⢗⢝⡜⣕⢵⢹⢪⡳⡹⡪⣎⢗⣕⢗⡝⡞⣎⢗⢵⢳⢝⢮⡫⠀⠀⠂⠁⡀⠌⢀⠐⠈⡀⠄⠠⠀
⢨⢪⢪⡪⡣⡣⡣⡣⡫⣪⢣⡣⡳⡱⡝⣜⢎⢞⣜⢕⢧⢳⡹⡕⡧⡳⡕⣗⢝⢞⣎⢯⢳⢝⢵⢳⠍⠀⠠⠈⠠⢀⠐⠀⠄⢁⠠⠐⢀⠂
⡢⡳⡱⡱⡱⡹⡸⡱⡹⡸⡜⣜⢵⢹⢜⢎⢮⣓⢎⢗⡝⡮⡺⣪⢳⡹⣚⣎⢏⡧⣳⡹⣪⡫⡳⠃⠀⢀⠐⠈⠠⠀⠂⡁⢈⠠⠀⠌⠀⠄
⡣⡣⣣⢫⢪⢣⡫⣪⢣⡫⡪⣎⢞⡜⣎⠗⠕⠑⠙⠑⠑⠙⠊⠊⠓⠙⠊⠊⠓⠙⠘⠊⠁⠁⠀⢀⠠⠀⠂⡁⠄⢁⠂⠐⡀⢐⠈⠠⠁⠂
⡝⣜⢜⡜⣕⢵⢱⢕⢵⢹⢜⢎⢮⠚⠀⠀⡀⠄⠠⠀⠠⠀⡀⠄⢀⠀⡀⠄⢀⠠⠀⠠⠀⢂⠈⡀⠄⡈⠄⡀⠂⠄⠂⡁⢐⠀⠌⠠⠁⡁
⢪⢪⡪⣪⢪⢎⢞⡜⣎⢧⢳⡹⠈⠀⢀⠐⠀⡀⠂⢈⠠⠐⠀⠠⠀⠄⠠⠐⠀⠠⠈⠠⠈⠠⠀⠄⠂⠠⠐⠀⠌⡀⠡⠀⡂⠄⠡⠈⠄⠂
⠨⡪⡪⡎⡞⣜⢕⢵⡱⡕⣇⠇⠀⠠⠀⠄⠁⡀⢈⠀⡀⠄⢈⠀⢂⠈⡀⠂⠁⠄⢁⠂⠁⠄⠡⠀⠅⠂⡁⠌⠠⠐⠈⠄⢐⠠⠁⠌⠠⠁
⠀⢣⢫⡪⣺⢸⡱⣣⢳⡹⡸⡅⠀⠐⠀⠂⠁⡀⠄⠠⠀⡐⠀⡐⠀⠄⠐⢈⠠⠈⠠⢀⠡⠈⠠⠁⠄⡁⠄⠂⡁⠌⠠⠁⡂⠄⠡⢈⠐⠀
⠀⠈⢪⢺⡸⡱⣕⢕⡇⡯⣚⠆⠀⢀⠁⠄⠁⡀⠄⠂⠐⢀⠐⢀⠈⠄⠁⠄⠐⢈⠀⡂⠠⠈⠄⡁⠂⠄⠂⡁⠄⠨⠀⠅⡐⢈⠐⠠⠀⠀
⠀⠀⠀⠑⠵⡹⡜⣕⢝⢮⣪⡃⠀⢀⠐⢀⠁⠠⠀⠌⠐⢀⠐⡀⠂⡈⠐⢈⠐⡀⢂⠐⢈⠠⠁⡐⠈⠄⠡⠐⠈⠄⠅⢂⢐⠠⠈⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠠⠐⠀⠄⢁⠐⢀⠡⠀⢂⠀⡂⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢀⠁⡐⢀⠐⠠⠐⠈⠠⠐⠀⠌⡀⠂⡂⠨⠐⢈⠠⠁⠌⠄⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⠠⢀⠐⢀⠈⠄⠨⢀⠡⠠⠁⡂⠄⠡⠐⡀⠅⠐⠀⠡⠈⠄⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠐⢀⠐⠠⢈⠠⠁⠄⠂⠄⠡⠀⡂⢁⠂⠄⠀⠀⠀⠀⢁⠡⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⠀⠌⠐⡀⡐⢈⠠⠁⠌⠠⢁⠐⡀⢂⠂⡀⠀⠀⡀⠂⠄⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠌⡀⠂⠄⠂⠄⠡⢈⠐⡀⢂⠂⢂⠐⠠⢁⠡⠠⠁⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠀⠅⠨⠀⠂⠂⠂⠨⠠⠈⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
@bot.event
async def on_ready():
    print("Bot iniciado!")
    print("Intent members:", bot.intents.members)


@bot.command()
async def oi(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(0.5)

    await ctx.send(f'Oi, {ctx.author.mention}!')

async def on_member_join(member):
    canal = bot.get_channel(1564739726643298497)
    await canal.send(f"Bem-Vindo {member.mention}!")

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
async def rolar_dado(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(0.5)

    await ctx.send('Rolando dado...')
    await asyncio.sleep(0.7)

    async with ctx.channel.typing():
        await asyncio.sleep(2.5)

    await ctx.send(f"O número sorteado foi o número {random.randint(1, 6)}\U0001F3B2")

@bot.command()
async def averiguar_resenha(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(0.7)

    imagem = 'C:\\Users\\enzog\\Downloads\\resenha.png'
    resenha_encontrada = 'C:\\Users\\enzog\\Downloads\\resenha_encontrada.png'

    await ctx.send(file=discord.File(imagem))

    chance = random.random()

    await asyncio.sleep(10)
    async with ctx.channel.typing():
        await asyncio.sleep(1)
    if chance < 0.90:
        await ctx.send("Nenhuma resenha averiguada")
    else:
        await ctx.send("RESENHA ENCONTRADA\U0001F6A8\U0001F6A8\U0001F6A8\U0001F6A8\U0001F6A8\U0001F440\U0001F440\U0001F440\U0001F440")
        await asyncio.sleep(1)
        await ctx.send(file=discord.File(resenha_encontrada))

@bot.command()
async def python_ascii(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(5)

    await ctx.send(python_logo)

@bot.command()
async def fibonacci(ctx, n: int = 0):
    numeros = []
    async with ctx.channel.typing():
        await asyncio.sleep(5)
    a, b = 0, 1
    while a <= n:
        numeros.append(str(a))
        a, b = b, a+b
    await ctx.send(f'```{" - ".join(numeros)}```')

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
    !dance: faz o PyBot dançar
    !rolar_dado: rola um dado comum
    !averiguar_resenha: \U00000022averiguando possível resenha...\U00000022
    !python_ascii: manda uma arte em ascii com a logo do python
    !fibonacci **n**: faz a sequencia de fibonacci (n é o numero, exemplo: \U00000022!fibonacci 8\U00000022)""")

bot.run("Wow, quase 200 linhas OoO")
