from telethon.tl.custom import button
from . import *

text = []

@bot_cmd("add ?(.*)")
async def add(e):
    if not e.is_group:
        return
    if str(e.sender_id) in all_sudo():
        try:
            hunter = e.pattern_match.group(1)
            text.append(hunter)
            await e.reply("**Done**\nNow You Can Add More Button Or Start By /go")
        except Exception as x:
            await e.reply(f"Error {str(x)}")
    else:
        await e.reply("**Go Away**")

@bot_cmd("go")
async def rem(event):
    if not event.is_group:
        return
    if str(event.sender_id) in all_sudo():
        if len(text) == 1:
            await bot.send_message(event.chat_id, "**Enjoy**", buttons=[Button.text(text[0], resize=False)])
        if len(text) == 2:
            await bot.send_message(event.chat_id, "**Enjoy**", buttons=[
                [Button.text(text[0], resize=False)],
                [Button.text(text[1], resize=False)]
                ]
            )
        if len(text) == 3:
            await bot.send_message(event.chat_id, "**Enjoy**", buttons=[
                [Button.text(text[0], resize=False)],
                [Button.text(text[1], resize=False)],
                [Button.text(text[2], resize=False)]
                ]
            )
        if len(text) == 4:
            await bot.send_message(event.chat_id, "**Enjoy**", buttons=[
                [Button.text(text[0], resize=False)],
                [Button.text(text[1], resize=False)],
                [Button.text(text[2], resize=False)],
                [Button.text(text[3], resize=False)]
                ]
            )
        if len(text) == 5:
            await bot.send_message(event.chat_id, "**Enjoy**", buttons=[
                [Button.text(text[0], resize=False)],
                [Button.text(text[1], resize=False)],
                [Button.text(text[2], resize=False)],
                [Button.text(text[3], resize=False)], 
                [Button.text(text[4], resize=False)]
                ]
            )
        if len(text) == 6:
            await bot.send_message(event.chat_id, "**Enjoy**", buttons=[
                [Button.text(text[0], resize=False)], 
                [Button.text(text[1], resize=False)], 
                [Button.text(text[2], resize=False)], 
                [Button.text(text[3], resize=False)], 
                [Button.text(text[4], resize=False)], 
                [Button.text(text[5], resize=False)]
                ]
            )
        if len(text) == 7:
            await bot.send_message(event.chat_id, "**Enjoy**", buttons=[
            [Button.text(text[0], resize=False)], 
            [Button.text(text[1], resize=False)], 
            [Button.text(text[2], resize=False)], 
            [Button.text(text[3], resize=False)], 
            [Button.text(text[4], resize=False)], 
            [Button.text(text[5], resize=False)], 
            [Button.text(text[6], resize=False)]
            ]
        )
        if len(text) == 8:
            await bot.send_message(event.chat_id, "**Enjoy**", buttons=[[Button.text(text[0], resize=False)], 
            [Button.text(text[1], resize=False)], 
            [Button.text(text[2], resize=False)], 
            [Button.text(text[3], resize=False)], 
            [Button.text(text[4], resize=False)], 
            [Button.text(text[5], resize=False)], 
            [Button.text(text[6], resize=False)], 
            [Button.text(text[7], resize=False)]
            ]
        )
        if len(text) == 9:
            await bot.send_message(event.chat_id, "**Enjoy**", buttons=[
            [Button.text(text[0], resize=False)], 
            [Button.text(text[1], resize=False)], 
            [Button.text(text[2], resize=False)], 
            [Button.text(text[3], resize=False)], 
            [Button.text(text[4], resize=False)], 
            [Button.text(text[5], resize=False)], 
            [Button.text(text[6], resize=False)], 
            [Button.text(text[8], resize=False)]
            ]
        )
        if len(text) == 10:
            await bot.send_message(event.chat_id, "**Enjoy**", buttons=[
            [Button.text(text[0], resize=False)], 
            [Button.text(text[1], resize=False)], 
            [Button.text(text[2], resize=False)], 
            [Button.text(text[3], resize=False)], 
            [Button.text(text[4], resize=False)], 
            [Button.text(text[5], resize=False)], 
            [Button.text(text[6], resize=False)], 
            [Button.text(text[8], resize=False)], 
            [Button.text(text[9], resize=False)]
            ]
            )
        if len(text) > 10:
            await event.reply("Cant Add More Then 10 Buttons")
            await bot.send_message(event.chat_id, "**Enjoy**", buttons=[
            [Button.text(text[0], resize=False)], 
            [Button.text(text[1], resize=False)], 
            [Button.text(text[2], resize=False)], 
            [Button.text(text[3], resize=False)], 
            [Button.text(text[4], resize=False)], 
            [Button.text(text[5], resize=False)], 
            [Button.text(text[6], resize=False)], 
            [Button.text(text[8], resize=False)], 
            [Button.text(text[9], resize=False)]
            ]
            )

    else:
        await event.reply("**Go Away**")


@bot_cmd("remove")
async def rem(event):
    if not event.is_group:
        return
    if str(event.sender_id) in all_sudo():
        text.clear()
        await bot.send_message(event.chat_id, "**Thnq For Using Me**", buttons=Button.clear())
    else:
        await event.reply("**Go Away**")


@bot_cmd("listpoles")
async def rem(event):
    if not event.is_group:
        return
    if str(event.sender_id) in all_sudo():
        for x in text:
            a = f"{x}\n"
        await event.reply(a)
    else:
        await event.reply("**Go Away**")


