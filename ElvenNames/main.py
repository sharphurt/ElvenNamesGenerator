import re
import random


def parse(text):
    parsed = {}
    for words in re.sub(r'[^a-zA-Zа-яА-Я\n]', ' ', text).split('\n'):
        words_seq = re.sub('[ ]+', ' ', words).strip().split(' ')
        word = words_seq[0]
        translation = list(filter(lambda w: (re.search(r'[а-яА-Я]', w)), words_seq))
        if not translation:
            continue
        parsed[word] = translation[0]
    return parsed


prefix_text = open("elvenPrefix.txt", 'r', encoding='utf-8')
suffix_text = open("elvenSuffix.txt", 'r', encoding='utf-8')

prefix_with_translation = parse(prefix_text.read())
suffix_with_translation = parse(suffix_text.read())

prefix_text.close()
suffix_text.close()

firstname, fn_translation = random.sample(prefix_with_translation.items(), 1)[0]
lastname, ln_translation = random.sample(suffix_with_translation.items(), 1)[0]

print(f'{firstname}{lastname} - {fn_translation} {ln_translation}')
