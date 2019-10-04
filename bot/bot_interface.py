from bot.bot_controller import BotController

class BotInterface:
  # Uses a bot object to initialize itself

  def __init__(self):
    self.bot = BotController()

  # process_message
  #   msg : dictionary
  #    has keys "author", "text", and "author_id"
  #   returns new msg dictionary:
  #    (just text key for now)
  def process_message(self, msg):
    msg = self.bot.process_message(msg)

    return msg 
  
  def canned_reply(self, title):
    if title == 'help':
      return {'text': 'No help for you!'}
    else:
      return {'text': 'I\'m sorry, my responses are limited. You must ask the right questions.'}
