from telethon import TelegramClient, events, Button
import requests
from headers import headers
import urls
import os
#from flask import request

client = TelegramClient('anfghohn', int(os.environ.get("APP_ID" )), os.environ.get("API_HASH")).start(bot_token= os.environ.get("TG_BOT_TOKEN"))
@client.on(events.NewMessage(pattern='/start'))
async def handler(event):
    chat = await event.get_chat()
    await client.send_message(chat,"""💁Hey, \n\n    I am Simple Auto Posting Bot
    Simply start and give me some time I will send you random pics, you can also add me in your groups.""")
    #await client.send_message(chat,"""https://1.bp.blogspot.com/-LU7wiyBQ54U/X62XOZNZsYI/AAAAAAAAIr8/zcrp5JWSxKoGtO_hUE2jue7E0wcqDbU6ACLcBGAsYHQ/s1200/YeQIGEd.jpg""")

@client.on(events.NewMessage(pattern='hi'))
async def handler2(event):
    
    chat = await event.get_chat()
    #await client.send_file(chat,r1["image_url"],caption = r1["title"])
    #markup = client.build_reply_markup(Button.url("stream",urls.stream_baseurl+g1))
    await client.send_photo(chat, photo="https://1.bp.blogspot.com/-LU7wiyBQ54U/X62XOZNZsYI/AAAAAAAAIr8/zcrp5JWSxKoGtO_hUE2jue7E0wcqDbU6ACLcBGAsYHQ/s1200/YeQIGEd.jpg")
    #await client.send_message(chat, "support @urlicupload    "+" TITLE:"+r1["title"]+"   DESCRIPTION:"+r1["description"],file=r1["image_url"], buttons=markup)
            
            #rgx = w
   # await client.send_message(chat, g1)
   #await client.send_message(chat,"445")
    
#@client.on(events.NewMessage(pattern='(?i)https://www.mxplayer.in'))
async def handler(event):
    link =event.text.split('/')[-1]
    video_d = "https://llvod.mxplay.com/"
    A =requests.get("https://api.mxplay.com/v1/web/detail/video?type=movie&id="+link+"&platform=com.mxplay.desktop&device-density=2&userid=30bb09af-733a-413b-b8b7-b10348ec2b3d&platform=com.mxplay.mobile&content-languages=hi,en,ta").json()
    chat = await event.get_chat()
    markup = client.build_reply_markup(Button.url("stream",video_d+A["stream"]['hls']['high']))
    await client.send_message(chat," support @urlicupload   "+A["title"],buttons=markup)
    print(A)
    print(link)
#@client.on(events.NewMessage(pattern='(?i)https://www.hotstar.com/in/'))
async def handler(event):
    link =event.text
    print(link)
    #import youtube_dl
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})
    with ydl:
        result = ydl.extract_info(
        link,
        download=True # We just want to extract the info
    )
    await client.send_message(chat,result)
    
@client.on(events.NewMessage(pattern='(?i)/ls'))
async def handler(event):
    link =event.text.split(" ")[1]
    e = os.listdir(link)
    chat = await event.get_chat()
    c = "|"
    #str1.join(s)
    #print(c)
    await client.send_message(chat,c.join(e))
@client.on(events.NewMessage(pattern='(?i)sm'))
async def handler(event):
    link =event.text.split(" ")[1]
    print(link)
    chat = await event.get_chat()
    await client.send_file(chat, '/Download'+link,force_document=True)
    
    
    
    
client.start()
client.run_until_disconnected()
