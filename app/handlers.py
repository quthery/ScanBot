from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from random import randint as rn
from app.generate import answer_physics
from app.scan_img import scan_image
import app.keyboards as kb
import os






router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет {message.from_user.first_name} \nэто ГДЗ бот где ты сможешь отправить фото \nи получить ответ на разные вопросы по категории',
                         reply_markup=kb.main)

@router.message(F.photo)
async def get_photo(message: Message) -> None:
    filename = f'images/{rn(1, 949888)}.jpg'
    await message.photo[-1].bot.download(file=message.photo[-1].file_id, destination=filename)
    text = await scan_image(filename)
    print(text)
    response = await answer_physics(text) 
    print(response)
    await message.bot.send_message(message.from_user.id, text=response)
    os.remove(f"/ScanBot/{filename}")
    





