# Print Your code here
class Solution:
    def __init__(self):
        self.crossedChrDict = {}
        self.maxLengthStr = 0
        self.index = 0
        self.currentStrLength = 0

    def lengthOfLongestSubstring(self, s):
        while self.index != len(s):
            self.chrRepeatHandler(s)
            self.chrNonRepeatHandler(s)
            self.index = self.index + 1
        self.setMaxLengthStr()
        return self.maxLengthStr

    def chrRepeatHandler(self, s):
        if(self.crossedChrDict.get(s[self.index]) != None):
            self.setMaxLengthStr()
            self.index = self.crossedChrDict.get(s[self.index]) + 1
            self.crossedChrDict = {}
            self.currentStrLength = 0

    def chrNonRepeatHandler(self, s):
        if(self.crossedChrDict.get(s[self.index]) == None):
            self.crossedChrDict[s[self.index]] = self.index
            self.currentStrLength = self.currentStrLength + 1

    def setMaxLengthStr(self):
        if(self.maxLengthStr < self.currentStrLength):
            self.maxLengthStr = self.currentStrLength


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
