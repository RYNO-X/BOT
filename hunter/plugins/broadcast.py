from . import *

@bot_cmd("bcast ?(.*)")
async def _(e):
    if str(e.sender_id) in all_sudo():
        msg = e.pattern_match.group(1)
        for x in all_chats():
            try:
                await bot.send_message(int(x), msg)
                await e.reply(f"Broadcast Sent To {len(x)} Chats")
            except Exception as err:
                await e.reply(f"Error {str(err)}")  
    else:
        await e.reply("**Go Away**")