from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn_srch_by_qw = KeyboardButton('Qwasar user boyicha qidirish')
btn_srch_by_tg = KeyboardButton("Rasm bo'yicha qidirish")

mainMenu = ReplyKeyboardMarkup(resize_keyboard= True)
mainMenu.add(btn_srch_by_qw,btn_srch_by_tg)





