import  logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1906077847:AAFbW5_IBxesgM4hcKzX3m8-h4UyVsDSHRE'
wikipedia.set_lang('uz')

logging.basicConfig(level=logging.INFO)

bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Wikipedia botiga xush kelibsiz...")

@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid ma'lumot topilmadi.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)