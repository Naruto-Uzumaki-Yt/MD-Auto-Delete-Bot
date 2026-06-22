# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

import os
import asyncio
from config import API_ID, API_HASH, BOT_TOKEN, DATABASE_URL, BOT_USERNAME, FORCE_SUB_CHANNEL, OWNER_ID

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from flask import Flask, redirect
from threading import Thread
from motor.motor_asyncio import AsyncIOMotorClient
from pyrogram.errors import FloodWait

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# MongoDB
client = AsyncIOMotorClient(DATABASE_URL)
db = client['databas']
groups = db['group_id']
users = db['users']

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# Bot setup
bot = Client("deletebot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# ➤ Force Subscribe checker (only for admins)
async def check_force_sub(client, chat_id, user_id):
    try:
        member = await client.get_chat_member(f"@{FORCE_SUB_CHANNEL}", user_id)
        if member.status not in [enums.ChatMemberStatus.OWNER, enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.MEMBER]:
            return False
    except:
        return False
    return True
  
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@bot.on_message(filters.command("start") & filters.private)
async def start(_, message):
    user_id = message.from_user.id

    # FORCE SUB CHECK
    if not await check_force_sub(bot, message.chat.id, user_id):
        btn = [[InlineKeyboardButton("🔔 Jᴏɪɴ Cʜᴀɴɴᴇʟ", url=f"https://t.me/{FORCE_SUB_CHANNEL}")]]
        await message.reply(
            "**›› ‼️ ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴᴇᴅ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, sᴜʙsᴄʀɪʙᴇ ɴᴏw.**",
            reply_markup=InlineKeyboardMarkup(btn)
        )
        return

    await users.update_one(
        {"user_id": user_id},
        {"$set": {"user_id": user_id}},
        upsert=True
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

    # ---------------- START ANIMATION ---------------- #
    m = await message.reply_text("ᴍᴏɴᴋᴇʏ ᴅ ʟᴜғғʏ\nɢᴇᴀʀ 𝟻. . .")
    await asyncio.sleep(0.5)
    await m.edit_text("🔥")
    await asyncio.sleep(0.5)
    await m.edit_text("⚡")
    await asyncio.sleep(0.5)
    await m.edit_text("sᴜɴ ɢᴏᴅ ɴɪᴋᴀ!...")
    await asyncio.sleep(0.5)
    await m.delete()
    # ------------------------------------------------ #

    buttons = [
        [InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕",
                              url=f"https://t.me/{BOT_USERNAME}?startgroup=true&admin=delete_messages")],
        [InlineKeyboardButton("❓ ʜᴇʟᴘ", callback_data="help"),
         InlineKeyboardButton("ℹ️ ᴀʙᴏᴜᴛ", callback_data="about")]
    ]

    await message.reply_text(
        "**👋 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝖳𝗈 𝖬𝖣 𝖠𝗎𝗍𝗈 𝖣𝖾𝗅𝖾𝗍𝖾𝗋 𝖡𝗈𝗍!**\n\n"
        "**𝖨 𝖼𝖺𝗇 𝖺𝗎𝗍𝗈-𝖽𝖾𝗅𝖾𝗍𝖾 𝗀𝗋𝗈𝗎𝗉 𝗆𝖾𝗌𝗌𝖺𝗀𝖾𝗌 𝖺𝖿𝗍𝖾𝗋 𝖺 𝗌𝖾𝗍 𝗍𝗂𝗆𝖾.**\n"
        "**𝖴𝗌𝖾 𝗆𝖾 𝗂𝗇 𝗒𝗈𝗎𝗋 𝗀𝗋𝗈𝗎𝗉𝗌 𝗍𝗈 𝗄𝖾𝖾𝗉 𝗍𝗁𝖾𝗆 𝖼𝗅𝖾𝖺𝗇**.\n\n**𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗯𝘆** @Anime_UpdatesAU",
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode=enums.ParseMode.MARKDOWN
    )
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@bot.on_callback_query()
async def callback_handler(_, query: CallbackQuery):
    if query.data == "help":
        await query.message.edit_text(
            "**🛠 𝖧𝖾𝗅𝗉 𝖬𝖾𝗇𝗎**\n\n"
            "/set_time <sec> – Set auto delete timer.\n"
            "/disable – Disable auto-delete.\n"
            "/status – Show current delete timer.\n\n**𝖭𝗈𝗍𝖾 : 𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖶𝗈𝗋𝗄 𝖮𝗇𝗅𝗒 in 𝖦𝗋𝗈𝗎𝗉.**",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="back")]])
        )
    elif query.data == "about":
        await query.message.edit_text(
             """<b>ℹ️ ᴀʙᴏᴜᴛ</b>

⍟───[ MY ᴅᴇᴛᴀɪʟꜱ ]───⍟
‣ ᴍʏ ɴᴀᴍᴇ : <a href="https://t.me/MD_AutoDelete_bot">ᴍᴅ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ʙᴏᴛ</a>
‣ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href="https://t.me/Mr_Mohammed_29">ᴍᴏʜᴀᴍᴍᴇᴅ</a>
‣ ʟɪʙʀᴀʀʏ : <a href="https://pypi.org/project/Pyrogram/">ᴘʏʀᴏɢʀᴀᴍ 𝟸.𝟶</a>
‣ ʟᴀɴɢᴜᴀɢᴇ : <a href="https://www.python.org/downloads/">ᴘʏᴛʜᴏɴ 𝟹</a>
‣ ᴅᴀᴛᴀ ʙᴀsᴇ : <a href="https://www.mongodb.com/">ᴍᴏɴɢᴏ ᴅʙ</a>
‣ ʙᴏᴛ sᴇʀᴠᴇʀ : <a href="https://render.com/">Bᴏᴛs Sᴇʀᴠᴇʀ</a>
‣ ᴜᴘᴅᴀᴛᴇs : <a href="https://t.me/Anime_UpdatesAU">ᴀɴɪᴍᴇ ᴜᴘᴅᴀᴛᴇs</a>
‣ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ2.𝟶 <a href="https://t.me/Anime_UpdatesAU">sᴛᴀʙʟᴇ</a>

</b>""",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="back"),
                InlineKeyboardButton("Rᴇᴘᴏ", url="https://github.com/MohammedDev-yt/MD-Auto-Delete-Bot")
            ]
        ]),
        parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "back":
        await query.message.edit_text(
            "**👋 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝖳𝗈 𝖬𝖣 𝖠𝗎𝗍𝗈 𝖣𝖾𝗅𝖾𝗍𝖾𝗋 𝖡𝗈𝗍!**\n\n**𝖨 𝖼𝖺𝗇 𝖺𝗎𝗍𝗈-𝖽𝖾𝗅𝖾𝗍𝖾 𝗀𝗋𝗈𝗎𝗉 𝗆𝖾𝗌𝗌𝖺𝗀𝖾𝗌 𝖺𝖿𝗍𝖾𝗋 𝖺 𝗌𝖾𝗍 𝗍𝗂𝗆𝖾.**\n**𝖴𝗌𝖾 𝗆𝖾 𝗂𝗇 𝗒𝗈𝗎𝗋 𝗀𝗋𝗈𝗎𝗉𝗌 𝗍𝗈 𝗄𝖾𝖾𝗉 𝗍𝗁𝖾𝗆 𝖼𝗅𝖾𝖺𝗇.**\n\**𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗯𝘆** @Anime_UpdatesAU",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"http://t.me/{BOT_USERNAME}?startgroup=none&admin=delete_messages")],
                [InlineKeyboardButton("❓ ʜᴇʟᴘ", callback_data="help"), InlineKeyboardButton("ℹ️ ᴀʙᴏᴜᴛ", callback_data="about")]
            ])
        )


# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@bot.on_message(filters.command("set_time"))
async def set_delete_time(_, message):
    if message.chat.type == enums.ChatType.PRIVATE:
        return await message.reply("❌ 𝖳𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗈𝗋𝗄𝗌 𝗈𝗇𝗅𝗒 𝗂𝗇 𝗀𝗋𝗈𝗎𝗉𝗌.")

    user_id = message.from_user.id
    is_admin = False
    async for m in bot.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if m.user.id == user_id:
            is_admin = True
            break

    if not is_admin:
        try:
            await message.delete()
        except: pass
        return

    if len(message.command) < 2:
        buttons = [[
            InlineKeyboardButton("2 min", callback_data="time_120"),
            InlineKeyboardButton("5 min", callback_data="time_300"),
            InlineKeyboardButton("15 min", callback_data="time_900")
        ], [
            InlineKeyboardButton("Custom", callback_data="custom")
        ]]
        msg = await message.reply("⏱️ 𝖢𝗁𝗈𝗈𝗌𝖾 𝖣𝖾𝗅𝖾𝗍𝖾 𝖳𝗂𝗆𝖾:", reply_markup=InlineKeyboardMarkup(buttons))
        await asyncio.sleep(10)
        try:
            await msg.delete()
            await message.delete()
        except: pass
        return

    delete_time = message.text.split()[1]
    if not delete_time.isdigit():
        reply = await message.reply("❌ 𝖳𝗂𝗆𝖾 𝗆𝗎𝗌𝗍 𝖻𝖾 𝖺 𝗇𝗎𝗆𝖻𝖾𝗋 𝗂𝗇 𝗌𝖾𝖼𝗈𝗇𝖽𝗌.")
        await asyncio.sleep(5)
        try:
            await reply.delete()
            await message.delete()
        except: pass
        return

    await groups.update_one({"group_id": message.chat.id}, {"$set": {"delete_time": int(delete_time)}}, upsert=True)
    reply = await message.reply(f"✅ 𝖠𝗎𝗍𝗈-𝖽𝖾𝗅𝖾𝗍𝖾 𝗍𝗂𝗆𝖾 𝗌𝖾𝗍 𝗍𝗈 {delete_time} 𝗌𝖾𝖼𝗈𝗇𝖽𝗌.")
    await asyncio.sleep(5)
    try:
        await reply.delete()
        await message.delete()
    except: pass

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@bot.on_message(filters.command("status") & filters.group)
async def status(_, message):
    group = await groups.find_one({"group_id": message.chat.id})
    if group:
        await message.reply_text(f"**🕒 𝖢𝗎𝗋𝗋𝖾𝗇𝗍 𝖽𝖾𝗅𝖾𝗍𝖾 𝗍𝗂𝗆𝖾 :** `{group['delete_time']}` seconds")
    else:
        await message.reply_text("**🛑 𝖠𝗎𝗍𝗈-𝖽𝖾𝗅𝖾𝗍𝖾 𝗂𝗌 𝗇𝗈𝗍 𝗌𝖾𝗍 𝖿𝗈𝗋 𝗍𝗁𝗂𝗌 𝗀𝗋𝗈𝗎𝗉.**")

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@bot.on_message(filters.command("disable") & filters.group)
async def disable(_, message):
    user_id = message.from_user.id
    async for m in bot.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if m.user.id == user_id:
            await groups.delete_one({"group_id": message.chat.id})
            await message.reply_text("✅ **𝖠𝗎𝗍𝗈-𝖽𝖾𝗅𝖾𝗍𝖾 𝖽𝗂𝗌𝖺𝖻𝗅𝖾𝖽 𝖿𝗈𝗋 𝗍𝗁𝗂𝗌 𝗀𝗋𝗈𝗎𝗉.**")
            return
    await message.reply("❌ 𝖠𝗎𝗍𝗈-𝖽𝖾𝗅𝖾𝗍𝖾 𝖽𝗂𝗌𝖺𝖻𝗅𝖾𝖽 𝖿𝗈𝗋 𝗍𝗁𝗂𝗌 𝗀𝗋𝗈𝗎𝗉.")

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@bot.on_message(filters.command("broadcast") & filters.private)
async def broadcast(_, message):
    if message.from_user.id != OWNER_ID:
        return await message.reply("❌ 𝖸𝗈𝗎'𝗋𝖾 𝗇𝗈𝗍 𝖺𝗎𝗍𝗁𝗈𝗋𝗂𝗓𝖾𝖽.")

    if len(message.command) < 2:
        return await message.reply("𝖴𝗌𝖺𝗀𝖾: `/broadcast 𝖸𝗈𝗎𝗋 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗁𝖾𝗋𝖾...`", parse_mode=enums.ParseMode.MARKDOWN)

    text = message.text.split(None, 1)[1]
    sent = 0
    failed = 0
    async for user in users.find({}):
        try:
            await bot.send_message(user["user_id"], text)
            sent += 1
            await asyncio.sleep(0.1)
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except:
            failed += 1
            continue

    await message.reply(f"✅ 𝖡𝗋𝗈𝖺𝖽𝖼𝖺𝗌𝗍 𝗌𝖾𝗇𝗍 𝗍𝗈 {sent} 𝗎𝗌𝖾𝗋𝗌.\n❌ 𝖥𝖺𝗂𝗅𝖾𝖽: {failed}")

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@bot.on_message(filters.command("users") & filters.private)
async def total_users(_, message):
    if message.from_user.id != OWNER_ID:
        return await message.reply("❌ 𝖸𝗈𝗎'𝗋𝖾 𝗇𝗈𝗍 𝖺𝗎𝗍𝗁𝗈𝗋𝗂𝗓𝖾𝖽.")
    total = await users.count_documents({})
    await message.reply(f"👤 𝖳𝗈𝗍𝖺𝗅 𝖴𝗌𝖾𝗋𝗌: `{total}`", parse_mode=enums.ParseMode.MARKDOWN)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@bot.on_message(filters.group & filters.text)
async def auto_delete(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if message.from_user.is_bot:
        return

    group = await groups.find_one({"group_id": chat_id})
    if not group:
        return

    async for m in bot.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if m.user.id == user_id:
            return

    try:
        await asyncio.sleep(int(group["delete_time"]))
        await message.delete()
    except Exception as e:
        print(f"𝖤𝗋𝗋𝗈𝗋 𝖽𝖾𝗅𝖾𝗍𝗂𝗇𝗀 𝗆𝖾𝗌𝗌𝖺𝗀𝖾: {e}")
      
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@bot.on_message(filters.command("g_broadcast") & filters.private)
async def broadcast(_, message):
    if message.from_user.id != OWNER_ID:
        return await message.reply("🚫 𝖸𝗈𝗎 𝖺𝗋𝖾 𝗇𝗈𝗍 𝖺𝗅𝗅𝗈𝗐𝖾𝖽 𝗍𝗈 𝖻𝗋𝗈𝖺𝖽𝖼𝖺𝗌𝗍.")

    if len(message.command) < 2:
        return await message.reply("📢 𝖴𝗌𝖺𝗀𝖾: /broadcast Your message here")

    text = message.text.split(None, 1)[1]
    success = 0
    fail = 0
    async for group in groups.find({}):
        try:
            await bot.send_message(group["group_id"], text)
            success += 1
        except:
            fail += 1
    await message.reply(f"✅ 𝖡𝗋𝗈𝖺𝖽𝖼𝖺𝗌𝗍 𝖢𝗈𝗆𝗉𝗅𝖾𝗍𝖾𝖽.\nS𝖾𝗇𝗍: {success}, 𝖥𝖺𝗂𝗅𝖾𝖽: {fail}")
  
# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# Flask keep-alive
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(f"https://t.me/{BOT_USERNAME}", code=302)

def run():
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))

if __name__ == "__main__":
    Thread(target=run).start()
    bot.run()

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #