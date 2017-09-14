import sys
import re
from collections import Counter

def load_data(filepath):
    with open(filepath, 'r') as f:
        words = re.findall(r'\w+', f.read().lower())
        return words

def get_most_frequent_words(words, cnt):
    return Counter(words).most_common(cnt)

if __name__ == '__main__':
    words = load_data(sys.argv[1])
    for word in get_most_frequent_words(words, 10):
        print('%s: %s' % word)
