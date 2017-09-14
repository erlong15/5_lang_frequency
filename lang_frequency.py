import sys
import re
from collections import Counter

def load_data(filepath):
    with open(filepath, 'r') as f:
        words = re.findall(r'\w+', f.read().lower())
        return words

def get_most_frequent_words(words, top_count):
    return Counter(words).most_common(top_count)

if __name__ == '__main__':
    words = load_data(sys.argv[1])
    top_count = 10
    for word in get_most_frequent_words(words, top_count):
        print('%s: %s' % word)
