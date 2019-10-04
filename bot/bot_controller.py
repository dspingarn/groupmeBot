class BotController:

    GREETING_WORDS = ['hello', 'hi', 'hey']
    BOT_NAME = 'alpha-demo-bot'

    def __init__(self):
        pass

    def process_message(self, recd_msg):
        msg_to_send = {}

        text = recd_msg['text'].lower()

        # helper function that returns true if the given word is in the word list
        # the word list is parameter for used_any()
        used_any = lambda word_list: any(map(lambda x : x in text, word_list))

        if BotController.BOT_NAME in text and used_any(BotController.GREETING_WORDS):
            msg_to_send['text'] = 'Hello there, ' + recd_msg['name'] + '!'
        elif 'text' == 'help':
            msg_to_send['text'] = 'No help for you!'
        else:
            msg_to_send['text'] = 'Echo: ' + recd_msg['text']

        return msg_to_send
