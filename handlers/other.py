from aiogram import Router
from aiogram.types import Message
from data.data import users
from lexicon.lexicon import LEXICON
import logging

router = Router()

@router.message()
async def process_unknown_message(message: Message):
    logging.debug(users)
    await message.answer(LEXICON['unknown_command'])