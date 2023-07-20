from aiogram import types

ikb = types.InlineKeyboardMarkup()
likes = 0
dislikes = 0
btn_1 = types.InlineKeyboardButton(text="👍🏾 (niggerly) " + str(likes), callback_data="like")
btn_2 = types.InlineKeyboardButton(text="👎🏾 (buster) " + str(dislikes), callback_data="dislike")
ikb.add(btn_1, btn_2)

