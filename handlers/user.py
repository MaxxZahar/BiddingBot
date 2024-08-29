from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.state import default_state, State, StatesGroup
from lexicon.lexicon import LEXICON
from data.data import users
from states.states import FSMTrainingStates

router = Router()


@router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message):
    if message.from_user.id not in users:
        users[message.from_user.id] = {}
    await message.answer(LEXICON[message.text])


@router.message(CommandStart(), ~StateFilter(default_state))
async def process_start_in_training_command(message: Message):
    await message.answer(LEXICON['interruption?'])


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON[message.text])


@router.message(Command(commands='crazy'), StateFilter(default_state))
async def process_crazy_command(message: Message, state: FSMContext):
    await message.answer(LEXICON[message.text])
    await state.set_state(FSMTrainingStates.crazy)


@router.message(Command(commands='stop'), StateFilter(default_state))
async def process_stop_default_command(message: Message):
    await message.answer(LEXICON['nothing_to_stop'])


@router.message(Command(commands='stop'), ~StateFilter(default_state))
async def process_stop_in_training_command(message: Message, state: FSMContext):
    await message.answer(LEXICON[message.text])
    await state.clear()
