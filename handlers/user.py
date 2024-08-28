from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart, StateFilter
from lexicon.lexicon import LEXICON
from data.data import users

router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    if message.from_user.id not in users:
        users[message.from_user.id] = {}
    await message.answer(LEXICON[message.text])