from . import *
import os
import time
from asyncio.exceptions import TimeoutError
from pathlib import Path
import cv2
from googletrans import Translator
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantsBots
from telethon.tl.types import DocumentAttributeVideo as video
from telethon.utils import pack_bot_file_id
import io
import sys
import traceback
from os import remove

import random
import requests
from carbonnow import Carbon, client
import asyncio
import random
from urllib.parse import quote_plus

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

CARBONLANG = "auto"
LANG = "en"

@bot_cmd("eval ?(.*)")
async def eval(event):
    if not event.is_group:
        return
    if str(event.sender_id) == XXX:    
        if len(event.text) > 5:
            if not event.text[5] == " ":
                return
        if not str(event.sender_id) == str(XXX):
            return await event.reply( "`This Command Is Sudo Restricted.`")
        xx = await event.reply("`Processing ...`")
        try:
            cmd = event.text.split(" ", maxsplit=1)[1]
        except IndexError:
            return await xx.edit("`Give some python cmd`")
        if event.reply_to_msg_id:
            reply_to_id = event.reply_to_msg_id
        old_stderr = sys.stderr
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        redirected_error = sys.stderr = io.StringIO()
        stdout, stderr, exc = None, None, None
        reply_to_id = event.message.id
        try:
            await aexec(cmd, event)
        except Exception:
            exc = traceback.format_exc()
        stdout = redirected_output.getvalue()
        stderr = redirected_error.getvalue()
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        evaluation = ""
        if exc:
            evaluation = exc
        elif stderr:
            evaluation = stderr
        elif stdout:
            evaluation = stdout
        else:
            evaluation = "Success"
        final_output = (
            "> **Eval**\n```{}``` \n\n > **Results**: \n```{}``` \n".format(
                cmd,
                evaluation,
            )
        )
        if len(final_output) > 4096:
            hunt = final_output.replace("`", "").replace("*", "").replace("_", "")
            with io.BytesIO(str.encode(hunt)) as out_file:
                out_file.name = "eval.txt"
                await bot.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    thumb="extras/bot.jpg",
                    allow_cache=False,
                    caption=f"```{cmd}```",
                    reply_to=reply_to_id,
                )
                await xx.delete()
        else:
            await xx.edit(final_output)
    else:
        event.reply("**Go Away**")


async def aexec(code, event):
    exec(
        f"async def __aexec(e, client): "
        + "\n message = event = e"
        + "\n reply = await event.get_reply_message()"
        + "\n chat = e.chat_id"
        + "".join(f"\n {l}" for l in code.split("\n")),
    )

    return await locals()["__aexec"](event, event.client)


@bot_cmd("tr ?(.*)")
async def _(event):
    if not event.is_group:
        return
    if len(event.text) > 3:
        if not event.text[3] == " ":
            return
    input = event.text[4:6]
    txt = event.text[7:]
    xx = await event.reply("`Translating...`")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input or "en"
    elif input:
        text = txt
        lan = input or "en"
    else:
        return await xx.edit(f"`/tr LanguageCode` as reply to a message")
    translator = Translator()
    try:
        tt = translator.translate(text, dest=lan)
        output_str = f"**TRANSLATED** from {tt.src} to {lan}\n{tt.text}"
        await xx.edit(output_str)
    except Exception as exc:
        await xx.edit(str(exc))


@bot_cmd("id ?(.*)")
async def _(event):
    if not event.is_group:
        return
    if event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await event.reply(
                "**Current Chat ID:**  `{}`\n**User ID:**  `{}`\n**File ID:**  `{}`".format(
                    str(event.chat_id),
                    str(r_msg.sender_id),
                    bot_api_file_id,
                ),
            )
        else:
            await event.reply(
                "**Chat ID:**  `{}`\n**User ID:**  `{}`".format(
                    str(event.chat_id),
                    str(r_msg.sender_id),
                ),
            )
    elif event.pattern_match.group(1):
        ids = await get_user_id(event.pattern_match.group(1))
        return await event.reply(
            "**Chat ID:**  `{}`\n**User ID:**  `{}`".format(
                str(event.chat_id),
                str(ids),
            ),
        )
    else:
        await event.reply("**Chat ID:**  `{}`".format(str(event.chat_id)))
