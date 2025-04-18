import discord
from discord.ext import commands
import os
import random


image_links = [
    "https://i.imgur.com/03StPAn.jpeg",
    "https://i.imgur.com/LbWj6fN.jpeg",
    "https://i.imgur.com/oEnxxeG.jpeg",
    "https://i.imgur.com/DHrDDYd.jpeg",
    "https://i.imgur.com/Vd3zIj9.jpeg",
    "https://i.imgur.com/CkSvT7h.jpeg",
    "https://i.imgur.com/6dts1LY.jpeg",
    "https://i.imgur.com/mj26iQB.jpeg",
    "https://i.imgur.com/QISFGoH.jpeg",
    "https://i.imgur.com/KRfLmE7.gif",
    "https://i.imgur.com/zpcaGb8.jpeg",
    "https://i.imgur.com/VqoSwVz.jpeg",
    "https://i.imgur.com/L6cRPGF.jpeg",
    "https://i.imgur.com/DTmyXXD.jpeg",
    "https://i.imgur.com/XN1B2xO.jpeg",
    "https://i.imgur.com/iMhLX6U.jpeg",
    "https://i.imgur.com/WS7Sc2v.jpeg",
    "https://i.imgur.com/ghi789.jpg"
]
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="", intents=intents, case_insensitive=True)


#  dire bonjour et envoyer une image
@bot.command()
async def papa(ctx):
    # Envoi du message
    await ctx.send(
        "Bonjour Rienne la méchante mineure, Ton papa est là ! Le bot va te montrer une image aléatoire par ton papa"
    )

    image_url = "https://imgur.com/rFySWuO"  

    await ctx.send(image_url)


# Commande bb 
@bot.command()
async def bb(ctx):
    await ctx.send(
        "Salut BB ! Voici une autre image pour toi, Reste gentille chaton !")

    image_url = "https://imgur.com/a/nkRuowP"  

    await ctx.send(image_url)


# Commande miaw 
@bot.command()
async def miaw(ctx):

    await ctx.send("Miaw Miaw Miaw !")
    image_url = "https://imgur.com/gallery/were-fostering-kitties-EdHhfzh#/t/cats"
    await ctx.send(image_url)



# Commande chat
@bot.command()
async def chat(ctx):
    await ctx.send("Chaton !")
    image_url = random.choice(image_links)
    await ctx.send(image_url)


# Récupère le token depuis les variables d'environnement
token = os.environ.get('My_Token')

if token is None:
    print(
        "Erreur : le token du bot n'est pas défini dans les variables d'environnement."
    )
else:
    
    bot.run(token)
