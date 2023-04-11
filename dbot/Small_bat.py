import discord
import os
from datetime import datetime
 
TOKEN = os.environ.get('TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')

def get_remaining_time_until(target_day, target_time):
    now = datetime.datetime.now()
    days_until_target = (datetime.datetime.strptime(target_day, '%A').weekday() - now.weekday()) % 7
    
    if now.weekday() == datetime.datetime.strptime(target_day, '%A').weekday() and now.time() >= target_time:
        days_until_target = (7 - now.weekday() + datetime.datetime.strptime(target_day, '%A').weekday()) % 7
        
    next_target_day = now + datetime.timedelta(days=days_until_target)
    next_target_time = datetime.datetime.combine(next_target_day.date(), target_time)

    time_remaining = next_target_time - now

    return time_remaining



class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await self.change_presence(status=discord.Status.online, activity=discord.Game("대기중"))
 
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content[0] == '!':
            if message.content[1:] == 'ping':
                await message.channel.send('pong {0.author.mention}'.format(message))
            else:
                answer = self.get_answer(message.content)
                await message.channel.send(answer)
 
    def get_day_of_week(self):
        weekday_list = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
 
        weekday = weekday_list[datetime.today().weekday()]
        date = datetime.today().strftime("%Y년 %m월 %d일")
        result = '{}({})'.format(date, weekday)
        return result
 
    def get_time(self):
        return datetime.today().strftime("%H시 %M분 %S초")
    
    
    def get_time_gohome(self):
        pass
 
    def get_answer(self, text):
        trim_text = text.replace(" ", "")
        trim_text = trim_text.replace("!", "")


 
        answer_dict = {
            '안녕': '안녕하세요. MyBot입니다.',
            '요일': ':calendar: 오늘은 {}입니다'.format(self.get_day_of_week()),
            '시간': ':clock9: 현재 시간은 {}입니다.'.format(self.get_time()),
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