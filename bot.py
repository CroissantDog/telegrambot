#Imports
import sys
import urllib.request
import re
import os
import logging
from youtubesearchpython import VideosSearch
import pyshorteners
import TenGiphPy
from flask import Flask, request
import telegram
from telegram import MessageEntity
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
import random


#Logging config
logging.basicConfig(
    level=logging.INFO,
    format ="%(asctime)s - %(name)s - %(levelname)s - %(message)s, "
)
logger = logging.getLogger()



#Tenor Token
t = TenGiphPy.Tenor(token= os.environ.get('TTOKEN'))

#Telegram bot Token
bot_token = os.environ.get('BOTTOKEN')


#Updater & Dispatcher 
updater = Updater(token=bot_token, use_context = True)
dispatcher = updater.dispatcher



#Start command
def start(update, context):
    msg = "Hi traveler I'm Noelle. Nice to meet you! if you need help, use the /help command ^^"
    context.bot.sendMessage(chat_id=update.message.chat_id, text=msg)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

#Help command
def help(update, context):
    msg = "Noelle to the rescue!\n\
                               \n\
My commands are: \n\
                        \n\
Gifs: \n\
                            \n\
    /smile - Send a gif about smiling\n\
                            \n\
    /angry - Send a gif about getting mad\n\
    \n\
    /blush - Send a gif about blushing\n\
        \n\
    /bored - Send a gif about boring\n\
                            \n\
    /slap - Send a gif summoning '@' to hit someone\n\
                            \n\
    /hug - Send a gif summoning '@' to hug someone\n\
                            \n\
    /pats - Send a gif summoning '@' to pat someone\n\
                            \n\
    /kiss - Send a gif summoning '@' to kiss someone\n\
                            \n\
        \n\
Nuke Codes:\n\
    \n\
    /nukecodes - Type a number... Degenerate.\n\
        \n\
YouTube:\n\
                            \n\
    /yt - Type anything and I'll search it in YouTube\n\
        \n\
URL Shortener:\n\
    \n\
    /urlshort - Paste an URL and I'll short it for you\n\
        \n\
        \n\
If you want to give feedback, need more help or want to report a bug contact my Master on reddit: u/CroissantDog"

    image1 = " "'<a href="'+'https://lh5.googleusercontent.com/proxy/T4AkP3cn_Xe5YsPHSXZuOPbuucEsb8pm-P1Mm4BvR2U0eP50wwUJgMzlek6VAmbZzK1m-nQXzJnW-DMsLXMaSt0ib3ewz5TK0VyuD_HpImOWHiFIlLkHP5FpZajGsk5v2bY3IW-Uk5BQMqOLIvin7-yrRYWpRWDNyY5sU0xU93zfUSMdKw=w1200-h630-p-k-no-nu'+'">.</a>'
    context.bot.send_message(chat_id=update.message.chat_id, text = msg + image1, parse_mode = "HTML", disable_web_page_preview = "false")

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)



#Gifs commands
def smile(update, context):
    first_name = update.message.from_user.first_name
    context.bot.send_animation(chat_id=update.message.chat_id, animation = t.random("Anime Smile"), caption = "@{} is smiling".format(first_name))
smile_handler = CommandHandler('smile', smile)
dispatcher.add_handler(smile_handler)


def angry(update, context):
    first_name = update.message.from_user.first_name
    context.bot.send_animation(chat_id=update.message.chat_id, animation = t.random("Anime angry"), caption = "@{} is angry. What did you guys do now?".format(first_name))

angry_handler = CommandHandler('angry', angry)
dispatcher.add_handler(angry_handler)


def blush(update, context):
    first_name = update.message.from_user.first_name
    context.bot.send_animation(chat_id=update.message.chat_id, animation = t.random("Anime blush"), caption = "@{} is blushing, how cute".format(first_name))

blush_handler = CommandHandler('blush', blush)
dispatcher.add_handler(blush_handler)


def bored(update, context):
    first_name = update.message.from_user.first_name
    context.bot.send_animation(chat_id=update.message.chat_id, animation = t.random("Anime bored"), caption = "@{} is bored, let's do something interesting".format(first_name))

bored_handler = CommandHandler('bored', bored)
dispatcher.add_handler(bored_handler)


def slap(update, context):
    args = context.args
    text = str(args)
    msg = re.sub("[^A-Za-z0-9-@]","",text)
    first_name = update.message.from_user.first_name
    if len(args) > 0:
        context.bot.send_animation(chat_id=update.message.chat_id, animation = t.random("Anime slap"), caption = "@{} slaps {}".format(first_name, msg))
    else:
        context.bot.send_animation(chat_id=update.message.chat_id, animation = t.random("Anime slap"), caption = "@{} is... hitting himself?".format(first_name))

slap_handler = CommandHandler('slap', slap)
dispatcher.add_handler(slap_handler)


def hug(update, context):
    args = context.args
    text = str(args)
    msg = re.sub("[^A-Za-z0-9-@]","",text)
    first_name = update.message.from_user.first_name
    if len(args) > 0:
        context.bot.send_animation(chat_id=update.message.chat_id, animation = t.random("Anime hug"), caption = "@{} hugs {} uwu".format(first_name, msg))
    else:
        context.bot.send_animation(chat_id=update.message.chat_id, animation = t.random("Anime hug"), caption = "@{} hugs himself".format(first_name))

hug_handler = CommandHandler('hug', hug)
dispatcher.add_handler(hug_handler)


def pats(update, context):
    args = context.args
    text = str(args)
    msg = re.sub("[^A-Za-z0-9-@]","",text)
    first_name = update.message.from_user.first_name
    if len(args) > 0:
        context.bot.send_animation(chat_id=update.message.chat_id, animation = t.random("Anime pats"), caption = "@{} pats {}".format(first_name, msg))
    else:
        context.bot.send_animation(chat_id=update.message.chat_id, animation = t.random("Anime pats"), caption = "@{} wants for some pats".format(first_name))

pats_handler = CommandHandler('pats', pats)
dispatcher.add_handler(pats_handler)


def kiss(update, context):
    args = context.args
    text = str(args)
    msg = re.sub("[^A-Za-z0-9-@]","",text)
    first_name = update.message.from_user.first_name
    if len(args) > 0:
        context.bot.send_animation(chat_id=update.message.chat_id, animation = t.random("Anime kiss"), caption = "@{} kiss {}, they are so cute together".format(first_name, msg))
    else:
        context.bot.send_animation(chat_id=update.message.chat_id, animation = t.random("Anime kiss"), caption = "@{} wants to kiss someone".format(first_name))

kiss_handler = CommandHandler('kiss', kiss)
dispatcher.add_handler(kiss_handler)


def poke(update, context):
    args = context.args
    text = str(args)
    msg = re.sub("[^A-Za-z0-9-@]","",text)
    first_name = update.message.from_user.first_name
    if len(msg) > 0:
        context.bot.send_animation(chat_id=update.message.chat_id, animation = t.random("Anime poke"), caption = "@{} pokes {}".format(first_name, msg))
    else:
        context.bot.send_animation(chat_id=update.message.chat_id, animation = t.random("Anime poke"), caption = "@{} wants to bother".format(first_name))

poke_handler = CommandHandler('poke', poke)
dispatcher.add_handler(poke_handler)


#nuclearcodes commands
def nukecodes(update, context):
    #Command input
    args = context.args
    #Convert to str and clean non interesting stuff
    text = str(args)
    msg = re.sub("[^0-9]","",text)
    #Url vanilla
    ncurl = "https://nhentai.net/g/"
    #Full url
    completedurl = ncurl+msg
    #HTML to hide the URL and make a clickable text
    url = '<a href= "' + completedurl + '">You are a disappointment, Traveler</a>'
    
    context.bot.sendMessage(chat_id=update.message.chat_id, text = url, parse_mode = 'HTML', disable_web_page_preview = True)

nukecodes_handler = CommandHandler('nukecodes', nukecodes)
dispatcher.add_handler(nukecodes_handler)


#Youtube commands
def yt(update, context):
    #Command input
    text = update.message.text
    #Remove /song and spaces
    text = text.replace("/song","")
    text = text.replace(" ","")
    #Now search the song in YT
    search_keyword = text
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    #Completed URL
    url = "https://www.youtube.com/watch?v=" + video_ids[0]

    context.bot.sendMessage(chat_id=update.message.chat_id, text = url, parse_mode = 'HTML')

yt_handler = CommandHandler('yt', yt)
dispatcher.add_handler(yt_handler)



#URL Shortener
def urlshort(update,context):
    id = update.effective_user["id"]
    text = update.message.text
    text = text.replace("/urlshort","")
    text = text.replace(" ","")
    shortener = pyshorteners.Shortener()
    new_url = shortener.tinyurl.short(text)

    context.bot.sendMessage(chat_id = id, parse_mode = 'HTML', text = "Here are the new URL, enjoy: "+new_url, disable_web_page_preview = True)


dispatcher.add_handler(MessageHandler(Filters.entity(MessageEntity.URL) | Filters.entity(MessageEntity.TEXT_LINK),urlshort))

#URL Validation
def Validation (update,context):
    id = update.effective_user["id"]
    name = update.effective_user["first_name"]
    context.bot.sendMessage(chat_id=id, parse_mode = 'HTML', text = "{}, send me the URL".format(name))



dispatcher.add_handler(MessageHandler(Filters.text, Validation))

    

updater.start_polling()




