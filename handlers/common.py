from random import randint

from aiogram import Router, types, F
from aiogram.filters.command import Command

from keyboards.keyboards import kb1, kb2
from utils.random_fox import fox

router = Router()


@router.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer("Привет! Я эхобот на aiogram 3. Отправь мне любое сообщение, и я повторю его.",
                         reply_markup=kb1)


@router.message(Command("ура"))
async def send_ura(message: types.Message):
    await message.answer("УРАААА! Я эхобот на aiogram 3. Отправь мне любое сообщение, и я повторю его.",
                         reply_markup=kb2)


@router.message(Command("fox"))
@router.message(Command("лиса"))
async def send_fox(message: types.Message):
    image_fox = fox()
    await message.answer_photo(image_fox)
    # await bot.send_photo(message.chat.id, image_fox)
    # await message.answer(f"{image_fox}")


@router.message(F.text.lower() == 'num')
async def send_random(message: types.Message):
    number = randint(1, 10)
    await message.answer(f"{number}")


@router.message(F.text)
async def echo(message: types.Message):
    if "ура" in message.text:
        await message.answer("УРАААА!")
    elif message.text == "инфо":

        user_name = message.chat.id
        print(user_name)
        await message.answer(str(user_name))
    else:
        await message.answer(message.text)
