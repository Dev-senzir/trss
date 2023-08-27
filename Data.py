from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("🔥 بـدء الاسـتخراج 🔥", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 الصـفحة الرئـيسيه 🏠", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                "✨ للمزيـد مـن البـوتات ✨", url="https://t.me/Xx_MO_ON_xX"
            )
        ],
        [
            InlineKeyboardButton("🤔 الاوامـر 🤔", callback_data="help"),
            InlineKeyboardButton("🎪 حـول الـبوت 🎪", callback_data="about"),
        ],
        [InlineKeyboardButton("💌 قـناة البـوت 💌", url="https://t.me/Xx_MO_ON_xX")],
    ]

    START = """
ʜᴇʏ {}
ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {}
ɪꜰ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴛʀᴜsᴛ ᴛʜɪs ʙᴏᴛ, 
1) sᴛᴏᴘ ʀᴇᴀᴅɪɴɢ ᴛʜɪs ᴍᴇssᴀɢᴇ
2) ᴅᴇʟᴇᴛᴇ ᴛʜɪs ᴄʜᴀᴛ
sᴛɪʟʟ ʀᴇᴀᴅɪɴɢ?
ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ. ᴜsᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ !
ʙʏ @V2R_3 ᴀɴᴅ @Xx_MO_ON_xX
    """

    HELP = """
✨ **الاوامـر المـتاحه** ✨

/about - حـول البـوت
/help - الاوامـر المـساعدة
/start - سـتارت البـوت
/repo - ريـبو المـطور
/generate - بـدء الاسـتخراج
/cancel - الـغاء العمـليه
/restart - الـغاء العمـليه
"""

    # About Message
    ABOUT = """
**حـول الـبوت** 

ᴀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ ʙʏ @V2R_3

sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/Xx_MO_ON_xX)
ғʀᴀᴍᴇᴡᴏʀᴋ : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)
ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ](www.python.org)
ᴏᴡɴᴇʀ : @G5_F1
    """

    # Repo Message
    REPO = """
━━━━━━━━━━━━━━━━━━━━━━━━
💥 A ᴘᴏᴡᴇʀғᴜʟ ʙᴏᴛ
ᴏғ ♻️ MR-BLACK 🔥
━━━━━━━━━━━━━━━━━
ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ғᴏʀ ᴛɢ...
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴄʀᴇᴀᴛᴇʀ [ᴀsᴀᴅ ᴀʟɪ](https://t.me/Xx_MO_ON_xX)
┣★ ʜᴇᴀʀᴛ ᴜs  [ʜᴇᴀʀᴛ ❤️](https://t.me/Xx_MO_ON_xX)
┣★ ʙᴏᴛ ᴜᴏᴅᴀᴛᴇs [ᴏᴜʀ ᴏᴛʜᴇʀ ʙᴏᴛs](https://t.me/Xx_MO_ON_xX)
┣★ ᴀʟᴇxᴀ ғᴇᴅ [ғᴇᴅ ʟᴏɢs](https://t.me/Xx_MO_ON_xX)
┣★ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/Xx_MO_ON_xX)
┣★ ɴᴇᴛᴡᴏʀᴋ [ʀᴏᴄᴋs](https://t.me/Xx_MO_ON_xX)
┗━━━━━━━━━━━━━━━━━┛
💞 
IF HAVE ANY QUESTION THEN CONTACT » TO » MY » [OWNER] @Xx_MO_ON_xX
   """
