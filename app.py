import os
import sys
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

from bot.bot_interface import BotInterface

app = Flask(__name__)
bi  = BotInterface()
BOT_NAME = bi.bot.BOT_NAME

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  print(data)

  # Don't reply to self, and must mention the bot
  if data['name'] != BOT_NAME and BOT_NAME in data['text'].lower():
    msg = {}
    msg['author']    = data['name']
    msg['author_id'] = data['sender_id']
    msg['text']      = data['text']

    reply = bi.process_message(msg)
    if reply:
      send_message(reply['text'])

  return "ok", 200

def send_message(msg):
  if os.environ['DEBUG'] == '1':
    print('[Alpha Bot]: ' + msg)
    return

  # for non-debug purposes
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : os.getenv('GROUPME_BOT_ID'),
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()
