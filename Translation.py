# This file is a part of TG-FileStreamBot
from WebStreamer.vars import Var
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


class Language(object):
    def __new__ (self, message: Message):
        if getattr(message.from_user, 'language_code', 'Unknown') in self.available:
            return getattr(self, getattr(message.from_user, 'language_code', self.en), self.en)
        else:
            return self.en

    available=['en', 'Test']

    class en(object):
        START_TEXT = """ <b>
ʜᴇʟʟᴏ, {}

ɪᴛ'ꜱ.. ᴍᴇ ꜰɪʟᴇ ᴛᴏ - [ꜱʜᴏʀᴛ ʟɪɴᴋ] ♡︎

ꜱᴇᴇ ᴍʏ ᴩᴏᴡᴇʀ ⚡.....!!

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ʟɪɴᴋ ᴛʜɪꜱ ʙᴏᴛ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ..!
</b> """

        HELP_TEXT = """ <b>𝐇𝐄𝐘 𝐁𝐑𝐔𝐇
✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵
╔════❰ ꫝꪖ𝘳𝓲 ❱═❍⊱❁۪۪
║┏━━━━━━━━━━━━━━━➣
║┣
║┣  ☔ꜰɪʟᴇ ᴛᴏ-[ꜱʜᴏʀᴛ ʟɪɴᴋ] ❣
║┣
║┗━━━━━━━━━━━━━━━➣
║┏━━━━━━━━━━━━━━━➣
║┣    ⚡ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ʙᴏᴛ..⚡
║┣    
║┣ ꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ (ᴏʀ) ᴍᴇᴅɪᴀ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ.
║┣ ɪ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ!.
║┣ ᴅᴏᴡɴʟᴏᴀᴅ Lɪɴᴋ Wɪᴛʜ Fᴀsᴛᴇsᴛ Sᴘᴇᴇᴅ
║┣
║┣🦋 ᴍʏ ʙᴇsᴛ ғʀɪᴇɴᴅ :<a href=tg://settings>ᴛʜɪs ᴘᴇʀsᴏɴ 🙌</a>
║┣
║┗━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁</b>
"""

        DON_TXT = """
<b>𝐇𝐄𝐘 𝐁𝐑𝐔𝐇
✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵
╔════❰ ꫝꪖ𝘳𝓲 ❱═❍⊱❁۪۪
║┏━━━━━━━━━━━━━━━➣
║┣🎯✨ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ꜰʟɪᴍꜱ ʜᴅ ᴏꜰꜰɪᴄɪᴀʟ❣
║┣⚡️🍬ᴊᴏɪɴ ᴏᴜʀ ᴍᴏᴠɪᴇꜱ ᴄʜᴀɴɴᴇʟꜱ 🦋✨
║┗━━━━━━━━━━━━━━━➣
║┏━━━━━━━━━━━━━━━➣
║┣
║┣<a href=https://t.me/TAMIL_FLIMS_HD>🔰✥ ▷ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ ◁</a>
║┣
║┣<a href=https://t.me/+lp5mOR6wSMIyMzY1>🔰✥ ▷ ꜰʟɪᴍꜱ ʜᴅ ᴏꜰꜰɪᴄɪᴀʟ ꜰɪʟᴇ 1 ◁</a>
║┣
║┣<a href=https://t.me/+VyuE_q8JC9UzZTll>🔰✥ ▷ ꜰʟɪᴍꜱ ʜᴅ ᴏꜰꜰɪᴄɪᴀʟ ꜰɪʟᴇ 2 ◁</a>
║┣
║┣<a href=https://t.me/+TJzbQrEhZBg3ZGRl>🔰✥ ▷ ꜰʟɪᴍꜱ ʜᴅ ᴏꜰꜰɪᴄɪᴀʟ ꜰɪʟᴇ 3 ◁</a>
║┣
║┣🦋 ᴍʏ ʙᴇsᴛ ғʀɪᴇɴᴅ :<a href=tg://settings>ᴛʜɪs ᴘᴇʀsᴏɴ 🙌</a>
║┣
║┗━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁</b>
"""

        ABOUT_TEXT = """
<b>𝗔𝗕𝗢𝗨𝗧 𝗠𝗦𝗚
✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵✵
╔════❰ ꫝꪖ𝘳𝓲 ❱═❍⊱❁۪۪
║┏━━━━━━━━━━━━━━━➣
║┣⪼ 𝓜𝔂 𝓝𝓪𝓶𝓮 - 𝙵𝙸𝙻𝙴 𝚃𝙾 𝙻𝙸𝙽𝙺
║┣⪼ 𝓒𝓻𝓮𝓪𝓽𝓸𝓻 - <a href=https://t.me/Hari_OP>𝙷𝙰𝚁𝙸 𓆩♡︎𓆪</a>
║┣⪼ 𝓛𝓲𝓫𝓻𝓪𝓻𝓻𝔂 - 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
║┣⪼ 𝓛𝓪𝓷𝓰𝓾𝓪𝓰𝓮 - 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
║┣⪼ 𝓓𝓪𝓽𝓪 𝓑𝓪𝓼𝓮 - 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
║┣⪼ 𝓑𝓸𝓽 𝓼𝓮𝓻𝓿𝓮𝓻 - 𝙺𝙾𝚈𝙴𝙱
║┣⪼ 𝓑𝓸𝓽 𝓡𝓮𝓸𝓹 - 𝙿𝙰𝙸𝙳 𝙾𝙽𝙻𝚈
║┣⪼ 𝓑𝓾𝓲𝓵𝓭 𝓢𝓽𝓪𝓽𝓾𝓼 - v1.0.1 [ 𝙱𝙴𝚃𝙰 ]
║┗━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁</b>"""

        stream_msg_text ="""
<b><i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>

📂 Fɪʟᴇ ɴᴀᴍᴇ : <code>{}</code>

📦 Fɪʟᴇ ꜱɪᴢᴇ : <code>{}</code>

📥 Dᴏᴡɴʟᴏᴀᴅ : {}

🚸 Nᴏᴛᴇ : Tʜɪs Pᴇʀᴍᴀɴᴇɴᴛ Lɪɴᴋ , Nᴏᴛ Exᴘɪʀᴇᴅ
</b>
"""

    class Test(object):
        START_TEXT = """
<i>👋 Hᴇʏ in Russian,</i>{}\n
<i>I'm Telegram Files Streaming Bot As Well Direct Links Generator</i>\n
<i>Cʟɪᴄᴋ ᴏɴ Hᴇʟᴘ ᴛᴏ ɢᴇᴛ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</i>\n
<i><u>𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸</u></i>\n
<b>🔞 Pʀᴏɴ ᴄᴏɴᴛᴇɴᴛꜱ ʟᴇᴀᴅꜱ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ ʏᴏᴜ.</b>\n\n"""

# ------------------------------------------------------------------------------

class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
         [
             [
                 InlineKeyboardButton("🍁 ꜱᴜᴩᴩᴏʀᴛ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ 🍁", url="https://t.me/TAMIL_FLIMS_HD")
             ],
             [
                 InlineKeyboardButton("💥 ᴜᴘᴅᴀᴛᴇᴢ 💥", url="https://t.me/+weOCjKl9oZs1ODJl"),
                 InlineKeyboardButton("😇 ᴏᴡɴᴇʀ 😇", url="https://t.me/Hari_OP")
             ],
             [
                 InlineKeyboardButton("🦋 ʜᴇʟᴩ 🦋", callback_data="help"),
                 InlineKeyboardButton("✨ ᴀʙᴏᴜᴛ ✨", callback_data="about")
             ]
         ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
         [
             [
                 InlineKeyboardButton("😊 ꜱᴏᴜʀᴄᴇ 😊", callback_data="don")
             ],
             [
                 InlineKeyboardButton("☔ ʜᴏᴍᴇ ☔", callback_data="home"),
                 InlineKeyboardButton("🌲 ᴄʟᴏsᴇ 🌲", callback_data="close")
             ]
         ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("😊 ꜱᴏᴜʀᴄᴇ 😊", callback_data="don")
            ],
            [
                InlineKeyboardButton("☔ ʜᴏᴍᴇ ☔", callback_data="home"),
                InlineKeyboardButton("🌲 ᴄʟᴏsᴇ 🌲", callback_data="close")
            ]
        ]
    )

    DONATE_BUTTONS = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ᴩᴀʏ 💰 ᴀᴍᴏᴜɴᴛ", url="https://t.me/Hari_OP")
            ],
            [
                InlineKeyboardButton("☔ ʜᴏᴍᴇ ☔", callback_data="home"),
                InlineKeyboardButton("🌲 ᴄʟᴏsᴇ 🌲", callback_data="close")
            ]
        ]
    ) 
