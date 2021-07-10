import re

from . import *


@bot_cmd("setredis ?(.*)")
async def _(event):
    if str(event.sender_id) in all_sudo():
        if not event.out:
            if not str(event.sender_id) == XXX:
                return await event.reply("**This Command Is Sudo Restricted**")
        ok = await event.reply( "`...`")
        try:
            delim = " " if re.search("[|]", event.pattern_match.group(1)) is None else " | "
            data = event.pattern_match.group(1).split(delim, maxsplit=1)
            db.set(data[0], data[1])
            redisdata = db.get(data[0])
            await ok.edit(
                "Redis Key Value Pair Updated\nKey : `{}`\nValue : `{}`".format(
                    data[0],
                    redisdata,
                ),
            )
        except BaseException:
            await ok.edit("`Something Went Wrong`")
    else:
        await event.reply("**Go Away**")

@bot_cmd("delredis ?(.*)")
async def _(event):
    if str(event.sender_id) in all_sudo():
        if not event.out:
            if not str(event.sender_id) == XXX:
                return await event.reply("**This Command Is Sudo Restricted**")
        ok = await event.reply("**Deleting data from Redis ...**")
        try:
            key = event.pattern_match.group(1)
            k = db.delete(key)
            if k == 0:
                return await ok.edit("**No Such Key**")
            await ok.edit(f"**Successfully deleted key** `{key}`")
        except BaseException:
            await ok.edit("**Something Went Wrong**")
    else:
        await event.reply("**Go Away**")


@bot_cmd("getredis ?(.*)")
async def _(event):
    if str(event.sender_id) in all_sudo():
        ok = await event.reply("**Fetching data from Redis**")
        val = event.pattern_match.group(1)
        if val == "":
            return await ok.edit(f"Please use `/getkeys <keyname>`")
        try:
            value = db.get(val)
            await ok.edit(f"Key: `{val}`\nValue: `{value}`")
        except BaseException:
            await ok.edit("`Something Went Wrong`")
    else:
        await event.reply("**Go Away**")

@bot_cmd("getkeys ?(.*)")
async def _(e):
    ok = await e.reply("**wait...**")
    keys = sorted(db.keys())
    msg = ""
    for x in keys:
        if x.isdigit() or x.startswith("-"):
            pass
        else:
            msg += f"~ `{x}`" + "\n"
    await ok.edit(msg)
