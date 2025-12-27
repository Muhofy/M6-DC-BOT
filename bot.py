import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # Hoşgeldin mesajı için
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Hoşgeldin Mesajı
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='hoşgeldin')
    if channel:
        await channel.send(f"{member.mention} Burada takılabilir, AI ile konuşanilir, Minecraft ve PUBG gibi oyunlar oynayabilirsin. 🎮  


Genel muhabbet → 💬│genel-sohbet  

Duyurular → 📢│duyurular

Video, Komiklik → 📷│medya

Yapay Zekayla Sohbet → 🧠│ yapay-zeka-sohbet

Minecraft ile alakalı yazıyla sohbet etmek → 🎮│minecraft-sohbet

Minecraft Sunucusuna katılmak ve bilgileri öğrenmek  → 🎮│minecraft-sunucu

Minecraft oynarken sesli konuşmak → 🗣️│Minecraft Ses

Sesli muhabbet etmek, konuşmak, tartışmak → 🗣️💬│Sohbet Ses

Sesli bir oda açmak → 🔒│Özel Oda Aç


Takıl, eğlen, oyna, tartış ne istersen 😏 😎")

# Basit AI Komutu (yalnızca örnek)
@bot.command()
async def merhaba(ctx):
    await ctx.send(f"Hey {ctx.author.name}, nasılsın? 😏")

bot.run('MTQ1NDM4Njk0NTAwMTAwMDk4Mg.Gc6lAM.0EvWxwCGc-7cN5HwPmMHzMqHkNIwpH144tqV-E')
