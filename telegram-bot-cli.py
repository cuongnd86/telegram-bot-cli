# -*- coding: utf-8 -*-

from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters
import json, sys, datetime, requests, os
from dotenv import load_dotenv;load_dotenv()

class telegram_bot_cli:

    def __init__(self, TOKEN = os.getenv('TOKEN')):
        # create .env file. add value for TOKEN, id, username
        self.TOKEN    = TOKEN
        self.id       = os.getenv('id')
        self.username = os.getenv('username')
    
    def auth(self, id, username):
        rs = False if id != self.id or username != self.username else True
        return rs

    def cli_sender(self, cli):
        cli = str(cli).lower()
        if cli in ['/start','/on']:
            return 'Start bot...'
        if cli in ['time', '/time']:
            return str(datetime.datetime.now())
        return '404'

    def handle_message(self, update: Update, context: CallbackContext):
        text = str(update.message.text).lower()
        rs   = self.cli_sender(text)
        return update.message.reply_text(rs)
    
    def info_command(self, update: Update, context: CallbackContext):
        user = update.effective_user
        update.message.reply_text(f'id: {user.id} - username: {user.username} - first_name: {user.first_name} - last_name: {user.last_name}')
    
    def help_command(self, update: Update, context: CallbackContext):
        menu  = '''*Bot Menu Management*
        
*/help:*  Hướng dẫn sử dụng
*/start:* Bắt đầu sử dụng
*/info:*  Thông tin tài khoản
'''
        return update.message.reply_text(text=menu, parse_mode=ParseMode.MARKDOWN)
    
    def main(self):
        updater = Updater(self.TOKEN)
        dp      = updater.dispatcher
        dp.add_handler(CommandHandler('help', self.help_command))
        dp.add_handler(CommandHandler('info', self.info_command))
        dp.add_handler(MessageHandler(Filters.text, self.handle_message))
        updater.start_polling()
        updater.idle()

if __name__ == '__main__':
    telegram_bot_cli = telegram_bot_cli()
    telegram_bot_cli.main()