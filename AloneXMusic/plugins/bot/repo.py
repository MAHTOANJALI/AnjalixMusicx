from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AloneXMusic import app
from config import BOT_USERNAME

start_txt = """
✪ 𝐖εℓ¢σмє 𝐅σя мαнтσ 𝐑єρσѕ ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛𝗘𝗟𝗣", url="https://t.me/BLACKx_GOD"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/QUEENx_GOD"),
          ],
               [
                InlineKeyboardButton("𝗔𝗡𝗝𝗔𝗟𝗜 𝗪𝗢𝗥𝗟𝗗", url=f"https://t.me/MAHTOxOFFICIAL"),

],
[
              InlineKeyboardButton("𝗩1 𝗠𝗨𝗦𝗜𝗖", url=f"https://github.com/TeamAloneOp/AloneX"),
              InlineKeyboardButton("𝗩2 𝗠𝗨𝗦𝗜𝗖", url=f"https://github.com/TeamAloneOp/AloneXMusic"),
              ],
              [
              InlineKeyboardButton("𝗩1 𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧", url=f"https://github.com/TeamAloneOp/AloneXRobot"),
InlineKeyboardButton("𝗩2 𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧", url=f"https://github.com/TeamAloneOp/AloneRobot"),
],
[
InlineKeyboardButton("𝗔𝗡𝗝𝗔𝗟𝗜 𝗠𝗨𝗦𝗜𝗖¹", url=f"https://github.com/TeamAloneOp/Telethon-Music"),
InlineKeyboardButton("𝗔𝗡𝗝𝗔𝗟𝗜 𝗠𝗨𝗦𝗜𝗖²", url=f"https://github.com/TeamAloneOp/AloneMusicBot"),
],
[
InlineKeyboardButton("𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://github.com/TeamAloneOp/AloneXChatBot"),
InlineKeyboardButton("𝗜𝗗 𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://github.com/TeamAloneOp/AloneXIdChatbot"),
],
[
              InlineKeyboardButton("𝗦𝗣𝗔𝗠", url=f"https://github.com/TeamAloneOp/AloneXSpam"),
              InlineKeyboardButton("𝗕𝗔𝗡𝗔𝗟𝗟", url=f"https://github.com/TeamAloneOp/AloneXBanallBot"),
              ],
              [
              InlineKeyboardButton("𝗔𝗡𝗝𝗔𝗟𝗜𝗦𝗧𝗥𝗜𝗡𝗚𝗕𝗢𝗧", url=f"https://t.me/AnjalixSessionBot"),
              InlineKeyboardButton("𝗕𝗬𝗣𝗔𝗦𝗦", url=f"https://github.com/TeamAloneOp/AloneXBypass"),
],
[
InlineKeyboardButton("𝗙𝗜𝗟𝗘 𝗥𝗘𝗡𝗔𝗠𝗘 𝗕𝗢𝗧", url=f"https://t.me/AnjalixRenameBot"),
InlineKeyboardButton("𝗧𝗚 𝗔𝗣𝗣𝗥𝗢𝗩𝗘 𝗕𝗢𝗧", url=f"https://t.me/AnjalixAppoveBot"),
],
[
InlineKeyboardButton("𝗢𝗙𝗙𝗜𝗖𝗜𝗔𝗟 𝗕𝗢𝗧", url=f"https://t.me/AloneXMusicBot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://te.legra.ph/file/ebd94c36f077edce512b3.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
