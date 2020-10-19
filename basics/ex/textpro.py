interrogatives = ('What', 'How', 'When', 'Which', 'Shall', 'Should', 'Would', 'Could', 'Can', 'Do', 'Does', 'Is')
phrases = []

def ask_to_say_something():
    raw_text = input('Say something: ')
    return str(raw_text).strip()

def is_end(phrase):
    return phrase.count('\end') > 0

def append_punctuation(phrase):
    if phrase.startswith(interrogatives): 
        return '{}?'.format(phrase)
    else:
        return '{}.'.format(phrase)
 
def make_sentences(phrases):
    sentences = []
    for phrase in phrases:
        if phrase.strip() == '' or is_end(phrase): continue
        sentence = phrase.capitalize()
        sentence = append_punctuation(sentence)
        sentences.append(sentence)
    return ' '.join(sentences)

def main():
    while True:
        phrases.append(ask_to_say_something())
        if is_end(phrases[-1]): break
    print(make_sentences(phrases))

# Start app
main()