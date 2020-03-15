# Test GroupMe Bot

This is the first bot I'm making to interact with groupme.
http://www.apnorton.com/blog/2017/02/28/How-I-wrote-a-Groupme-Chatbot-in-24-hours/ for original bot

### \*I will no longer be adding new features to this repo, but will update dependencies if needed.\*  

## Local Testing

Run the local client: 

```
$ source debug_setup.sh # unix only
$ set DEBUG=1 # windows only, space/case sensitive
$ waitress-serve --listen=*:8000 app:app # the first parameter is app.py in app:app
$ python bot_cli.py # Run CLI for sending messages to bot
```
You may wish to  
1. use a virtual envrionment (need to run source /env/Scripts/activate, or maybe just env/Scripts/activate.bat depending on OS)
2. use a different python wsgi server besides waitress, but waitress works well on windows (a gunicorn example might be the following)
```
$ gunicorn app:app --log-file bot.log & # Run botserver in background
```
You can use :quit to exit the cli successfully at any time while the server is running.  


sample data payload looks like:  
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
