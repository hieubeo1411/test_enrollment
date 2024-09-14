import json
import os
from collections import Counter


def def_word_cnt(text, folder_name='json_files'):
    word_count = Counter(text.split())
    result = dict(word_count)
    os.makedirs(folder_name, exist_ok=True)
    def save_to_json(n=1):
        if n > 100:
            return
        filename = os.path.join(folder_name, f'result_{n}.json')
        with open(filename, 'w') as file:
            json.dump(result, file, indent=4)
        save_to_json(n + 1)
    save_to_json()
text_input = "hello world hello"
def_word_cnt(text_input, folder_name='100_json_files')
