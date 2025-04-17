import json

from Tools.scripts.summarize_stats import print_title

with open('questions.json','r') as file:
    content = file.read()


data = json.loads(content)
print(data)

score = 0

for question in data:
    print(question['question_text'])
    for index, answer in enumerate(question['alternatives']):
        print(f'{index + 1} - {answer}')
    user_choice = int(input('Your choice: '))
    question['user_choice'] = user_choice

for index, question in enumerate(data):
    if question['user_choice'] == question['correct_answer']:
        score += 1

print(score,'/',len(data))