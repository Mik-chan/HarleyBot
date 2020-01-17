# -*- coding: utf-8 -*-
import vk_api.vk_api
from vk_api.bot_longpoll import VkBotLongPoll,VkBotEventType
from vk_api import audio
import random
import json
from bs4 import BeautifulSoup as bs
import requests

CHAT_ID_MIN=2000000000 #НЕ МЕНЯТЬ!
CREATOR_ID=537414928 #ИД СОЗДАТЕЛЯ БОТА
RAZR_IDS=[537414928,354162667,544194575,509362493] #ИД РАЗРАБОВ
ADMIN_CONVERSATION=2000000019 #ИД АДМИНСКОЙ БЕСЕДЫ (СЮДА БУДЕТ КИДАТЬ, ЧТО БОТ ЗАПУЩЕН)
ZAM_ID=509115187#ИД ЗАМА СОЗДАТЕЛЯ БОТА
LEHA_ID=384832146
SEMA_ID=359566499
MUSA_ID=509115187
ALEN_ID=502182497
MILA_ID=377289572
class harli:
    def __init__(self,api_token,group_id,login,password,music_id,user_token): #НЕ МЕНЯТЬ!
        self.vk=vk_api.VkApi(token=api_token)
        self.long_poll=VkBotLongPoll(self.vk,group_id)
        self.vk_api=self.vk.get_api()
        self.user_vk_session=vk_api.VkApi(login=login,password=password)
        self.user_vk_session.auth()
        self.user_vk=self.user_vk_session.get_api()
        self.vk_audio=audio.VkAudio(self.user_vk_session)
        self.user_vk_for_video=vk_api.VkApi(token=user_token).get_api()

    def sendmsg(self,peer_id,message=None,attachment=None,disable_mentions=None): self.vk_api.messages.send(peer_id=int(peer_id),message=message,attachment=attachment,random_id=random.randint(-2135425010,2135425010),disable_mentions=disable_mentions) #НЕ МЕНЯТЬ!
    def sex(self,user_id): return self.vk_api.users.get(user_ids=user_id,fields='sex')[0]['sex']                                                                                                                                                      #НЕ МЕНЯТЬ!
    def members(self,peer_id): return [item["member_id"] for item in self.vk_api.messages.getConversationMembers(peer_id=peer_id)["items"] if item['member_id']>0]                                                                                    #НЕ МЕНЯТЬ!
    def kick(self,chat_id,member_id): self.vk_api.messages.removeChatUser(chat_id=chat_id,member_id=member_id)                                                                                                                                        #НЕ МЕНЯТЬ!
    def uid(self,screen_name):                                                                                                                                                                                                                        #НЕ МЕНЯТЬ!
        if screen_name.startswith('https://vk.com/'): user=screen_name[15:]
        elif screen_name.startswith('[id'): user=screen_name.split('|')[0][1:]
        elif screen_name.startswith('id'): user=str(screen_name)
        else: user='id'+screen_name
        return self.vk_api.utils.resolveScreenName(screen_name=user)["object_id"]
    def name(self,user_id): return self.vk_api.users.get(user_ids=user_id)[0]['first_name']                                                                                                                                                           #НЕ МЕНЯТЬ!
    def photo(self,url,peer_id):                                                                                                                                                                                                                      #НЕ МЕНЯТЬ!
        session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(max_retries=10)
        session.mount('http://', adapter)
        p=session.request('GET',url,headers={'User-agent':'Mozilla/5.0','Referer':'http://www.python.org/'})
        out=open("img.jpg", "wb")
        out.write(p.content)
        out.close()
        p.close()
        session.close()
        pfile = requests.post(self.vk_api.photos.getMessagesUploadServer(peer_id=peer_id)['upload_url'], files = {'photo': open('img.jpg', 'rb')}).json()
        photo = self.vk_api.photos.saveMessagesPhoto(server = pfile['server'], photo = pfile['photo'], hash = pfile['hash'])[0]
        return 'photo'+str(photo['owner_id'])+'_'+str(photo['id'])



    def start(self):
        users,conversations,info,arts=json.load(open('users.json',encoding='utf-8')),json.load(open('conversations.json',encoding='utf-8')),json.load(open('info.json',encoding='utf-8')),json.load(open('arts.json',encoding='utf-8'))  #Импорт файлов с информацией
        brakzapros={}  #НЕ МЕНЯТЬ, это запросы на браки!
        self.sendmsg(peer_id=ADMIN_CONVERSATION,message="Бот запущен")
        print("бот запущен!")
        while True:
            try:
                for event in self.long_poll.listen():
                    if event.type==VkBotEventType.MESSAGE_NEW and event.object.from_id>0:
                        peer_id,user_id,message=event.object.peer_id,str(event.object.from_id),event.object.text
                        sexinf="а" if self.sex(user_id)==1 else ""
                        if peer_id>CHAT_ID_MIN and str(peer_id-CHAT_ID_MIN) not in conversations.keys():
                            conversations[str(peer_id-CHAT_ID_MIN)]={
                            "chat_id": peer_id-CHAT_ID_MIN,
                            "admins": RAZR_IDS.copy(),
                            "hello": "приветствие не установлено!",
                            "autokick": True,
                            "hentai": True
                            }
                        if user_id not in users.keys():
                            users[user_id]={
                            "user_id": user_id,
                            "name": self.name(user_id), #имя
                            "clan": False,
                            "rank": False,
                            "money": 0, #деньги
                            "wall": False, #ёбнуть
                            "hit": False, #ударить
                            "universe": False, #взорвать вселенную
                            "crusade": False, #крестовый поход
                            "vacuum": False, #пропылесосить
                            "ride": True, #кататься
                            "opidorasit": False, #опидорасить
                            "cut": False, #порезать руки
                            "cat": False, #стать котом
                            "macho": False, #стать мачо
                            "ban": False, #забанить
                            "drink": False, #выпить
                            "kus": False, #кусь
                            "scratch": False, #почесать
                            "fly": False, #полетать
                            "ricardo": False, #рикардо
                            "house": False, #построить дом
                            "rose": False, #подарить розу
                            "showtits": False, #показать сиськи
                            "love": False, #брак
                            "rab": False, #рабовладельчество
                            "banned": False, #забанен ли в беседах
                            "rab_of": False, #является ли рабом, если да, то чьим
                            "yaoy": False, #уничтожить яой
                            "garem": False, #наличие гарема
                            "in_garem": False, #в чьем гареме
                            "hate": False, #ненивидеть
                            "cry": False #расплакаться
                            }
                            self.sendmsg(peer_id=peer_id,message="Приветствую тебя впервые в нашей беседе,твой аккаунт зарегестрирован [id{}|{}]!".format(user_id,users[user_id]['name']))
                        users[user_id]['money']+=1
                        if event.object.action!=None and (event.object.action['type']=='chat_invite_user' or event.object.action['type']=='chat_invite_user_by_link'):
                            if event.object.action['type']=='chat_invite_user':
                                invite_id=event.object.action['member_id']
                            elif event.object.action['type']=='chat_invite_user_by_link':
                                invite_id=event.object.from_id
                            self.sendmsg(peer_id=peer_id,message="[id"+str(user_id)+"|"+users[str(user_id)]['name']+"], "+conversations[str(peer_id-CHAT_ID_MIN)]['hello'])
                        elif event.object.action!=None and event.object.action['type']=='chat_kick_user' and conversations[str(peer_id-CHAT_ID_MIN)]['autokick']==True and user_id==event.object.action['member_id']:
                            try: self.kick(chat_id=peer_id-CHAT_ID_MIN,member_id=user_id)
                            except: pass

                        elif peer_id<CHAT_ID_MIN and int(user_id)!=CREATOR_ID:
                            self.sendmsg(peer_id=peer_id,message="Бот работает только в беседах!")
                        elif message.lower().startswith('харли. ') or message.lower().startswith("харли, ") or message.lower().startswith("harli, ") or message.lower().startswith("harli , "):
                            msg=message[6:]
                            smsg=msg.split()
                            args=msg[len(smsg[0])+1:]
                            if smsg[0]=="use" and int(user_id)==CREATOR_ID:
                                user_id=str(self.uid(smsg[1]))
                                msg=' '.join(smsg[2:])
                                smsg=msg.split()
                                args=msg[len(smsg[0])+1:]


                            elif smsg[0].lower() in ["расплакаться"] and users[user_id]['cry']==True:
                                answer="[id{}|{}] расплакался{}".format(user_id,users[user_id]['name'],sexinf,args)
                                self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts['cry']))

                            if smsg[0].lower() in ["ёбнуть"] and users[user_id]['wall']==True:
                                answer="[id{}|{}] ёбнул{} {}".format(user_id,users[user_id]['name'],sexinf,args)
                                self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts['wall']))

                            elif smsg[0].lower() in ["ударить"] and users[user_id]['hit']==True:
                                answer="[id{}|{}] ударил{} {}".format(user_id,users[user_id]['name'],sexinf,args)
                                self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts['hit']))

                            elif msg.lower() in ["взорвать вселенную"] and users[user_id]['universe']==True:
                                answer="[id{}|{}] взорвал{} вселенную".format(user_id,users[user_id]['name'],sexinf)
                                self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts['universe']))

                            elif msg.lower() in ["уничтожить яой"] and users[user_id]['yaoy']==True:
                                answer="[id{}|{}] уничтожил{} весь яой. Горите в аду, черти".format(user_id,users[user_id]['name'],sexinf,args)
                                self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts['yaoy']))

                            elif smsg[0].lower() in ["ненавидеть"] and users[user_id]['hate']==True:
                                answer="[id{}|{}] ненавидит{} {}".format(user_id,users[user_id]['name'],sexinf,args)
                                self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts['hate']))

                            elif smsg[0].lower() in ["крестовый"] and users[user_id]['crusade']==True:
                                answer="[id{}|{}] устроил{} крестовый поход".format(user_id,users[user_id]['name'],sexinf)
                                self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts['crusade']))

                            elif smsg[0].lower() in ["пропылесосить"] and users[user_id]['vacuum']==True:
                                answer="[id{}|{}] пропылесосил{} {}".format(user_id,users[user_id]['name'],sexinf,args)
                                self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts['vacuum']))

                            elif smsg[0].lower() in ["кататься"] and users[user_id]['ride']==True:
                                answer="[id{}|{}] катается {}".format(user_id,users[user_id]['name'],args)
                                self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts['ride']))

                            elif smsg[0].lower() in ["опидорасить"] and users[user_id]['opidorasit']==True:
                                answer="[id{}|{}] опидорасил{} {}".format(user_id,users[user_id]['name'],sexinf,args)
                                self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts['opidorasit']))

                            elif smsg[0].lower() in ["порезать"] and users[user_id]["cut"]==True:
                                if smsg[1].lower() in ["руки"]:
                                    answer="[id{}|{}] порезал{} руки".format(user_id,users[user_id]['name'],sexinf)
                                    self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts["cut"]))

                            elif smsg[0].lower() in ["стать"]:
                                if smsg[1].lower() in ["котом"] and users[user_id]["cat"]==True:
                                    answer="[id{}|{}] стал{} котом".format(user_id,users[user_id]['name'],sexinf)
                                    self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts["cat"]))
                                if smsg[1].lower() in ["мачо"] and users[user_id]['macho']==True:
                                    answer="[id{}|{}] стал{} мачо".format(user_id,users[user_id]['name'],sexinf)
                                    self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts["macho"]))

                            elif smsg[0].lower() in ["забанить"] and users[user_id]['ban']==True:
                                answer="[id{}|{}] забанил{} {}".format(user_id,users[user_id]['name'],sexinf,args)
                                self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts['ban']))

                            elif msg.lower() in ["напиться до инфаркта"] and users[user_id]['drink']==True:
                                answer="[id{}|{}] напил{} до инфаркта".format(user_id,users[user_id]['name'],('ась' if sexinf=='а' else 'ся'))
                                self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts['drink']))

                            elif smsg[0].lower() in ["кусь"] and users[user_id]['kus']==True:
                                answer="[id{}|{}] укусил{} {}".format(user_id,users[user_id]['name'],sexinf,args)
                                self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts['kus']))

                            elif smsg[0].lower() in ["почесать"] and users[user_id]['scratch']==True:
                                answer="[id{}|{}] почесал{} {}".format(user_id,users[user_id]['name'],sexinf,args)
                                self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts['scratch']))

                            elif smsg[0].lower() in ["полетать"] and users[user_id]['fly']==True:
                                answer="[id{}|{}] летает".format(user_id,users[user_id]['name'])
                                self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts['fly']))

                            elif msg.lower() in ["рикардо"] and users[user_id]['ricardo']==True:
                                answer="[id{}|{}], держи Рикардо!".format(user_id,users[user_id]['name'])
                                self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts['ricardo']))

                            elif msg.lower() in ["построить дом"] and users[user_id]['house']==True:
                                answer="[id{}|{}] построил{} дом".format(user_id,users[user_id]['name'],sexinf)
                                self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts['house']))

                            elif smsg[0].lower() in ["подарить"] and users[user_id]['rose']==True:
                                answer="[id{}|{}] подарил{} {}".format(user_id,users[user_id]['name'],sexinf,args)
                                self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts['rose']))

                            elif smsg[0].lower() in ["показать"] and users[user_id]['showtits']==True:
                                if smsg[1].lower() in ["сиськи"]:
                                    answer="[id{}|{}] показал{} {}".format(user_id,users[user_id]['name'],sexinf,args)
                                    self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts['showtits']))

                            elif smsg[0].lower() in ["addcommand"] and CREATOR_ID==int(user_id):
                                users[str(self.uid(smsg[1]))][smsg[2]]=True
                                self.sendmsg(peer_id=peer_id,message="Команда '{}' была выдана пользователю {}".format(smsg[2],smsg[1]))

                            elif smsg[0].lower() in ["remcommand"] and CREATOR_ID==int(user_id):
                                users[str(self.uid(smsg[1]))][smsg[2]]=False
                                self.sendmsg(peer_id=peer_id,message="Команда '{}' была убрана у пользователя {}".format(smsg[2],smsg[1]))

                            elif smsg[0].lower() in ["тиньге"]:
                                try:
                                    opp=smsg[1]
                                    meta_id=int(self.uid(smsg[2]))
                                    ost=smsg[3]
                                    if opp in ["добавить", "+"] and int(user_id)==CREATOR_ID:
                                        users[str(meta_id)]['money']+=int(ost)
                                        self.sendmsg(peer_id=peer_id,message="Тиньге у пользователя {} теперь {}".format(smsg[2],str(users[str(meta_id)]['money'])))

                                    elif opp in ["удалить", "-"] and int(user_id)==CREATOR_ID:
                                        users[str(meta_id)]['money']-=int(ost)
                                        self.sendmsg(peer_id=peer_id,message="Тиньге у пользователя {} теперь {}".format(smsg[2],str(users[str(meta_id)]['money'])))

                                    elif opp in ["перевести", "передать", "перевод"]:
                                        if int(ost)<=0:
                                            answer="Введите положительное кол-во Тиньге, которое хотите передать!"
                                        else:
                                            if users[user_id]['money']<=int(ost):
                                                answer="Вам не хватает Тиньге для перевода!"
                                            else:
                                                users[user_id]['money']-=int(ost)
                                                users[str(meta_id)]['money']+=int(ost)
                                                answer="Тиньге у пользователя {} теперь {}".format(smsg[2],str(users[str(meta_id)]['money']))
                                        self.sendmsg(peer_id=peer_id,message=answer)

                                except IndexError:
                                    self.sendmsg(peer_id=peer_id,message="У вас {} тиньге!".format(str(users[user_id]['money'])))

                            elif smsg[0].lower() in ['монетка']:
                                self.sendmsg(peer_id=peer_id,message=random.choice(["Выпала решка!","Выпал орёл"]))

                            elif smsg[0].lower() in ["бан"] and int(user_id) in RAZR_IDS:
                                users[str(self.uid(smsg[1]))]['banned']==True
                                self.sendmsg(peer_id=peer_id,message="Пользователь теперь в бане. Кикните его, потом его нельзя будет пригласить (чтобы разбанить, команда разбан)")

                            elif smsg[0].lower() in ["разбан"] and int(user_id) in RAZR_IDS:
                                users[str(self.uid(smsg[1]))]['banned']==False
                                self.sendmsg(peer_id=peer_id,message="Теперь этот пользователь не в бане.")

                            elif smsg[0].lower() in ['printpeer_id'] and int(user_id)==CREATOR_ID:
                                self.sendmsg(peer_id=peer_id,message=str(peer_id))

                            elif smsg[0].lower() in ["подножка"]:
                                answer="[id{}|{}] поставил{} подножку {}".format(user_id,users[user_id]['name'],sexinf,args)
                                self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts['podn']))

                            elif smsg[0].lower() in ["sethello"] and int(user_id) in RAZR_IDS:
                                conversations[str(peer_id-CHAT_ID_MIN)]['hello']=args
                                self.sendmsg(peer_id=peer_id,message="Готово!")

                            elif smsg[0].lower() in ["приветствие"]:
                                self.sendmsg(peer_id=peer_id,message=conversations[str(peer_id-CHAT_ID_MIN)]['hello'])

                            elif smsg[0].lower() in ["брак"]:
                                if smsg[1] in ["запрос"] and users[user_id]['love']==False:
                                    brakzapros[user_id]=int(self.uid(smsg[2]))
                                    self.sendmsg(peer_id=peer_id,message="Запрос отправлен!",attachment=random.choice(arts['brak']))
                                elif smsg[1] in ["принять"] and users[user_id]['love']==False:
                                    try:
                                        if int(user_id)==brakzapros[str(self.uid(smsg[2]))]:
                                            del brakzapros[str(self.uid(smsg[2]))]
                                            users[user_id]['love']=int(self.uid(smsg[2]))
                                            users[str(self.uid(smsg[2]))]['love']=int(user_id)
                                            answer="Теперь [id{}|{}] и [id{}|{}] в браке! Поздравим их!".format(user_id,users[user_id]['name'],str(self.uid(smsg[2])),users[str(self.uid(smsg[2]))]['name'])
                                            self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts['love']))
                                        else: self.sendmsg(peer_id=peer_id,message="Этот пользователь не отправлял вам запрос на брак")
                                    except: self.sendmsg(peer_id=peer_id,message="Этот пользователь не отправлял вам запрос на брак")

                            elif msg.lower() in ["ебаться"] and users[user_id]['love']!=False and peer_id==2000000016 or msg.lower() in ["ебаться"] and users[user_id]['love']!=False and int(user_id)==CREATOR_ID:
                                answer="[id{}|{}] ебется с [id{}|{}]".format(user_id,users[user_id]['name'],str(users[user_id]['love']),users[str(users[user_id]['love'])]['name'])
                                self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts['sex']))

                            elif smsg[0].lower() in ["инфа"]:
                                self.sendmsg(peer_id=peer_id,message="Я думаю что {}%".format(str(random.randint(0,101))))

                            elif smsg[0].lower() in ["оцени"]:
                                self.sendmsg(peer_id=peer_id,message="Моя оценка - {} из 5".format(str(random.randint(0,6))))

                            elif smsg[0].lower() in ["кик"] and str(user_id) in conversations[str(peer_id-CHAT_ID_MIN)]['admins']:
                                for i in smsg[1:]:
                                    self.kick(chat_id=peer_id-CHAT_ID_MIN,member_id=int(self.uid(i)))

                            elif smsg[0].lower() in ["обнять","обними"]:
                                self.sendmsg(peer_id=peer_id,message="[id{}|{}] обнял{} {}".format(user_id,users[user_id]['name'],sexinf,args),attachment=random.choice(arts['hug']))

                            elif msg.lower() in ["поцеловаться"] and users[user_id]['love']!=False:
                                answer="[id{}|{}] поцеловался с [id{}|{}]".format(user_id,users[user_id]['name'],str(users[user_id]['love']),users[str(users[user_id]['love'])]['name'])
                                self.sendmsg(peer_id=peer_id,message=answer,attachment=random.choice(arts['kiss']))

                            elif smsg[0].lower() in ["кто"]:
                                memb=random.choice(self.members(peer_id))
                                answer="Мне кажется, что это [id{}|{}]".format(str(memb),users[str(memb)]['name'])
                                self.sendmsg(peer_id=peer_id,message=answer)

                            elif smsg[0].lower() in ["рассылка"] and int(user_id) in RAZR_IDS:
                                tempconversations=conversations.keys()
                                for i in [2000000005,2000000021,2000000022]:
                                    if i in tempconversations:
                                        tempconversations.remove(i)
                                for i in tempconversations:
                                    self.sendmsg(peer_id=int(i)+CHAT_ID_MIN,message=args)

                            elif smsg[0].lower() in ["проверить"] and str(user_id) in conversations[str(peer_id-CHAT_ID_MIN)]['admins']:
                                convers=[2000000021,2000000022]
                                code='''var post = [];
                                var peer_ids={};
                                var i=0;
                                while (i<{}) {{
                                post.push(API.messages.getConversationMembers({{"peer_id": peer_ids[i]}}));
                                i=i+1;
                                }}
                                return post;'''.format(str(convers),len(convers))
                                mem=[[item["member_id"] for item in i["items"] if item['member_id']>0] for i in self.vk_api.execute(code=code)]
                                mem={convers[i]: mem[i] for i in range(len(convers))}
                                v=int(self.uid(smsg[1]))
                                convers=[int(abcde) for abcde in convers if v in mem[abcde]]
                                if convers==[]: answer="Этого пользователя нет в беседах"
                                else: answer=', '.join(list(map(str,convers)))
                                self.sendmsg(peer_id=peer_id,message=answer)

                            elif smsg[0].lower() in ["id","ид"] and int(user_id) in RAZR_IDS:
                                self.sendmsg(peer_id=peer_id,message=str(self.uid(smsg[1])))

                            elif smsg[0].lower() in ["+админ","-админ","админы"] and int(user_id) in RAZR_IDS:
                                if smsg[0].lower() in ["+админ"]:
                                    try:
                                        if str(self.uid(smsg[1])) not in conversations[str(peer_id-CHAT_ID_MIN)]['admins']:
                                            conversations[str(peer_id-CHAT_ID_MIN)]['admins'].append(str(self.uid(smsg[1])))
                                            self.sendmsg(peer_id=peer_id,message="Админ добавлен!")
                                        else:
                                            self.sendmsg(peer_id=peer_id,message="Этот пользователь уже админ!")

                                    except:
                                        conversations[str(peer_id-CHAT_ID_MIN)]['admins']=[str(self.uid(smsg[1]))]
                                        self.sendmsg(peer_id=peer_id,message="Админ добавлен!")

                                elif smsg[0].lower() in ["-админ"]:
                                    conversations[str(peer_id-CHAT_ID_MIN)]['admins'].remove(str(self.uid(smsg[1])))
                                    self.sendmsg(peer_id=peer_id,message="Админ удален!")

                                elif smsg[0].lower() in ["админы"]:
                                    admnames=[users[str(i)]['name'] for i in conversations[str(peer_id-CHAT_ID_MIN)]['admins']]
                                    answer="Админы текущей беседы"
                                    for i in range(len(admnames)):
                                        answer+="\n[id{}|{}]".format(conversations[str(peer_id-CHAT_ID_MIN)]['admins'][i],admnames[i])
                                    self.sendmsg(peer_id=peer_id,message=answer)

                            elif smsg[0].lower() in ["выбери", "выбрать"]:
                                self.sendmsg(peer_id=peer_id,message=random.choice(args.split(' или ')))

                            elif msg.lower() in ["кинь хентай"] and peer_id==2000000016 or msg.lower() in ["кинь хентай"] and int(user_id)==CREATOR_ID:
                                hentai=self.user_vk_for_video.video.search(q="hentai",longer=900,shorter=1800,adult=1,count=10,offset=random.randint(0,1000))['items']
                                att=[random.choice(hentai) for _ in range(10)]
                                self.sendmsg(peer_id=peer_id,attachment=','.join(['video'+str(i['owner_id'])+"_"+str(i['id']) for i in att]))

                            elif msg.lower() in ["созвать всех"] and str(user_id) in conversations[str(peer_id-CHAT_ID_MIN)]['admins']:
                                a=[str(x) for x in self.members(peer_id) if x>0]
                                n=[]
                                for i in a:
                                    if str(i) in users.keys():
                                        n.append(users[str(i)]['name'])
                                    else:
                                        n.append(self.name(i))
                                answer=""
                                for i in range(len(n)):
                                    answer+="[id{}|{}],".format(str(a[i]),n[i])
                                self.sendmsg(peer_id=peer_id,message=answer[:-1])

                            elif msg in ["развод"] and users[user_id]['love']!=False:
                                users[str(users[user_id]['love'])]['love']=False
                                users[user_id]['love']=False
                                self.sendmsg(peer_id=peer_id,message="[id{}|{}] больше не в браке!".format(user_id,users[user_id]['name']),attachment=random.choice(arts['relove']))

                            elif smsg[0] in ["раб"]:
                                if smsg[1] in ["добавить"] and users[user_id]['rab']==True:
                                    if users[str(self.uid(smsg[2]))]['rab_of']==False:
                                        users[str(self.uid(smsg[2]))]['rab_of']=int(user_id)
                                        self.sendmsg(peer_id=peer_id,message="Теперь этот пользователь ваш раб!")
                                    else:
                                        self.sendmsg(peer_id=peer_id,message="Этот пользователь уже раб!")

                                elif smsg[1] in ["удалить"] and users[user_id]['rab']==True:
                                    if users[str(self.uid(smsg[2]))]['rab_of']==int(user_id):
                                        users[str(self.uid(smsg[2]))]['rab_of']=False
                                        self.sendmsg(peer_id=peer_id,message="Раб удален!")
                                    else:
                                        self.sendmsg(peer_id=peer_id,message="Этот пользователь - не ваш раб!")

                                elif smsg[1] in ["поиграться"] and users[user_id]['rab']==True and peer_id==2000000016 or smsg[1] in ["поиграться"] and users[user_id]['rab']==True and int(user_id)==CREATOR_ID:
                                    if users[str(self.uid(smsg[2]))]['rab_of']==int(user_id):
                                        self.sendmsg(peer_id=peer_id,message="[id{}|{}] играется со своей рабыней {}".format(user_id,users[user_id]['name'],' '.join(smsg[2:])),attachment=random.choice(arts['rab']))
                                    else:
                                        self.sendmsg(peer_id=peer_id,message="Этот пользователь не является вашим рабом")

                                elif smsg[1] in ["кормить"] and users[user_id]['rab']==True:
                                    if users[str(self.uid(smsg[2]))]['rab_of']==int(user_id):
                                        self.sendmsg(peer_id=peer_id,message="[id{}|{}] кормит своего раба, {}".format(user_id,users[user_id]['name'],' '.join(smsg[2:])),attachment=random.choice(arts['rabeat']))
                                    else:
                                        self.sendmsg(peer_id=peer_id,message="Этот пользователь не является вашим рабом")

                            elif smsg[0] in ['гарем']:
                                if smsg[1] in ["добавить"] and users[user_id]['garem']==True:
                                    if users[str(self.uid(smsg[2]))]['in_garem']==False:
                                        users[str(self.uid(smsg[2]))]['in_garem']=int(user_id)
                                        self.sendmsg(peer_id=peer_id,message="Теперь этот пользователь в вашем гареме!")
                                    else:
                                        self.sendmsg(peer_id=peer_id,message="Этот пользователь уже находится в чьем-то гареме!")

                                elif smsg[1] in ["удалить"] and users[user_id]['garem']==True:
                                    if users[str(self.uid(smsg[2]))]['in_garem']==int(user_id):
                                        users[str(self.uid(smsg[2]))]['in_garem']=False
                                        self.sendmsg(peer_id=peer_id,message="Пользователь удален из вашего гарема!")
                                    else:
                                        self.sendmsg(peer_id=peer_id,message="Этот пользователь не в вашем гареме!")

                                elif smsg[1] in ["ебаться"] and users[user_id]['garem']==True and peer_id==2000000016 or smsg[1] in ["ебаться"] or users[user_id]['garem']==True and int(user_id)==CREATOR_ID:
                                    if users[str(self.uid(smsg[2]))]['in_garem']==int(user_id):
                                        self.sendmsg(peer_id=peer_id,message="[id{}|{}] ебётся с  {}".format(user_id,users[user_id]['name'],' '.join(smsg[2:])),attachment=random.choice(arts['sex']))
                                    else:
                                        self.sendmsg(peer_id=peer_id,message="Этот пользователь не в вашем гареме")

                                elif smsg[1] in ["поцеловаться"] and users[user_id]['garem']==True:
                                    if users[str(self.uid(smsg[2]))]['in_garem']==int(user_id):
                                        self.sendmsg(peer_id=peer_id,message="[id{}|{}] поцеловался с  {}".format(user_id,users[user_id]['name'],' '.join(smsg[2:])),attachment=random.choice(arts['kiss']))
                                    else:
                                        self.sendmsg(peer_id=peer_id,message="Этот пользователь не в вашем гареме")


                            elif msg in ["хентай"] and int(user_id) in RAZR_IDS:
                                if conversations[str(peer_id-CHAT_ID_MIN)]['hentai']==True:
                                    conversations[str(peer_id-CHAT_ID_MIN)]['hentai']=False
                                    self.sendmsg(peer_id=peer_id,message="Хентай запрещен!")
                                else:
                                    conversations[str(peer_id-CHAT_ID_MIN)]['hentai']=True
                                    self.sendmsg(peer_id=peer_id,message="Хентай разрешен!")

                            elif msg in ["аниме"]:
                                html = requests.get("https://animestars.org/topanime.html")
                                soup = bs(html.text, "html.parser")
                                soup=soup.select('#dle-content')[0].select('.rels-shot.short.clearfix')
                                res=[]
                                for i in soup:
                                    meta=i.select('.short-text')[0]
                                    pic='https://animestars.org'+i.select('.short-i.img-box>img')[0]['src']
                                    name=meta.select('.short-t')[0].get_text()
                                    url=meta.select('.short-t')[0]['href']
                                    genres=meta.select('.short-c')[0].get_text()
                                    describe=meta.select('.short-d')[0].get_text()
                                    res.append({'name': name, 'url': url, 'genres': genres, 'describe': describe,'pic': pic})
                                res=random.choice(res)
                                message=res['name']+':\nЖанры: '+res['genres']+'\nОписание: '+res['describe']+'\n'+res['url']
                                self.sendmsg(peer_id=peer_id,message=message,attachment=self.photo(url=res['pic'],peer_id=peer_id))

                            elif msg in ['время']:
                                MoscowTime=bs(requests.get("https://www.timeserver.ru/cities/ru/moscow").text,'html.parser').select('div.timeview-data')[0].select('div')[0]
                                LondonTime=bs(requests.get("https://www.timeserver.ru/cities/gb/london").text,'html.parser').select('div.timeview-data')[0].select('div')[0]
                                TokyoTime=bs(requests.get("https://www.timeserver.ru/cities/jp/tokyo").text,'html.parser').select('div.timeview-data')[0].select('div')[0]
                                MoscowTime=[MoscowTime.select('span.hours')[0].get_text(),MoscowTime.select('span.minutes')[0].get_text(),MoscowTime.select('span.seconds')[0].get_text()]
                                LondonTime=[LondonTime.select('span.hours')[0].get_text(),LondonTime.select('span.minutes')[0].get_text(),LondonTime.select('span.seconds')[0].get_text()]
                                TokyoTime=[TokyoTime.select('span.hours')[0].get_text(),TokyoTime.select('span.minutes')[0].get_text(),TokyoTime.select('span.seconds')[0].get_text()]
                                #self.sendmsg(peer_id=523261909,message=str(info))
                                self.sendmsg(peer_id=peer_id,message="Время по МСК: {}\nВремя по Лондону: {}\nВремя по Токио: {}".format(':'.join(MoscowTime),':'.join(LondonTime),':'.join(TokyoTime)))

                            elif smsg[0] in ["вики"]:
                                json_get=requests.get("https://ru.wikipedia.org/w/api.php?action=opensearch&search="+'%20'.join(args.split(' '))+"&meta=siteinfo&rvprop=content&format=json").json()
                                self.sendmsg(peer_id=peer_id,message=json_get[2][0]+"\nСсылка: "+json_get[3][0])

                            elif smsg[0] in ["выход"] and int(user_id)==CREATOR_ID:
                                self.sendmsg(peer_id=peer_id,message="бот выключается!")
                                with open('users.json','w',encoding='utf-8') as f:
                                    json.dump(users,f,indent=4,ensure_ascii=False)
                                with open('conversations.json','w',encoding='utf-8') as f:
                                    json.dump(conversations,f,indent=4,ensure_ascii=False)
                                with open('arts.json','w',encoding='utf-8') as f:
                                    json.dump(arts,f,indent=4,ensure_ascii=False)
                                exit()

                            elif smsg[0] in ["ник"]:
                                if len(' '.join(smsg[1:]))<=20:
                                    users[user_id]['name']=' '.join(smsg[1:])
                                    self.sendmsg(peer_id=peer_id,message="Ваш ник изменен!")
                                else:
                                    self.sendmsg(peer_id=peer_id,message="Длина ника должна быть не более 20 символов!")

                            elif smsg[0] in ['опенинги']:
                                openings=[random.choice(self.music) for _ in range(10)]
                                answer="😁🎵🎶[id{id}|{name}], Держи опенинги 🎧".format(id=str(user_id),name=users[user_id]['name'])
                                self.sendmsg(peer_id=peer_id,message=answer,attachment=','.join(["audio"+str(i['owner_id'])+"_"+str(i['id']) for i in openings]))

                            elif msg in ["F","press F"]:
                                self.sendmsg(peer_id=peer_id,message="[id{}|{}] отдал{} честь!".format(user_id,users[user_id]['name'],sexinf),attachment=random.choice(arts['pressf']))

                            elif msg in ['facepalm']:
                                self.sendmsg(peer_id=peer_id,message="[id{}|{}] сделал{} facepalm".format(user_id,users[user_id]['name'],sexinf),attachment=random.choice(arts['facepalm']))

                            elif smsg[0] in ["взлом"] and users[str(user_id)]['money']>=250:
                                users[str(user_id)]['money']-=250
                                self.sendmsg(peer_id=peer_id,message="[id{}|{}] взломал{} жопу {}".format(user_id,users[user_id]['name'],sexinf,args),attachment=random.choice(arts['vzlom']))

                            elif msg in ["охуеть"]:
                                self.sendmsg(peer_id=peer_id,message="[id{}|{}] охуевает от происходящего".format(user_id,users[user_id]['name']),attachment=random.choice(arts['ohuet']))

                            elif smsg[0] in ["addart"] and int(user_id) in RAZR_IDS:
                                try:
                                    arts[smsg[1]].append(smsg[2])
                                except KeyError:
                                    arts[smsg[1]]=[smsg[2]]
                                self.sendmsg(peer_id=peer_id,message="Арт добавлен!")

                            elif smsg[0] in ["казино"]:
                                meta=list(smsg[1].lower())
                                metak=meta.count('к')
                                while 'к' in meta: meta.remove('к')
                                metamoney=int(''.join(meta))*(1000**metak)
                                if metamoney>0 and metamoney<=users[str(user_id)]['money']:
                                    mt=random.randint(0,1000)
                                    if mt in range(0,200): cf='0'
                                    elif mt in range(200,350): cf='0.1'
                                    elif mt in range(350,500): cf='0.5'
                                    elif mt in range(500,630): cf='1'
                                    elif mt in range(630,750): cf='1.5'
                                    elif mt in range(750,995): cf='2'
                                    else: cf='10'
                                    hp=users[str(user_id)]['money']
                                    users[str(user_id)]['money']-=metamoney
                                    if cf=='0': metamoney=0
                                    elif cf=='0.1': metamoney=metamoney//10
                                    elif cf=='0.5': metamoney=metamoney//2
                                    elif cf=='1': pass
                                    elif cf=='1.5': metamoney=metamoney+metamoney//2
                                    elif cf=='2': metamoney=metamoney*2
                                    elif cf=='10': metamoney=metamoney*10
                                    users[str(user_id)]['money']+=round(metamoney)
                                    self.sendmsg(peer_id=peer_id,message="Коэффицент: x{}.\nВаши деньги - ".format(cf)+str(users[str(user_id)]['money'])+"\nБыло - "+str(hp))
                                else: self.sendmsg(peer_id=peer_id,message="Неправильное число. Число должно быть больше 0 и меньше, чем денег у вас!")

                            elif smsg[0] in ["накормить"]:
                                self.sendmsg(peer_id=peer_id,message="[id{}|{}] накормил{} {}".format(user_id,users[user_id]['name'],sexinf,args),attachment=random.choice(arts['eat']))

                            elif smsg[0] in ["поблагодарить"]:
                                self.sendmsg(peer_id=peer_id,message="[id{}|{}] поблагодарил{} {}".format(user_id,users[user_id]['name'],sexinf,args),attachment=random.choice(arts['thx']))

                            elif smsg[0].lower() in ["донат"]:
                                answer="50 рублей:\nрабовладельчество\nнаписать отдельную премиум команду для одного человека\n\n20 рублей:\nгарем\n\n5 рублей за одну команду:\nёбнуть\nударить\nвзорвать вселенную\nкрестовый поход\nпропылесосить\nкататься\nопидорасить\nпорезать руки\nстать котом\nстать мачо\nзабанить\nнапиться до инфаркта\nкусь\nпочесать\nполетать\nпостроить дом\nпоказать сиськи\nуничтожить яой\nненавидеть\nрасплакаться"
                                answer+="\n\n5 рублей:\nсмена ника с кол-вом символов больше 20\n\n n рублей\nзабрать раба у рабовладельца - стоимость в зависимости, от статуса человека в беседе\n\nкол-во монет за 1 рубль - 200\nпо поводу покупки писать (программисту)"
                                self.sendmsg(peer_id=peer_id,message=answer)

                            elif smsg[0] in ["профиль"]:
                                if args!="":
                                    profile_id=str(self.uid(args))
                                else:
                                    profile_id=user_id

                                if int(profile_id)==CREATOR_ID:
                                    user_role="Создатель бота"
                                elif int(profile_id) in RAZR_IDS:
                                    user_role="Разработчик"
                                elif int(profile_id)==MUSA_ID:
                                    user_role="создатель бесед"
                                elif int(profile_id)==LEHA_ID:
                                    user_role="Нигилист"
                                elif int(profile_id)==MILA_ID:
                                    user_role="Богиня Беседы"
                                elif profile_id in conversations[str(peer_id-CHAT_ID_MIN)]['admins']:
                                    user_role="Админ текущей беседы"
                                else:
                                    user_role="участник беседы"

                                if False:
                                    clan=""
                                else:
                                    clan="Vanya_heh"

                                if users[profile_id]['love']==False:
                                    love="никем"
                                else:
                                    love=('[id'+str(users[profile_id]['love'])+'|'+users[str(users[profile_id]['love'])]['name']+']')

                                if users[profile_id]['rab_of']!=False:
                                    rabinf="Раб у [id{}|{}]".format(str(users[profile_id]['rab_of']),users[str(users[profile_id]['rab_of'])]['name'])
                                else: rabinf=""

                                if users[profile_id]['in_garem']!=False:
                                    garemif="в гареме у [id{}|{}]".format(str(users[profile_id]['in_garem']),users[str(users[profile_id]['in_garem'])]['name'])
                                else: garemif=""
                                answer="Имя - {name}\nНик - {nick}\nДенег - {money}\nВ браке с - {love}\nРоль - {role}\nВ клане - {clan}\n".format(name=self.name(profile_id),nick=users[profile_id]['name'],love=love,role=user_role,clan=clan,money=str(users[profile_id]['money']))+rabinf+garemif
                                self.sendmsg(peer_id=peer_id,message=answer)


                            elif smsg[0] in ["помощь"]:
                                al=["донат - стоимость и виды премиум команд","Тиньге - кол-во Тиньге","монетка - сыграть в монетку", "подножка - поставить подножку", "приветствие - приветствие", "инфа - информация о чем-то в процентах", "оцени - оценить что-то по 5бальной шкале","кто - кто","выбери 1 или 2 или... или n - выбрать одно из нескольких" , "обнять - обнять пользователя", "время - время по МСК/Лондону/Токио","вики - информация о чем-то из википедии", "аниме - посоветовать аниме","ник - сменить ник", "опенинги - кинуть опенинги", "press F - press F", "facepalm - facepalm", "взлом - взлом жопы", "охуеть - охуеть от происходящего", "казино - казино", "накормить - накормить", "поблагодарить - поблагодарить", "профиль - профиль", "кинь хентай - кинуть хентай"]
                                aladm=["созвать всех - созвать всех","кик - кик пользователя (или пользователей)","проверить - на наличие бесед"]
                                albrak=["брак запрос @id1 + брак принять @id2 - запрос и добавление в брак", "развод - развод", "поцеловаться - поцеловаться с мужем/женой", "ебаться - ебаться с мужем/женой"]
                                alrazr=["бан - бан", "разбан - разбан", "sethello - установить приветствие", "рассылка - рассылка информации", "ид - ID пользователя", "+админ - добавить админа в текущую беседу", "-админ - убрать админа из текущей беседы", "админы - список админов", "хентай - запрет/разрешение хентая"]
                                alcreator=["addcommand/remcommand - добавить/удалить команду", "printpeer_id - получить peer_id беседы", "выход - выкл бота", "addart - добавить арт на команду (пример - addart sex photo-1_2)","use - читкоманда создателя(зера, use id (команла))"]
                                alexclusive={"cry": "расплакаться","hate": "ненавидеть","yaoy": "уничтожить яой","wall": "ёбнуть","hit": "ударить", "universe": "взорвать вселенную", "crusade": "крестовый поход", "vacuum": "пропылесосить", "ride": "кататься","opidorasit": "опидорасить", "cut": "порезать руки", "cat": "стать котом", "macho": "стать мачо", "ban": "забанить", "drink": "напиться до инфаркта", "kus": "кусь", "scratch": "почесать", "fly": "полетать", "ricardo":"рикардо", "house": "построить дом", "rose": "подарить розу", "showtits": "показать сиськи"}
                                alexclusive=[alexclusive[i] for i in alexclusive.keys() if users[user_id][i]==True]
                                alrab=["раб добавить","раб удалить","раб поиграться","раб кормить"]
                                algarem=["гарем добавить","гарем удалить","гарем ебаться","гарем поцеловаться"]
                                answer="[Основные команды]: \n"+'\n'.join(al)+"\n\n"+"[Брак-команды]: \n"+'\n'.join(albrak)+"\n\n"
                                if str(user_id) in conversations[str(peer_id-CHAT_ID_MIN)]['admins']: answer+="[Команды админов]: \n"+"\n".join(aladm)+"\n\n"
                                if int(user_id) in RAZR_IDS: answer+="[Команды разработчиков бота]: \n"+"\n".join(alrazr)+"\n\n"
                                if int(user_id) == CREATOR_ID: answer+="[Команды создателя бота]: \n"+"\n".join(alcreator)+"\n\n"
                                if alexclusive!=[]: answer+="[Премиум команды]: \n"+"\n".join(alexclusive)+"\n\n"
                                if users[user_id]['rab']!=False: answer+="[Pабовладельчество]: \n"+"\n".join(alrab)+"\n\n"
                                if users[user_id]['garem']!=False: answer+="[Гарем]: \n"+"\n".join(algarem)
                                self.sendmsg(peer_id=peer_id,message=answer)


                            #помощь (эксклюзивы, раб), кланы

            except Exception as e: print(repr(e))
info=json.load(open('info.json'))
harliServer=harli(
        api_token=info['api_token'],
        group_id=info['group_id'],
        music_id=info['music_id'],
        login=info['login'],
        password=info['password'],
        user_token=info['user_token']
    )
harliServer.start()

