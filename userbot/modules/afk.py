from telethon import TelegramClient, events
from userbot import bot
import time
from userbot import COUNT_MSG, USERS, ISAFK, AFKREASON, LOGGER, LOGGER_GROUP


@bot.on(events.NewMessage(incoming=True))
async def mention_afk(e):
    global COUNT_MSG
    global USERS
    global ISAFK
    if e.message.mentioned and not (await e.get_sender()).bot:
        if ISAFK:
            if e.chat_id not in USERS:
                  await e.reply("Bitch dont pm")
                  USERS.update({e.chat_id:1})
                  COUNT_MSG=COUNT_MSG+1
            elif e.chat_id in USERS:
                 if USERS[e.chat_id] % 5 == 0:
                      await e.reply("You son of a bitch dont pm")
                      USERS[e.chat_id]=USERS[e.chat_id]+1
                      COUNT_MSG=COUNT_MSG+1
                 else:
                   USERS[e.chat_id]=USERS[e.chat_id]+1
                   COUNT_MSG=COUNT_MSG+1


@bot.on(events.NewMessage(incoming=True))
async def afk_on_pm(e):
    global ISAFK
    global USERS
    global COUNT_MSG
    if e.is_private  and not (await e.get_sender()).bot:
        if ISAFK:
            if e.chat_id not in USERS:
                  await e.reply("Bitch dont pm")
                  USERS.update({e.chat_id:1})
                  COUNT_MSG=COUNT_MSG+1
            elif   e.chat_id in USERS:
                   if USERS[e.chat_id] % 5 == 0:
                     await e.reply("You son of a bitch dont pm")
                     USERS[e.chat_id]=USERS[e.chat_id]+1
                     COUNT_MSG=COUNT_MSG+1
                   else:
                    USERS[e.chat_id]=USERS[e.chat_id]+1
                    COUNT_MSG=COUNT_MSG+1


@bot.on(events.NewMessage(outgoing=True,pattern='^.notafk$'))
@bot.on(events.MessageEdited(outgoing=True,pattern='^.notafk$'))
async def not_afk(e):
    if not e.text[0].isalpha():
        global ISAFK
        global COUNT_MSG
        global USERS
        global AFKREASON
        ISAFK=False
        await e.edit("Oke master has arrived")
        await e.respond("`You recieved "+str(COUNT_MSG)+" messages while you were away. Check log for more details. This auto-generated message shall be self destructed in 2 seconds.`")
        time.sleep(2)
        i=1
        async for message in bot.iter_messages(e.chat_id,from_user='me'):
            if i>1:
                break
            i=i+1
            await message.delete()
        if LOGGER:
            await bot.send_message(LOGGER_GROUP,"You\'ve recieved "+str(COUNT_MSG)+" messages from "+str(len(USERS))+" chats while you were away")
            for i in USERS:
                name = await bot.get_entity(i)
                name0 = str(name.first_name)
                await bot.send_message(LOGGER_GROUP,'['+ name0 +'](tg://user?id='+str(i)+')'+" sent you "+"`"+str(USERS[i])+" messages`")
        COUNT_MSG=0
        USERS={}
        AFKREASON="No Reason"


@bot.on(events.NewMessage(outgoing=True, pattern='^.iamafk'))
@bot.on(events.MessageEdited(outgoing=True, pattern='^.iamafk'))
async def set_afk(e):
    if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
            message=e.text
            string = str(message[8:])
            global ISAFK
            global AFKREASON
            ISAFK=True
            await e.edit("AFK AF!")
            if string!="":
                AFKREASON=string
            await bot.send_message(LOGGER_GROUP,"You went AFK!")
