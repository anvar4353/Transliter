
import logging


from aiogram import Bot, Dispatcher, executor, types
from config import *
from buttons import *
from aiogram.types import Message,CallbackQuery
from googletrans import Translator


logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
translator = Translator()




@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    javob = f'*Mualif: Alikuziyev Anvar \nAssalom alekum {message.from_user.first_name}\nBizning Telegram Translator \nbotimizga xush kelibsiz🤩🥳*'
    javob+='*\niltimos soz yoki matin kiriting👇*'
    await message.reply(javob,parse_mode='markdown')



 
@dp.message_handler()
async def echo(message: types.Message):
    global full
    full = message.text
    await message.answer('*Tilni tanlang!*',parse_mode='markdown',reply_markup=til)




@dp.callback_query_handler(text='english')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='en')
    await call.message.answer(res.text)





@dp.callback_query_handler(text='russian')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='ru')
    await call.message.answer(res.text)





@dp.callback_query_handler(text='uzbek')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='uz')
    await call.message.answer(res.text)





@dp.callback_query_handler(text='afrikaans')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='af')
    await call.message.answer(res.text)


@dp.callback_query_handler(text='albanian')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='sq')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='amharic')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='am')
    await call.message.answer(res.text)


@dp.callback_query_handler(text='arabic')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='ar')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='armenian')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='hy')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='azerbaijani')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='az')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='basque')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='eu')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='belarusian')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='be')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='bengali')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='bn')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='bosnian')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='bs')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='bulgarian')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='bg')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='catalan')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='ca')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='cebuano')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='ceb')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='chichewa')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='ny')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='chinese (simplified)')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='zh-cn')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='chinese (traditional)')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='zh-tw')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='corsican')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='co')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='croatian')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='hr')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='czech')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='cs')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='danish')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='da')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='dutch')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='nl')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='esperanto')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='eo')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='estonian')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='et')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='filipino')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='tl')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='finnish')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='fi')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='french')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='fr')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='frisian')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='fy')
    await call.message.answer(res.text)




@dp.callback_query_handler(text='galician')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='gl')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='georgian')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='ka')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='german')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='de')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='greek')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='el')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='gujarati')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='gu')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='haitian creole')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='ht')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='hausa')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='ha')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='hawaiian')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='haw')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='hebrew')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='iw')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='hebreww')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='he')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='hindi')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='hi')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='hmong')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='hmn')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='hungarian')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='hu')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='icelandic')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='is')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='igbo')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='ig')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='indonesian')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='id')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='irish')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='ga')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='italian')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='it')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='Japanese')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='ja')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='javanese')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='jw')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='kannada')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='kn')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='kazakh')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='kk')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='khmer')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='km')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='korean')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='ko')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='kurdish')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='ku')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='kyrgyz')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='ky')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='lao')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='lo')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='latin')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='la')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='latvian')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='lv')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='lithuanian')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='lt')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='luxembourgish')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='lb')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='macedonian')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='mk')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='malagasy')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='mg')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='malay')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='ms')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='malayalam')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='ml')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='maltese')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='mt')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='maori')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='mi')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='marathi')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='mr')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='mongolian')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='mn')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='myanmarb (burmese)')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='my')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='nepali')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='ne')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='norwegian')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='no')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='odia')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='or')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='pashto')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='ps')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='persian')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='ps')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='polish')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='pl')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='portuguese')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='pt')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='punjabi')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='pa')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='romanian')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='ro')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='samoan')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='sm')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='scots gaelic')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='gd')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='serbian')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='sr')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='sesotho')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='st')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='shona')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='sn')
    await call.message.answer(res.text)


@dp.callback_query_handler(text='sindhi')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='sd')
    await call.message.answer(res.text)


@dp.callback_query_handler(text='sinhala')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='si')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='slovak')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='sk')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='slovenian')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='sl')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='somali')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='so')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='spanish')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='es')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='sundanese')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='su')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='swahili')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='sw')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='swedish')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='sv')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='tajik')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='tg')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='tamil')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='ta')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='telugu')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='te')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='thai')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='th')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='turkish')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='tr')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='ukrainian')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='uk')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='urdu')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='ur')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='uyghur')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='ug')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='vietnamese')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='vi')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='welsh')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='cy')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='xhosa')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='xh')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='yiddish')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='yi')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='yoruba')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='yo')
    await call.message.answer(res.text)



@dp.callback_query_handler(text='zulu')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(full,dest='zu')
    await call.message.answer(res.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

