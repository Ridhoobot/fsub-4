# (©)Codexbotz
# Recode by @ursickfeeling
# Kalo clone Gak usah hapus 
# gue tandain akun tele nya ngentod

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import CHANNEL, GROUP, OWNER


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>Tentang Bot ini:\n\n • Owner: <a href='https://t.me/idooo5'>Nnettawin</a>\n • Channel: <a href='https://t.me/+AYcedopCRLU5MDE1'>JOIN</a>\n • Pemilik Repo: <a href='https://t.me/idooo5'>Ridoo</a></b>\n",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(" ᴛᴜᴛᴜᴘ ", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
