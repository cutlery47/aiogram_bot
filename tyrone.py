from aiogram import Bot, executor, types, Dispatcher
import random
import config
import keyboards
import keyboards as kb
import database as datab

tyrone = Bot(config.TOKEN)
dispatch = Dispatcher(tyrone)

db = datab.MyBD

def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup()
    button = types.KeyboardButton("nigger button", request_location=True)
    keyboard.add(button)
    return keyboard

@dispatch.message_handler(commands=['start'])
async def help_reply(message:  types.Message):
    await tyrone.send_message(chat_id=message.chat.id, text="what it do baby. try /help 😏")

@dispatch.message_handler(commands=['help'])
async def help_reply(message:  types.Message):
    await tyrone.send_message(chat_id=message.chat.id, text=config.COMMANDS, parse_mode='HTML')

@dispatch.message_handler(commands=['who_you_callin_a_nigga'])
async def nigga_reply(message:  types.Message):
    a = random.randrange(1, 10)

    if (a == 5):
        text = "I AM A NIGGER"
    else:
        text = "you's a nigga"

    await tyrone.send_message(chat_id=message.chat.id, text=text)

@dispatch.message_handler(commands=['somethin'])
async def defunny_reply(message: types.Message):
    reply = "dayum cuh clicc thah buttn"
    await tyrone.send_message(chat_id=message.chat.id, text="check them directz if ya in a group chat")
    await tyrone.send_message(chat_id=message.from_user.id, text=reply, reply_markup=get_keyboard())

@dispatch.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    db.add_data(db, lat, lon)
    reply = "latitude:  {}\nlongitude: {}\nyou?".format(lat, lon)
    await tyrone.send_message(chat_id=message.from_user.id, text=reply, reply_markup=types.ReplyKeyboardRemove())

@dispatch.message_handler(commands=['send_nudes'])
async def handle_pics(message: types.Message):
    k = random.randint(0, len(config.IMAGES) - 1)
    await tyrone.send_photo(chat_id=message.chat.id, photo=open(config.IMAGES[k], 'rb'), caption="big dawg big nutz", reply_markup=kb.ikb)



@dispatch.message_handler()
async def return_data(message:  types.Message):
    if "Tyrone" in message.text or "tyrone" in message.text:
        await tyrone.send_message(message.chat.id, "bitch ass nigga")

@dispatch.callback_query_handler()
async def callback_handle(callback: types.CallbackQuery):
    if callback.data == "like":
        await tyrone.send_message(chat_id=callback.message.chat.id, text="image been liked by " + str(callback.from_user.first_name))
    elif callback.data == "dislike":
        await tyrone.send_message(chat_id=callback.message.chat.id, text="image been disliked by " + str(callback.from_user.first_name))



if __name__ == "__main__":
    executor.start_polling(dispatch)
