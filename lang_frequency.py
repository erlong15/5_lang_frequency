import sys
import re


def load_data(filepath):
    words = {}
    with open(filepath, 'r') as f:
        for line in f:
            """
            Read line by line to avoid memory issues
            """
            for word in re.findall('[\w\d]+', line):
                words[word] = words[word] + 1 if word in words else 1

        return sorted(words.items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    print(load_data(sys.argv[1])[:10])
