import re

def main():
    WORD_RE = re.compile('\w+')

    index = {}
    with open("setdefault_data.txt","r",encoding='utf-8') as f:
        for line_no, line in enumerate(f):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start()+1
                location = (line_no, column_no)
                index.setdefault(word, []).append(location)
    #print(index)
    # print in alphabetical order
    for word in sorted(index, key=str.upper):
        print(word, index[word])

if __name__ == '__main__':
    main()
