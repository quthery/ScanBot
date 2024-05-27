from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from random import randint as rn
from app.generate import answer_physics
from app.scan_img import scan_image
from app.get_new_file import last_modified_file
import app.keyboards as kb
import os






router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет {message.from_user.first_name} \nэто ГДЗ бот где ты сможешь отправить фото \nи получить ответ на разные вопросы по категории',
                         reply_markup=kb.main)

@router.message(F.photo)
async def get_photo(message: Message) -> None:
    await message.answer("По какому предмету тебе нужно решить задачу?", reply_markup=kb.answer)
    filename = f'images/{rn(1, 949888)}.jpg'
    await message.photo[-1].bot.download(file=message.photo[-1].file_id, destination=filename)

@router.callback_query(F.data == "Physics")
async def photo(callback: CallbackQuery):
    filename = last_modified_file(os.path.abspath('images'))
    text = await scan_image(filename)
    response = await answer_physics(text) 
    await callback.message.edit_text(response)
    os.remove(filename)






