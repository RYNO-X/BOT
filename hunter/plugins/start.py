from telethon.client import buttons
from . import *

@bot_cmd("start ?(.*)")
async def start(e):
    chat = await e.get_chat()
    chat_id = chat.id
    if chat_id not in all_chats():
        print(chat_id)
        hunter = all_chats()
        hunter.append(chat_id)
        db.set("CHATS", list_str(hunter))
    PIC = "http://telegra.ph/file/2878408d913ba97309431.jpg"
    uname = (await bot.get_me()).username
    if e.is_group:
        if str(e.sender_id) in all_sudo(): #  if in all_sudo()
            return await e.reply("**Hey, You Can Use Me To Make Keyboard Buttons**\n\n `Dm Me For Help`",
            buttons=[Button.url("Help", url=f"https://t.me/{uname}?start=set")]
            )
        else: # if not in all_sudo()
            return await e.reply("**Hey, You Dont Have Permisson to Use Me** xD\n\n `Dm For Permisson and help`")
    else: # not in group
        if str(e.sender_id) in all_sudo():
            return await bot.send_file(e.chat_id, file=PIC, caption="**Hey, You Can Use Me To Make Keyboard Buttons And Other Stuff**\n\n`Version` - 1.0.0\n\n`My Master Link Is Below`\n\nClick Help Button For More Info",
            buttons=[
                Button.url("Master", url="https://t.me/HUNTER_YUVRAJ"),
                Button.inline("Help", data="s1")])
        else:
            return await bot.send_file(e.chat_id, file=PIC, caption="**Hey You Can Use Me Dm My Master For Access**",
            buttons=[
                [
                Button.url("Master", url=f"https://t.me/HUNTER_YUVRAJ")
                ],
                [
                Button.inline("Help", data="s1")
                ]
            ]
            )

@callback("s1")
async def s1(e):
    await e.edit(
        "Join @TheTermite For More Info",
         buttons=[
             [
                 Button.inline("Add Keyboard", data="addk"),
                 Button.inline("Start Buttons", data="go")
             ],
             [
                 Button.inline("Remove Keyboard", data="removek"),
                 Button.inline("List Poles", data="listp")
             ],
             [
                 Button.inline("Add Sudo", data="adds"),
                 Button.inline("Remove Sudo", data="rems"),
                 Button.inline("List Sudo", data="lists")
             ],
             [
                Button.inline("Eval", data="eval"),
                Button.inline("Broadcast", data="bcast")
             ],
             [
                Button.inline("Translate", data="tr"),
                Button.inline("Get Id", data="id")
             ],
             [
                Button.inline("My Master", data="me")
             ],
             [
                Button.inline("Back", data="start")
             ],
         ]
         )

@callback("start")
async def start(e):
    await e.delete()
    PIC = "http://telegra.ph/file/2878408d913ba97309431.jpg"
    uname = (await bot.get_me()).username
    if e.is_group:
        if str(e.sender_id) in all_sudo(): #  if in all_sudo()
            return await e.reply("**Hey, You Can Use Me To Make Keyboard Buttons**\n\n `Dm Me For Help`",
            buttons=[Button.url("Help", url=f"https://t.me/{uname}?start=set")]
            )
        else: # if not in all_sudo()
            return await e.reply("**Hey, You Dont Have Permisson to Use Me** xD\n\n `Dm For Permisson and help`")
    else: # not in group
        if str(e.sender_id) in all_sudo():
            return await bot.send_file(e.chat_id, file=PIC, caption="**Hey, You Can Use Me To Make Keyboard Buttons And Other Stuff**\n\n`Version` - 1.0.0\n\n`My Master Link Is Below`\n\nClick Help Button For More Info",
            buttons=[
                Button.url("Master", url="https://t.me/HUNTER_YUVRAJ"),
                Button.inline("Help", data="s1")])
        else:
            return await bot.send_file(e.chat_id, file=PIC, caption="**Hey You Can Use Me Dm My Master For Access**",
            buttons=[
                [
                Button.url("Master", url=f"https://t.me/HUNTER_YUVRAJ")
                ],
                [
                Button.inline("Help", data="s1")
                ]
            ]
            )


@callback("addk")
async def _(e):
    msg = """
**Add Keyboard**

    Just The Cmd To Add Keyboard Button

          `/add <text>`
    """
    await e.edit(
        msg,
        buttons=[Button.inline("Back", data="s1")]
    )


@callback("go")
async def _(e):
    msg = """
**Start Button Keyboard**

    To Start Keyboard Spam

          `/go`
    """
    await e.edit(
        msg,
        buttons=[Button.inline("Back", data="s1")]
    )


@callback("removek")
async def _(e):
    msg = """
**Remove Keyboard**

    Clear The Buttons In The Chat

          `/remove`
    """
    await e.edit(
        msg,
        buttons=[Button.inline("Back", data="s1")]
    )


@callback("listp")
async def _(e):
    msg = """
**List Buttons Available**

    List All The Buttons

          `/listpoles`
    """
    await e.edit(
        msg,
        buttons=[Button.inline("Back", data="s1")]
    )


@callback("ads")
async def _(e):
    msg = """
**Add Sudo**

    Dev Cmd To Add Sudo Users

         `/newsudo <userid>`
    """
    await e.edit(
        msg,
        buttons=[Button.inline("Back", data="s1")]
    )


@callback("rems")
async def _(e):
    msg = """
**Remove Sudo**

    Dev Cmd To Remove Sudo Users

          `/delsudo <userid>`
    """
    await e.edit(
        msg,
        buttons=[Button.inline("Back", data="s1")]
    )


@callback("lists")
async def _(e):
    msg = """
**List SUDO Users**

    List Sudo Users

          `/listsudos`
    """
    await e.edit(
        msg,
        buttons=[Button.inline("Back", data="s1")]
    )


@callback("eval")
async def _(e):
    msg = """
**Eval**
    Dev Cmd To Run Pyton Code

          `/eval`
    """
    await e.edit(
        msg,
        buttons=[Button.inline("Back", data="s1")]
    )


@callback("bcast")
async def _(e):
    msg = """
**Broadcast**

    Send Message To Every Channel And Chat

          `/bcast`
    """
    await e.edit(
        msg,
        buttons=[Button.inline("Back", data="s1")]
    )


@callback("tr")
async def _(e):
    msg = """
**Translate**

    Translate The Given Text

        `/tr <lang code> <text>`
    """
    await e.edit(
        msg,
        buttons=[Button.inline("Back", data="s1")]
    )


@callback("id")
async def _(e):
    msg = """
**Id**

    Returns The Chat Id Or User Id

          `/id`
    """
    await e.edit(
        msg,
        buttons=[Button.inline("Back", data="s1")]
    )

@callback("me")
async def _(e):
    await e.edit(
        "My Master Here [HUNTER](https://t.me/HUNTER_YUVRAJ)",
        buttons=[Button.inline("Back", data="s1")]
        )