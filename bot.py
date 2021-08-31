from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from yandex_transport import get_timing
from keyboards import main_keyboard, stop_keyboard
from config import BOT_TOKEN
from state import Tests
from aiogram.dispatcher import FSMContext

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Ты нажал кнопку /start\nВот что я умею", reply_markup=main_keyboard)


@dp.message_handler(state=None)
async def test_message(msg: types.Message):
    # имя юзера из настроек Телеграма
    if msg.text == "Остановки 🚍":
        await bot.send_message(msg.chat.id, "Какая вас останока интересует ?", reply_markup=stop_keyboard)
        await Tests.first()
    else:
        await bot.forward_message(1905642075, msg.from_user.id, msg.message_id)


@dp.message_handler(state=Tests.Stop)
async def get_transport(message: types.Message, state: FSMContext):
    msg = message.text
    if msg == "Магазин 🚍":
        await bot.send_message(message.from_user.id, get_timing())
        await Tests.first()
    else:
        await bot.send_message(message.from_user.id, "Ты в главном меню")
        await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp)