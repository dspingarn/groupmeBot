from bot.bot_controller import BotController

class BotInterface:
  # Fields:
  #  - bot
  # 

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