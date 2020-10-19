question_words = ('What', 'How', 'When', 'Which', 'Shall', 'Should', 'Would', 'Could', 'Can', 'Do', 'Does', 'Is')
texts = []

def ask_to_say_something():
    raw_text = input('Say something: ')
    return str(raw_text).strip()

def is_end(text):
    return text.count('\end') > 0

def append_punctuation(text):
    punctuation = '.'
    if text.startswith(question_words): punctuation = '?'
    return f'{text}{punctuation}'
 
def make_conclusion(texts):
    sentences = []
    for text in texts:
        if text.strip() == '' or is_end(text): continue
        sentence = text.capitalize()
        sentence = append_punctuation(sentence)
        sentences.append(sentence)
    return ' '.join(sentences)

def main():
    while True:
        texts.append(ask_to_say_something())
        if is_end(texts[-1]): break
    print(make_conclusion(texts))

# Start app
main()