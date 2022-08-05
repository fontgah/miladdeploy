#!/usr/bin/env python
# -*- coding: utf-8 -*-
import script
import requests
from telegram.utils.request import Request
# from telegram.ext import MessageHandler, Filters
# from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
import json
from telegram.ext import Updater, CommandHandler
from telegram import Update,Bot,ParseMode 
from telegram.ext import CallbackContext 
from telegram.ext import (Updater,CommandHandler,MessageHandler,MessageFilter,Filters)
import os 
from data import token,app_name
PORT = int(os.environ.get('PORT', '8443'))
Token = token
print('milad is here ')
test_bot_url = 'https://api.telegram.org/bot' + Token + '/getme'
adminuserid = ['5331124033']
shutte = []
import logging
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
logger = logging.getLogger(__name__)
# try:
#     test_bot = requests.get(test_bot_url)
#     data = json.loads(test_bot.text)
#     parsing1 = data['result']
#     parsing2 = parsing1['username']
#     print('[*] Test Your Token Bot ... \n[*] Bot is OK . username Of Bot Is : ' + parsing2 + '\n[*]Bot Run!')
# except:
#     print('[!]Error! \n[*]Check Your Connection\n[*]Check Your Token.')
#     exit()


def check(link):
    if 'uploadboy.' in link:
        return 'uploadboy'
    if 'drive.google.com' in link:
        return 'google'
    else:
        return 'leech'


def start(update, context):
    bot = context.bot
    try:
        b = [['لیچر', 'تماس']]
        bot.sendMessage(update.message.chat_id, text='<b>Welcome</b>', parse_mode='HTML',
                        reply_markup=ReplyKeyboardMarkup(keyboard=b, resize_keyboard=True))
    except Exception as f:
        print(str(f))


def leech(update, context):
    bot = context.bot
    try:
        b = [['لیچر', 'تماس'], ['وضعیت سایت ها']]
        print(update.message.chat_id, ' Send Message || Message : ' + str(update.message.text))
        if str(update.message.chat_id) in adminuserid:
            if 'برگشت' == update.message.text:
                try:
                    b = [['لیچر', 'تماس'], ['وضعیت سایت ها']]
                    bot.sendMessage(update.message.chat_id, text='<b>Main Menu</b>', parse_mode='HTML',
                                    reply_markup=ReplyKeyboardMarkup(keyboard=b, resize_keyboard=True))
                    return ''
                except Exception as f:
                    print(str(f))
            if 'تماس' == update.message.text:
                text = 'جهت پشتیبانی روی دکمه زیر بزنید.'
                keyboard = []
                keyboard.append(
                    [InlineKeyboardButton(text='📩 تماس با پشتیبانی',
                                          url='https://t.me/luiuio')])
                reply_markup = InlineKeyboardMarkup(keyboard)
                bot.sendMessage(update.message.chat_id, text=text, parse_mode='HTML',
                                reply_markup=reply_markup)
                bot.sendMessage(update.message.chat_id, text='<b>Main Menu</b>', parse_mode='HTML',
                                reply_markup=ReplyKeyboardMarkup(keyboard=b, resize_keyboard=True))
                return ''
            if update.message.text == 'وضعیت سایت ها':
                text = '''<b>💡 لیست سایت های فعال:</b>
                <a href="https://test.com">test</a>              
                '''
                b = [['برگشت']]
                bot.sendMessage(update.message.chat_id, text=text, parse_mode='HTML',
                                reply_markup=ReplyKeyboardMarkup(keyboard=b, resize_keyboard=True))
                return ''
            if update.message.text == 'لیچر':
                b = [['برگشت']]
                text = 'لینک خود را ارسال کنید.'
                bot.sendMessage(update.message.chat_id, text=text, parse_mode='HTML',
                                reply_markup=ReplyKeyboardMarkup(keyboard=b, resize_keyboard=True))
                return ''
            if '\n' in update.message.text and check(
                    update.message.text) == 'leech' and 'pik.com' not in update.message.text and 'http' in update.message.text:
                l = str(update.message.text).split('\n')
                for i in l:
                    p = script.leecher(link=i)
                    if p == 'Link Is Deleted':
                        bot.sendMessage(update.message.chat_id, text='<b>Your Link Is Deleted</b>', parse_mode='HTML')
                    if p != 'Link Is Deleted':
                        text = '<b>Size:</b> ' + p['size'] + '\n<b>Name:</b> ' + p['name'] + '\n<b>Link:</b> \n' + p[
                            'link']
                        bot.sendMessage(update.message.chat_id, text=text, parse_mode='HTML')
                return ''


            
            if '\n' not in update.message.text and check(
                    update.message.text) == 'leech' and 'freepik.com' not in update.message.text and 'http' in update.message.text:
                p = script.leecher(link=update.message.text)

                if p == 'Link Is Deleted':
                    bot.sendMessage(update.message.chat_id, text='<b>Your Link Is Deleted</b>', parse_mode='HTML')
                if p != 'Link Is Deleted':
                    text = '<b>Size:</b> ' + p['size'] + '\n<b>Name:</b> ' + p['name'] + '\n<b>Link:</b>\n' + p['link']
                    bot.sendMessage(update.message.chat_id, text=text, parse_mode='HTML')
                return ''
            if 'uploadboy.' in update.message.text:
                message = update.message.text
                i = json.loads(requests.post('https://test.com',
                                             json={'key': '767a8f92',
                                                   'link': message},
                                             timeout=10).text)
                l = '✅<b>Your UploadBoy Link Leeched.</b>\n<b>Download Link:</b> ' + \
                    '\n\n<code>' + i['link'] + '</code>\n@luiuio'
                bot.sendMessage(update.message.chat_id,
                                text=l,
                                parse_mode='HTML', reply_markup=ReplyKeyboardMarkup(keyboard=b))
                return ''
            if 'drive.google.com' in update.message.text:
                l = script.googledrive(update.message.text)
                bot.sendMessage(update.message.chat_id, text=l, parse_mode='HTML',
                                reply_markup=ReplyKeyboardMarkup(keyboard=b))
                return ''
            bot.sendMessage(update.message.chat_id, text='<b>پیام شما نامعتبر است.</b>', parse_mode='HTML',
                            reply_markup=ReplyKeyboardMarkup(keyboard=b, resize_keyboard=True))
            return ''
        bot.sendMessage(update.message.chat_id, text='<b>پیام شما نامعتبر است.</b>', parse_mode='HTML',
                        reply_markup=ReplyKeyboardMarkup(keyboard=b, resize_keyboard=True))
        return ''

    except Exception as f:
        pass






def main(): 
   TOKEN = token 
   APP_NAME=app_name 
   req = Request(connect_timeout = 0.5) 
   t_bot = Bot(request=req,token = TOKEN) 
   updater = Updater(bot = t_bot ,use_context = True)     
   dp = updater.dispatcher 
   dp.add_handler(CommandHandler("start", start))
   dp.add_handler(MessageHandler(Filters.text, leech))
   updater.start_webhook(listen="0.0.0.0",port=PORT,url_path=TOKEN,webhook_url=APP_NAME + TOKEN) 
   updater.idle() 
  
if __name__=='__main__': 
   main()




















