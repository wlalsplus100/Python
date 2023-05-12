import discord
import os
from datetime import datetime, time, timedelta
import random
import json

TOKEN = os.environ.get('TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')

from datetime import datetime, timedelta, time

def get_remaining_time_until(target):
    target_day = target[0]
    if target_day == 'Friday':
        target_day = 4
    elif target_day == 'Saturday':
        target_day = 5
    target_time = target[1]
    now = datetime.now()
    
    days_until_target = (target_day - now.weekday()) % 7
    
    if days_until_target == 0 and now.time() >= target_time:
        days_until_target = 7
    
    if days_until_target == 0 and now.time() < target_time:
        next_target_time = datetime.combine(now.date(), target_time)
        time_remaining = next_target_time - now
    else:
        next_target_day = now + timedelta(days=days_until_target)
        next_target_time = datetime.combine(next_target_day.date(), target_time)
        time_remaining = next_target_time - now
    
    return time_remaining



class MyClient(discord.Client):


    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await self.change_presence(status=discord.Status.online, activity=discord.Game("대기중"))
        try:
            with open('.\\dbot\\data.json') as f:
                json_data = json.load(f)
                MyClient.go_home_day = []
                for item in json_data:
                    if ":" in item:  # Assume it's a time string
                        time_obj = time.fromisoformat(item)
                        MyClient.go_home_day.append(time_obj)
                    else:  # Assume it's a string
                        MyClient.go_home_day.append(item)
        except json.decoder.JSONDecodeError:
            MyClient.go_home_day = "아직 설정되지 않음"



 
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content[0] == '!':
            if message.content[1:] == 'ping':
                await message.channel.send('pong {0.author.mention}'.format(message))
            elif message.content[1:] == '귀가설정':
                if str(message.author) == '일반인1#8315':
                    msg = await message.channel.send('1. 금요일 14시 30분 귀가\n2. 금요일 22시 15분 귀가\n3. 토요일 6시 30분 귀가')
                    await msg.add_reaction('🕝')
                    await msg.add_reaction('🕣')
                    await msg.add_reaction('🕡')
            elif message.content[1:5] == '제비뽑기':
                if(len(message.content) > 6):
                    jaby = str(message.content[6:]).split(' ')
                    result = random.choice(jaby)
                    await message.channel.send("매우 공정한 제비뽑기 결과 {}(이)가 뽑혔습니다".format(result))
                else:
                    await message.channel.send("제비뽑기의 요소를 입력해주세요.")
            else:
                answer = self.get_answer(message.content)
                await message.channel.send(answer)

    async def on_reaction_add(self, reaction, user):
        if user.bot == 1: #봇이면 패스
            return None
        if str(reaction.emoji) == "🕝":
            await reaction.message.channel.send("귀가 시간이 금요일 14시 30분으로 설정되었습니다.")
            MyClient.go_home_day = ['Friday', time(14, 30)]
            json_data = []
            for item in MyClient.go_home_day:
                if isinstance(item, time):
                    json_data.append(item.strftime("%H:%M:%S"))  # Convert time object to string
                else:
                    json_data.append(item)  # Keep strings as they are
            
            with open(".\\dbot\\data.json", "w") as file:
                json.dump(json_data, file)
        if str(reaction.emoji) == "🕣":
            await reaction.message.channel.send("귀가 시간이 금요일 22시 15분으로 설정되었습니다.")
            MyClient.go_home_day = ['Friday', time(22, 15)]
            json_data = []
            for item in MyClient.go_home_day:
                if isinstance(item, time):
                    json_data.append(item.strftime("%H:%M:%S"))  # Convert time object to string
                else:
                    json_data.append(item)  # Keep strings as they are

            with open(".\\dbot\\data.json", "w") as file:
                json.dump(json_data, file)

        if str(reaction.emoji) == "🕡":
            await reaction.message.channel.send("귀가 시간이 토요일 6시 30분으로 설정되었습니다.")
            MyClient.go_home_day = ['Saturday', time(6, 30)]
            json_data = []
            for item in MyClient.go_home_day:
                if isinstance(item, time):
                    json_data.append(item.strftime("%H:%M:%S"))  # Convert time object to string
                else:
                    json_data.append(item)  # Keep strings as they are
            
            with open(".\\dbot\\data.json", "w") as file:
                json.dump(json_data, file)
 
    def get_day_of_week(self):
        weekday_list = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
 
        weekday = weekday_list[datetime.today().weekday()]
        date = datetime.today().strftime("%Y년 %m월 %d일")
        result = '{}({})'.format(date, weekday)
        return result
 
    def get_time(self):
        return datetime.today().strftime("%H시 %M분 %S초")
    
    
    def get_time_gohome(self):
        if type(MyClient.go_home_day) == str:
            return ['귀가일이 설정되지 않았습니다.', '얼마 남았는지 구할 수 없습니다.']
        if MyClient.go_home_day == ['Friday', time(14, 30)]:
            go_home_day = '금요일 14시 30분'
        elif MyClient.go_home_day == ['Friday', time(22, 15)]:
            go_home_day = '금요일 22시 15분'
        elif MyClient.go_home_day == ['Saturday', time(6, 30)]:
            go_home_day = '토요일 6시 30분'
        result = get_remaining_time_until(MyClient.go_home_day)
        days = result.days
        secs = result.seconds
        hours = secs // 3600
        mins = (secs // 60) % 60
        secs = secs % 60

        return [go_home_day, '{}일 {}시 {}분 {}초 남았습니다.'.format(days, hours, mins, secs)]
 
    def get_answer(self, text):
        trim_text = text.replace(" ", "")
        trim_text = trim_text.replace("!", "")


 
        answer_dict = {
            '안녕': '안녕하세요. MyBot입니다.',
            '요일': ':calendar: 오늘은 {}입니다'.format(self.get_day_of_week()),
            '시간': ':clock9: 현재 시간은 {}입니다.'.format(self.get_time()),
            '귀가': ':calendar: 설정된 귀가일은 {}입니다. 귀가까지 {}'.format(self.get_time_gohome()[0], self.get_time_gohome()[1]),
        }
 
        if trim_text == '' or None:
            return "알 수 없는 질의입니다. 답변을 드릴 수 없습니다."
        elif trim_text in answer_dict.keys():
            return answer_dict[trim_text]
        else:
            for key in answer_dict.keys():
                if key.find(trim_text) != -1:
                    return "연관 단어 [" + key + "]에 대한 답변입니다.\n" + answer_dict[key]
 
            for key in answer_dict.keys():
                if answer_dict[key].find(text[1:]) != -1:
                    return "질문과 가장 유사한 질문 [" + key + "]에 대한 답변이에요.\n" + answer_dict[key]
 
        return text + "은(는) 없는 질문입니다."
 
 
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)