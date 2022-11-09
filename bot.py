# coding: utf-8

from os import environ
from dotenv import load_dotenv

from telegram import (
  Update,
) 
from telegram.ext import (
  CallbackContext,
  CommandHandler,
  Filters,
  MessageHandler,
  Updater,
)

# Loads .env file to environ, after that we can read the variables from .env
load_dotenv()

TG_TOKEN = environ['TG_TOKEN']


# -----------------------------------------------------------------------------
# Utils

def update_get_ids(update: Update):
  """Return chat_id, user_id and message_id if they exist."""
  chat_id = update.effective_chat.id
  user_id = update.effective_user.id
  message_id = update.effective_message.message_id

  return chat_id, user_id, message_id


# -----------------------------------------------------------------------------
# Command and message handlers

# Update documentation: https://docs.python-telegram-bot.org/en/latest/telegram.update.html
# CallbackContext documentation: https://docs.python-telegram-bot.org/en/latest/telegram.ext.callbackcontext.html

def start(update: Update, context: CallbackContext):
  msg = 'Hi! I\'m a sample bot. Edit the <code>bot.py</code> file and reload the bot to change me.\n\nTry the /test command either with some text or without text to see an example of that, or send a text message for another example.'
  update.message.reply_html(msg)

def example_command(update: Update, context: CallbackContext):
  # No argument?
  if (len(context.args) == 0):
    update.message.reply_text('No text given after the command.')
    return

  word = context.args[0].lower()

  # Example of logging to terminal and formatting a string programmatically
  print(f'Example command args: {context.args}, first arg lowercased: {word}')

  update.message.reply_text(f'The first word after the command was {word}.')

def message_handler(update: Update, context: CallbackContext):
  # Get chat id and user id, discard message id that is also returned by the function
  chat_id, user_id, _ = update_get_ids(update)
  
  msg = f'The message was sent to chat {chat_id} by user {user_id}.'

  update.message.reply_text(msg)


# -----------------------------------------------------------------------------
# Main loop

def main():
  updater = Updater(TG_TOKEN, use_context=True)
  
  # Add handlers to commands and messages
  dp = updater.dispatcher

  dp.add_handler(CommandHandler("start", start))
  dp.add_handler(CommandHandler("test", example_command))
  dp.add_handler(MessageHandler(Filters.text, message_handler))

  # Poll for new messages and commands every second
  updater.start_polling(poll_interval=1.0)


main()
