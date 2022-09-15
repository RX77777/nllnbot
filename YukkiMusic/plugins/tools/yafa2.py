from utlis.send import send_msg, BYusers, GetLink,Name,Glang,getAge
from utlis.tg import Bot
import threading, requests, time, random, re, json, datetime
import importlib
from os import listdir
from os.path import isfile


if text == "عدد الكروب" and (rank is not False or rank is not  0 ):
      from pyrogram.raw.functions.channels import GetFullChannel
      chat = client.resolve_peer(chatID)
      full_chat = client.send(GetFullChannel(channel=chat)).full_chat
      Bot("sendMessage",{"chat_id":chatID,"text":r.gpinfo.format(message.chat.title,full_chat.participants_count,full_chat.admins_count,full_chat.kicked_count,full_chat.banned_count,message.message_id),"reply_to_message_id":message.message_id,"parse_mode":"html","disable_web_page_preview":True})
    if text == c.ID and not redis.sismember("{}Nbot:IDSend".format(BOT_ID),chatID) and not message.reply_to_message:
      Ch = True
      t = IDrank(redis,userID,chatID,r)
      msgs = (redis.hget("{}Nbot:{}:msgs".format(BOT_ID,chatID),userID) or 0)
      edits = (redis.hget("{}Nbot:{}:edits".format(BOT_ID,chatID),userID) or 0)
      rate = int(msgs)*100/20000
      age = getAge(userID,r)
      if redis.hget("{}Nbot:SHOWid".format(BOT_ID),chatID):
        tx = redis.hget("{}Nbot:SHOWid".format(BOT_ID),chatID)
        rep = {"#age":"{age}","#name":"{name}","#id":"{id}","#username":"{username}","#msgs":"{msgs}","#stast":"{stast}","#edits":"{edits}","#rate":"{rate}","{us}":"{username}","#us":"{username}"}
        for v in rep.keys():
          tx = tx.replace(v,rep[v])
      else:
        tx = r.IDnPT
      if not redis.sismember("{}Nbot:IDSendPH".format(BOT_ID),chatID):
        get = Bot("getUserProfilePhotos",{"user_id":userID,"offset":0,"limit":1})
        if get["ok"] == False: 
          Ch = True
        elif get["result"]["total_count"] == 0:
          Ch = True
        else:
          Ch = False
          file_id = get["result"]["photos"][0][0]["file_id"]
          Bot("sendPhoto",{"chat_id":chatID,"photo":file_id,"caption":tx.format(username=("@"+username or "None"),id=userID,stast=t,msgs=msgs,edits=edits,age=age,rate=str(rate)+"%"),"reply_to_message_id":message.message_id,"parse_mode":"html"})
      if Ch == True:
        Bot("sendMessage",{"chat_id":chatID,"text":tx.format(username=("@"+username or "None"),id=userID,stast=t,msgs=msgs,edits=edits,age=age,rate=str(rate)+"%"),"reply_to_message_id":message.message_id,"parse_mode":"html"})
