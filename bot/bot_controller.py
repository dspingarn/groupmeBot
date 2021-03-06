class BotController:

    GREETING_WORDS = ['hello', 'hi', 'hey']
    BOT_NAME = 'foodbot'

    def __init__(self):
        pass

    def process_message(self, recd_msg):
        msg_to_send = {}

        text = recd_msg['text'].lower()

        # helper function that returns true if the given word is in the word list
        # the word list is parameter for calling used_any()
        used_any = lambda word_list: any(map(lambda x : x in text, word_list))

        if BotController.BOT_NAME in text and used_any(BotController.GREETING_WORDS):
            msg_to_send['text'] = 'Hello there, ' + recd_msg['author'] + '!'
        elif 'help' in text:
            msg_to_send['text'] = 'No help for you!'
        else:
            msg_to_send['text'] = 'I\'m sorry, my responses are limited. You must ask the right questions.'

        return msg_to_send
