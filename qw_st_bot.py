from aiogram import Bot, Dispatcher, executor, types
import logging

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

import markups as nav
from main_s import Database
from main_s import Registration

API_TOKEN = '5536890192:AAEQgIYCfyJc0UwoCWA6NFRMuObZwlu_ATs'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

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


'''
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if not db.user_exists(message.from_user.id):
        # print(db.user_exist(message.from_user.id))
        db.add_user(message.from_user.id)
        db.set_t_user(message.from_user.id, message.from_user.username )
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
                db.set_name(message.from_user.id, message.text)

                await bot.send_message(message.from_user.id, "Qwasar useringizni kiriting")
                db.add_quser(message.from_user.id, message.text)
                db.set_signup(message.from_user.id, "done")                                     #Shu joyida ishlavomman!!!!
                await bot.send_message(message.from_user.id, "Registrasiya muvafiqiyatli otti!",
                                       reply_markup=nav.mainMenu)



            else:
                await bot.send_message(message.from_user.id, "Nma?")
'''


@dp.message_handler(commands=['start'])
async def register(message: types.Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
        db.set_t_user(message.from_user.id, message.from_user.username)
        await bot.send_message(message.from_user.id, "Siz Registrasiyani boshladingiz\nOtingizni kiriting")
        await Registration.name.set()
    else:
        await bot.send_message(message.from_user.id, "Siz registrasiyadan otib bolgansiz!", reply_markup=nav.mainMenu)


@dp.message_handler(state=Registration.name)
async def state_name(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(name=answer)
    await bot.send_message(message.from_user.id, "Qwasar nikingizni kiriting")
    await Registration.qwasar_user.set()


@dp.message_handler(state=Registration.qwasar_user)
async def state_qwname(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(qwasar_user=answer)
    await bot.send_message(message.from_user.id, "Telefon nomeringizni kiriting")
    await Registration.phone.set()


@dp.message_handler(state=Registration.phone)
async def state_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(phone=answer)
    await bot.send_message(message.from_user.id, "Qaysi seasonda o'qiysiz?")
    await Registration.season.set()


@dp.message_handler(state=Registration.season)
async def state_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(season=answer)
    await bot.send_message(message.from_user.id, "Qaysi xonada otirasiz?")
    await Registration.stay.set()


@dp.message_handler(state=Registration.stay)
async def state_phone(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(stay=answer)
    await bot.send_message(message.from_user.id, "Rasimingizni tashlang")
    await Registration.path.set()


@dp.message_handler(state=Registration.path)
async def state_season(message: types.Message, state: FSMContext):
    # answer = message.text
    # await state.update_data(path=answer)
    # data = await state.get_data()
    # name = data.get('name')
    # q_user = data.get('qwasar_user')
    # phone = data.get('phone')
    # season = data.get('season')
    # stay = data.get('stay')
    # path = data.get('path')
    # print(name)
    # print(q_user)
    # print(phone)
    # print(season)
    # print(stay)
    # print(path)
    # db.set_name(message.from_user.id, name)
    # db.add_quser(message.from_user.id, q_user)
    # db.set_phone_number(message.from_user.id, phone)
    # db.set_season(message.from_user.id, season)
    # db.set_stay(message.from_user.id, stay)
    # db.set_path(message.from_user.id, path)

    if db.get_signup(message.from_user.id) == 'setnickname':
        answer = message.text
        await state.update_data(path=answer)
        data = await state.get_data()
        name = data.get('name')
        q_user = data.get('qwasar_user')
        phone = data.get('phone')
        season = data.get('season')
        stay = data.get('stay')
        path = data.get('path')
        print(name)
        print(q_user)
        print(phone)
        print(season)
        print(stay)
        print(path)
        db.set_name(message.from_user.id, name)
        db.add_quser(message.from_user.id, q_user)
        db.set_phone_number(message.from_user.id, phone)
        db.set_season(message.from_user.id, season)
        db.set_stay(message.from_user.id, stay)
        db.set_path(message.from_user.id, path)

        db.set_signup(message.from_user.id, "done")  # Shu joyida ishlavomman!!!!
        await bot.send_message(message.from_user.id, "Registrasiya muvafiqiyatli otti!",
                               reply_markup=nav.mainMenu)
        await state.finish()

    # await bot.send_message(message.from_user.id, "Registrasiya muvafiqiyatli otti!", reply_markup=nav.mainMenu)
    # await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
