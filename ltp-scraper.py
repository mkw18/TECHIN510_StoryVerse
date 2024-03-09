import os
import requests
import re
import json
from dotenv import load_dotenv

load_dotenv()

from openai import OpenAI
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'), base_url=os.getenv('OPENAI_API_BASE'))

URL = 'https://yesnogame.net'
res = requests.get(URL+'/en')

max_page = int(re.findall(r'<a class="pagination__link" href="/en\?page=(\d+)', res.text)[0])
for i in range(1, max_page+1):
    page = requests.get(f'{URL}/en?page={i}')
    stories = re.findall(r'<a class="quest__link" href="(.+)">', page.text)
    for link in stories:
        game = requests.get(URL+link)
        story = re.findall('<div class="quest__card__front quest__story quest__story_question">\n.+\n.+<p>(.+)</p>', game.text)[0]
        answer = re.findall('<div class="quest__card__back quest__story quest__story_answer">\n.+\n.+<p>(.+)</p>', game.text)[0]
        eval = re.findall('<div class="quest__about__value">(.+)</div>', game.text)
        like, time, level, date = eval[0], eval[1], eval[2], eval[3]
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {'role': 'user', 'content': f'Please list the key point of the following sentence:\n{story}'}
            ]
        )
        story_key = completion.choices[0].message.content
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {'role': 'user', 'content': f'Please list the key point of the following sentence:\n{answer}'}
            ]
        )
        answer_key = completion.choices[0].message.content
        data = {
            'story': story, 
            'answer': answer, 
            'story_keys': story_key, 
            'answer_keys': answer_key, 
            'likes': like, 
            'solving_time': time,
            'level': level,
            'date': date
        }
        if level[-4:] == 'Hard':
            with open('data/hard.json', 'a+') as f:
                f.write(json.dumps(data)+'\n')
        elif level[-4:] == 'Easy':
            with open('data/easy.json', 'a+') as f:
                f.write(json.dumps(data)+'\n')
        if level[-4:] == 'dium':
            with open('data/medium.json', 'a+') as f:
                f.write(json.dumps(data)+'\n')
        # with open('data/details.json', 'a+') as f:
        #     f.write(json.dumps(data, indent=2)+'\n')
