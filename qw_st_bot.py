from aiogram import Bot, Dispatcher, executor, types
import logging
import markups as nav
from main_s import Database

API_TOKEN = '5466643678:AAH9fnTyC0CAwSktV3tZUgalUam006vPfCs'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

db = Database('data.db')

admin_id = '1784921501'  # Abdulaziz
admin_id_1 = "5161784802"  # Abubakr


# @dp.message_handler(commands=['start', 'help'])
# async def send_to_admin(message: types.Message):
#     id_us = message.from_user.id
#     await bot.send_message(chat_id=admin_id, text=id_us)
#
#
# @dp.message_handler()
# async def send_to_admin(message: types.Message):
#     id_us = message.text
#     await bot.send_message(chat_id=id_us, text= 'Hello bro')
#
#
# @dp.message_handler()
# async def echo(message: types.Message):
#     print(message.text)
#     print(message.from_user.id)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if not db.user_exists("user_id"):
        # print(db.user_exist(message.from_user.id))
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Otingizni kiriting")
    else:
        await bot.send_message(message.from_user.id, "Siz registrasiyadan otib bolgansiz!", reply_markup=nav.mainMenu)


@dp.message_handler()
async def bot_mesaage(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Qwasar user boyicha qidirish':
            pass

        else:
            print(db.get_signup(message.from_user.id))
            if db.get_signup(message.from_user.id) == 'setnickname':
                if '@' in message.text or "/" in message.text:
                    await bot.send_message(message.from_user.id, "Taqiqlangan simvol kirittingiz")
                else:

                    db.set_name(message.from_user.id, message.text)
                    db.set_signup(message.from_user.id, "done")
                    await bot.send_message(message.from_user.id, "Registrasiya muvafiqiyatli otti!", reply_markup=nav.mainMenu)
            else:
                await bot.send_message(message.from_user.id, "Nma?")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
