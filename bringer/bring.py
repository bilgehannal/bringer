import bios
import math
import re
from collections import Counter
import pkg_resources
from urllib.request import urlopen

URL_BASE_OF_CONTENTS = "https://raw.githubusercontent.com/bilgehannal/bringer-data/main/contents"
URL_CONTENT_FILE = "https://raw.githubusercontent.com/bilgehannal/bringer-data/main/content.yaml"

WORD = re.compile(r"\w+")

f = urlopen(URL_CONTENT_FILE)
tmp_str = f.read().decode("utf-8") 
bios.write('content.yaml', tmp_str, file_type='standart')
contents = bios.read('content.yaml')

def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

def get_cosine(text1, text2):
    vec1 = text_to_vector(text1.lower())
    vec2 = text_to_vector(text2.lower())

    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def compare(labels, content, best_match):
    tmp_cos = get_cosine(labels, content['labels'])
    if tmp_cos > best_match['cos']:
        return {'cos': tmp_cos, 'content': content}
    return best_match

def compare_labels_with_all_content(labels):
    best_match = {
        'cos': 0, 
        'content': contents[0]
    }
    for content in contents:
        best_match = compare(labels, content, best_match)
    return best_match['content']

def print_content(content):

    f = urlopen('{}/{}'.format(URL_BASE_OF_CONTENTS, content['name']))
    file_content = f.read().decode("utf-8") 
    print(file_content)

def find_content(labels):
    content = compare_labels_with_all_content(labels)
    print_content(content)