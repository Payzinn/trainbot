from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import keyboards

router = Router()


class Reg(StatesGroup):
    name = State()
    number = State()

@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.reply(f"Привет, твой ID: {message.from_user.id}\nИмя {message.from_user.full_name}", reply_markup= keyboards.another)

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("Команда /help")

@router.message(F.text == "Как дела?")
async def cmd_hay(message: Message):
    await message.answer("Норм а у тебя как")


@router.message(F.photo)
async def cmd_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')


@router.message(Command('get_photo'))
async def cmd_getphoto(message: Message):
    await message.answer_photo(photo = "AgACAgIAAxkBAAMZZzGmqKIIzwK1XZcqJwP9uaPO7F0AAuXjMRvbgJBJ4afjSkhYt7kBAAMCAAN5AAM2BA",
                               caption='Это кот')

@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer('Вы выбрали каталог', show_alert=True)
    await callback.message.edit_text("Привет!", reply_markup = await keyboards.inline_cars())

@router.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer("Введите ваше имя.")

@router.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer("Введите номер")

@router.message(Reg.number)
async def reg_three(message: Message, state: FSMContext):
    await state.update_data(number = message.text)
    data = await state.get_data()
    await message.answer(f"Регистрация завершена.\nName: {data['name']}\nNumber: {data['number']}")
    await state.clear()
    print(data)