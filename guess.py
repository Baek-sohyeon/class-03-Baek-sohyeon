class Guess:

    def __init__(self, word):

        self.secretWord = word
        self.guessedChars = set()
        self.numTries = 0
        self.currentStatus = '_' * len(word)


    def display(self):

        print('단어:' + self.currentStatus)
        print('시도횟수:' + str(self.numTries))


    def guess(self, character):

        self.guessedChars  |= {character}   #guessedChars 집합에 입력받은 새로운 문자를 합집합 시킨다.
        if character not in self.secretWord:    #입력한 문자가 단어가 필요없는 문자라면
            self.numTries += 1
            return False

        else:
            currentStatus = ''
            for c in self.secretWord:       #단어의 첫번째 문자부터 뽑음
                if c in self.guessedChars:
                    currentStatus += c
                else:
                    currentStatus += '_'

            self.currentStatus = currentStatus



