import random


class Monkey:
    def generateOne(self, leng):  # generates one rand str of approp length
        """
        restype: str
        rtype: str
        """
        self.length = leng
        res = ""
        alphabet = "abcdefghijklmnopqrstuvwyxz "
        for i in range(self.length):  # iterating through str
            res = res + alphabet[random.randrange(27)]  # concat 1 letter

        return res

    def score(self, generateOne, goalstr, percent=0):
        self.goalstring = goalstr
        numsame = 0
        for i in range(len(self.goalstring)):  # iterating through str
            if self.goalstring[i] == generateOne[i]:
                numsame = numsame + 1  # if char is the same count it
                percent = numsame / len(self.goalstring)  # check
            return percent

    def main(self, generateOne, score):
        best = 0
        while score < 1:
            if score > best:
                print(score, self.goalstring)
                best = score
                score(29, self.goalstring)


monkey1 = Monkey()
gen = monkey1.generateOne(29)
scor = monkey1.score(gen, 'me thinks it is like a weasel')
mai = monkey1.main(gen, scor)
