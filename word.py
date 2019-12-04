import random

class Word:

    def __init__(self, filename, minLength): # minLength 받을 문자의 최소길이
        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            word = line.rstrip()
            if len(word) >= minLength:
                self.words.append(word) # 단어의 길이가 minLength보다 길어야함
                self.count += 1

        print('%d words in DB' % self.count)


    def test(self):
        return 'default'


    def randFromDB(self):

        r = random.randrange(self.count)
        return self.words[r]
