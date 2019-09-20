Alpha Demo Bot
======

This is the first bot I'm making to interact with groupme.
http://www.apnorton.com/blog/2017/02/28/How-I-wrote-a-Groupme-Chatbot-in-24-hours/ for original bot 

Local Testing
-------------

Since I was tired of continually deploying broken stuff to Heroku, I wrote a small bot client in CLI; the process for local running is:

```
$ source debug_setup.sh # unix only
$ set DEBUG=1 # windows only, space/case sensitive
$ gunicorn app:app --log-file bot.log & # Run botserver in background, only for unix
$ waitress-serve --listen=*:8000 app:app # the first parameter is app.py in app:app
$ python3 bot_cli.py # Run CLI for sending messages to bot
```

It's a little hacky (the botserver determines if it's in debug mode and prints responses instead of sending them back over HTTP), but it works and is good enough for simple tests.

data looks like
{
  "attachments": [],
  "avatar_url": "http://i.groupme.com/123456789",
  "created_at": 1302623328,
  "group_id": "1234567890",
  "id": "1234567890",
  "name": "John",
  "sender_id": "12345",
  "sender_type": "user",
  "source_guid": "GUID",
  "system": false,
  "text": "Hello world ☃☃",
  "user_id": "1234567890"
}