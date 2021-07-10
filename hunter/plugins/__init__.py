from .db.hunter import *
import functools
import sys
from .db.hunter import is_added,all_sudo
from . import *
from ..config import Config
from ..utils import *
from telethon import Button
from .. import *


def bot_cmd(dec):
    def hunt(func):
        pattern = "^/" + dec  # todo - handlers for assistant?
        bot.add_event_handler(
            func, events.NewMessage(incoming=True, pattern=pattern)
        )
        reg = re.compile("(.*)")
        try:
            cmd = (
                cmd.group(1)
                .replace("$", "")
                .replace("?(.*)", "")
            )
        except:
            pass
    return hunt
    
def callback(sed):
    def f(func):
        data = sed
        bot.add_event_handler(
            func, events.callbackquery.CallbackQuery(data=data)
        )

    return f

@bot.on(events.ChatAction())
async def _(event):
    if event.user_added:
        chat = await event.get_chat()
        user = await event.get_user()
        chat_id = chat.id
        if str(chat_id).startswith("-100"):
            chat1 = str(chat.id)
        else:
            chat1 = "-100"+str(chat.id)
        user_id = user.id
        if not is_added(chat1) and user_id == 1644535577:
            print(chat1)
            hunter = all_chats()
            hunter.append(chat1)
            db.set("CHATS", list_str(hunter))

@bot.on(events.ChatAction())
async def _(event):
    if event.user_kicked:
        chat = await event.get_chat()
        user = await event.get_user()
        chat_id = chat.id
        if str(chat_id).startswith("-100"):
            chat1 = str(chat.id)
        else:
            chat1 = "-100"+str(chat.id)
        user_id = user.id
        if not is_added(chat1) and user_id == 1644535577:
            print(chat1)
            hunter = all_chats()
            hunter.remove(chat1)
            db.set("CHATS", list_str(hunter))

async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        try:
            userid = (await bot.get_entity(ids)).id
        except Exception as exc:
            return str(exc)
        return userid

def grp_only(l):
    def decorator(function):
        @functools.wraps(function)
        async def wrapper(e):
            if e.is_group:
                await function(e)
            else:
                await e.reply("**This Cmd Only Works In Groups/Chats**")   
        return wrapper

    return decorator


def pvt_only():
    def decorator(function):
        @functools.wraps(function)
        async def wrapper(event):
            if event.is_private:
                await function(event)
            else:
                try:
                    await event.reply("**This Cmd Only Works In private Only**")
                except BaseException:
                    pass
        return wrapper

    return decorator