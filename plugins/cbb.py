#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b> This bot was created by 👉 <a href='https://t.me/lflixadmin'>L-FLIX Admin</a> /n 𝑰𝒇 𝒚𝒐𝒖 𝒏𝒆𝒆𝒅 𝒂 𝒔𝒊𝒎𝒊𝒍𝒂𝒓 𝒃𝒐𝒕 𝒍𝒊𝒌𝒆 𝒕𝒉𝒊𝒔, 𝒚𝒐𝒖 𝒄𝒂𝒏 𝒄𝒐𝒏𝒕𝒂𝒄𝒕 𝒕𝒉𝒆 𝒂𝒅𝒎𝒊𝒏 𝒐𝒏:/n/n  𝑷𝒉𝒐𝒏𝒆 𝒏𝒐:<code>+256704312951</code>/n/n 𝑾𝒉𝒂𝒕𝒔𝒂𝒑𝒑:<a href='https://wa.me/qr/A3GNDFJZU2G3P1'>𝑪𝑳𝑰𝑪𝑲 𝑯𝑬𝑹𝑬</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 𝑪𝑳𝑶𝑺𝑬", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
