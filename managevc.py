from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.phone import LeaveGroupCall
from pytgcalls import GroupCall
from pyrogram import Client, filters
from pyrogram.types import Message

INPUT_FILENAME = '/bot/downloads/input.raw'
VOICE_CHATS = {}

@Client.on_message(filters.command("join")
    & filters.group
    & ~ filters.edited
async def join_voice_chat(client, message: Message):
    if message.chat.id in VOICE_CHATS:
        await message.edit_text("`[userbot]`: already joined")
        return
    chat_id = message.chat.id
    group_call = GroupCall(client, INPUT_FILENAME)
    await group_call.start(chat_id)
    VOICE_CHATS[chat_id] = group_call
    await message.edit_text("`[userbot]`: Joined Voice Chat")

@Client.on_message(filters.command("leave")
    & filters.group
    & ~ filters.edited
async def leave_voice_chat(client, message: Message):
    chat_id = message.chat.id
    await leave_group_call(client, chat_id)
    VOICE_CHATS.pop(chat_id, None)
    await message.edit_text("`[userbot]`: Left Voice Chat")


async def leave_group_call(client, chat_id):
    peer = await client.resolve_peer(chat_id)
    full_chat = await client.send(GetFullChannel(channel=peer))
    chat_call = full_chat.full_chat.call
    await client.send(LeaveGroupCall(call=chat_call, source=0))

