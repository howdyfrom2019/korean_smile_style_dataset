import json

content = {}
content['formal'] = 'Formal is helpful and polite assistant'
content['informal'] = 'Informal is helpful and friendly assistant'
content['android'] = 'Android has a robotical accent'
content['azae'] = 'Azae is 40 years old assistant'
content['chat'] = 'Chat is youngster and chatty assiatant'
content['choding'] = 'Choding is 8 years old and cute assistant'
content['emoticon'] = 'Emoticon is usually using text emoji and friendly assistant'
content['enfp'] = 'Enfp is outroverted and always making a positive vibe assistant'
content['gentle'] = 'Gentle is gentle assistant'
content['halbae'] = 'Halbae is eldery male assistant'
content['halmae'] = 'Halbae is eldery female assistant'
content['joongding'] = 'Joongding is korean teenager assistant'
content['king'] = 'King has traditional korean king\'s accent assistant'
content['naruto'] = 'Naruto has animation charactor naruto\'s accent assistant'
content['seonbi'] = 'Seonbi has tradition korean poet\'s accent assistant'
content['sosim'] = 'Sosim is shy and introverted assistant'
content['translator'] = 'Translator has translated korean accent'


def tsvparser(input, output):
  file = open(input, 'rt', encoding='utf-8')
  firstline = file.readline()
  titles = [type.strip() for type in firstline.split('\t')]

  for i in range(0, len(titles)):
    title = titles[i]
    arr = []
    isUser = True
    messages = [{'role': 'system', 'content': content[title]}]
    for line in file:
      response = line.split('\t')
      if response.count('') == 16:
        arr.append({'messages' : messages})
        messages = [{'role': 'system', 'content': content[title]}]
        isUser = True
        continue
      message = {}
      message['role'] = 'user' if isUser else 'assistant'
      message['content'] = response[i]
      messages.append(message)
      isUser = not isUser
    filename = str(output) + '_' + str(title) + '.json'
    with open(filename, 'wt', encoding='utf-8') as filename:
      filename.write(json.dumps(arr, indent=4, ensure_ascii=False))
    file = open(input, 'rt', encoding='utf-8')
    firstline = file.readline()

input_filename = 'smilestyle_dataset.tsv'
output_filename = 'smilestyle_dataset'
tsvparser(input_filename, output_filename)