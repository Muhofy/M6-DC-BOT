import os
import discord
from discord.ext import commands

# ===== KANAL İSİMLERİ (SUNUCUDA BİREBİR AYNI OLMALI) =====
WELCOME_CHANNEL_NAME = "hoşgeldin"
AI_CHANNEL_NAME = "yapay-zeka-sohbet"

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot aktif: {bot.user}")


# ===== HOŞGELDİN MESAJI =====
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(
        member.guild.text_channels, name=WELCOME_CHANNEL_NAME
    )
    if channel:
        await channel.send(
            f"{member.mention}\n\n"
            "Burada takılabilir, AI ile konuşabilir, Minecraft ve PUBG gibi oyunlar oynayabilirsin 🎮\n\n"
            "💬 Genel muhabbet → 💬│genel-sohbet\n"
            "📢 Duyurular → 📢│duyurular\n"
            "📷 Video, komiklik → 📷│medya\n\n"
            "🧠 Yapay zekayla sohbet → 🧠│yapay-zeka-sohbet\n\n"
            "🎮 Minecraft sohbet → 🎮│minecraft-sohbet\n"
            "🌍 Minecraft sunucu bilgileri → 🎮│minecraft-sunucu\n\n"
            "🗣️ Minecraft ses → 🗣️│Minecraft Ses\n"
            "🗣️💬 Genel sesli sohbet → 🗣️💬│Sohbet Ses\n\n"
            "🔒 Özel sesli oda açmak → 🔒│Özel Oda Aç\n\n"
            "Takıl, eğlen, oyna, tartış — ne istersen 😎"
        )


# ===== AI KANALI (KOMUTSUZ CEVAP) =====
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.name == AI_CHANNEL_NAME:
        await message.channel.send(
            "🤖 Buradayım. Yaz gitsin."
        )

    await bot.process_commands(message)


# ===== BOTU BAŞLAT =====
bot.run(os.getenv("DISCORD_TOKEN"))