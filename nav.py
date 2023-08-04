
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnLogin = KeyboardButton('👤')
btnConfTo = KeyboardButton('⚙️')
btnGo = KeyboardButton('▶️')
btnStop = KeyboardButton('⏸')
btnInform = KeyboardButton('📑')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnLogin, btnConfTo,btnGo,btnStop,btnInform)
