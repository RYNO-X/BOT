from . import *
from .db.hunter import *


@bot_cmd("newsudo ?(.*)")
async def _(event):
    if str(event.sender_id) in all_sudo():
        inputs = event.pattern_match.group(1)
        if not str(event.sender_id) == XXX:
            return await event.reply("**Sudo users can't add new sudos!**")
        ok = await event.reply("**Updating SUDO Users List ...**")
        mmm = ""
        if inputs:
            if is_sudo(id):
                mmm += f"**{inputs} is already a SUDO User...**"
            else:
                add_sudo(inputs)
                mmm += f"**Added ****{inputs}**** as SUDO User**"
        else:
            mmm += "**add it's id/username.**"
        await ok.edit(mmm)
    else:
        await event.reply("**Go Away**")

@bot_cmd("delsudo ?(.*)")
async def _(event):
    if str(event.sender_id) in all_sudo():
        inputs = event.pattern_match.group(1)
        if not str(event.sender_id) == XXX:
            return await event.edit(
                "You are sudo user, You cant remove other sudo user.",
            )
        ok = await event.reply("**Updating SUDO Users List ...**")
        mmm = ""
        if inputs:
            id = await get_user_id(inputs)
            try:
                name = (await event.client.get_entity(int(id))).first_name
            except BaseException:
                name = ""
            del_sudo(id)
            if name != "":
                mmm += f"**Removed [{name}](tg://user?id={id}) from SUDO User(s)**"
            else:
                mmm += f"**Removed ****{id}**** from SUDO User(s)**"
        else:
            mmm += "**add it's id/username.**"
        await ok.edit(mmm)
    else:
        event.reply("**Go Away**")


@bot_cmd("listsudos ?(.*)")
async def _(event):
    ok = await event.reply("**...**")
    sudos = db.get("SUDO_USERS")
    if sudos == "" or sudos is None:
        return await ok.edit("**No SUDO User was assigned ...**", time=5)
    sumos = sudos.split(" ")
    msg = ""
    for i in sumos:
        if i == " ":
            sumos.remove(" ")
        if i == " ":
            sudos.remove(" ")
        try:
            name = (await event.client.get_entity(int(i))).first_name
        except BaseException:
            name = ""
        if name != "":
            msg += f"• [{name}](tg://user?id={i}) ( `{i}` )\n"
        else:
            msg += f"• **{i}** -> Invalid User\n"
    return await ok.edit(
        f"**List of SUDO Users :**\n{msg}", link_preview=False)