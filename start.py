from telethon import TelegramClient, events, Button
import requests
import os
import random
from src import src
#from telethon.tl.types import PeerChat

client = TelegramClient('anfghohn', int(os.environ.get("APP_ID" )), os.environ.get("API_HASH")).start(bot_token= os.environ.get("TG_BOT_TOKEN"))
@client.on(events.NewMessage(pattern='/start'))
async def handler(event):
    chat = await event.get_chat()
    await client.send_message(chat,""" 💁 Join \n\n@tamil_girls_boys_chatting_group""")
    
@client.on(events.ChatAction)
async def handler2(event):
    # Welcome every new user
    if event.user_joined:
        markup = client.build_reply_markup(Button.url("💖 Share 💖",tg://msg?text=%2A%2AHai%20%E2%9D%A4%EF%B8%8F%2C%2A%2A%20%0AToday%20i%20just%20found%20out%20an%20intresting%20Group%20for%20Free%F0%9F%A5%B0.%20%20%0A%2A%2AChatting%20Link%20%3A%20%40tamil_girls_boys_chatting_group%2A%2A%20%F0%9F%94%A5))
        await event.reply('Welcome to the group!', buttons=markup)

@client.on(events.NewMessage(chats=[-1001375180691]))
async def handler3(event):
        # Reference for retrieve all posts from Blogger   --->  https://blogname.blogspot.com/feeds/posts/default?alt=json-in-script&callback=myFunc
        #with open("backup.json", "r", encoding="utf8") as f:
        #          b_json = json.load(f)
        chat = await event.get_chat()
        value = []
        images = random.choice(src["feed"]["entry"])
        get_links = []
        get_title = images["title"]["$t"]
        see_more = images["link"][3]["href"]
        post = images["content"]["$t"]
        for i in post.split('"'):
          if ".jpg" in i:
                value.append(i)
          if ".png" in i:
                value.append(i)
        for links in value:
                link = links
                get_links.append(link)
        await client.send_file(chat,random.choice(get_links).replace("\/", "/"),caption = "{}\n\nSee more at {}".format(get_title, see_more.replace("\/", "/")))
        return
    #with open("backup.json", "w", encoding="utf8") as outfile:
    #          json.dump(b_json, outfile, ensure_ascii=False)
    #await client.send_message(chat,"backup finished")
    #await client.send_message(chat,count)
    #return
    #await client.send_file(chat,r1["image_url"],caption = r1["title"])
    #markup = client.build_reply_markup(Button.url("stream",urls.stream_baseurl+g1))
    #sr = requests.get("src.xml")
    #await client.send_message(sr)
    #try:
    #  await client.send_file(chat,"https://1.bp.blogspot.com/-LU7wiyBQ54U/X62XOZNZsYI/AAAAAAAAIr8/zcrp5JWSxKoGtO_hUE2jue7E0wcqDbU6ACLcBGAsYHQ/s1200/YeQIGEd.jpg",caption = "Original Quality available only at www.actressanddivas.tk")
    #except:
    #  pass
    #await client.send_message(chat, "support @urlicupload    "+" TITLE:"+r1["title"]+"   DESCRIPTION:"+r1["description"],file=r1["image_url"], buttons=markup)
            
            #rgx = w
   # await client.send_message(chat, g1)
   #await client.send_message(chat,"445")
    
    
    
    
    
client.start()
client.run_until_disconnected()
